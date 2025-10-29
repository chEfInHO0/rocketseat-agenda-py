# 1. Mostrar uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# 2. Implementar funcionalidade para adicionar um contato (Nome, Telefone, Email, Favorito)
# 3. Desenvolver visualização da lista de contatos cadastrados
# 4. Criar funcionalidade para editar um contato existente
# 5. Implementar uma opção para marcar ou desmarcar um contato como favorito
# 6. Desenvolver uma lista para a visualização de contatos favoritos
# 7. Criar funcionalidade para apagar um contato
from string import digits
from os import system


class Agenda:
    def __init__(self, testing=False):
        self.contatos = list()
        self.testing = testing

    def dups(self, name):
        for c in self.contatos:
            if c.get(name):
                return True
        return False

    def is_empty(self):
        if len(self.contatos) == 0:
            return True
        else:
            return False

    def format_number(self, number: str):
        if len(number) == 10:
            return f"({number[0:2]}) {number[2:6]}-{number[6:]}"
        elif len(number) == 11:
            return f"({number[0:2]}) {number[2]} {number[3:7]}-{number[7:]}"
        else:
            return None

    def pretty_print(self, msg):
        print("#"*20)
        print(msg)
        print("#"*20)

    def show_format(self, contato, number):
        print(f"{contato} - {self.format_number(number)}".rjust(35, " "))

    def sanitize(self, stdout):
        _accept = list(digits)
        for i in stdout:
            if i not in _accept:
                stdout = stdout.replace(i, '')
        return stdout

    def add(self):
        contact = dict()
        info = dict()

        name = str(input('Nome do Contato: ')).capitalize() or ''

        while len(name) < 3 or self.dups(name):
            if name == '':
                print("\n### Cadastro abortado ###\n")
                return 400
            elif self.dups(name):
                print("O nome já está cadastrado na agenda")
                return 401
            else:
                print("O nome deve ter pelo menos 3 caracteres")
            name = str(input('Nome do Contato: ')).capitalize() or ''

        number = self.sanitize(str(input('Numero do Contato: ')) or '')

        while len(number) < 10 or len(number) > 11:
            if number == '':
                print("\n### Cadastro abortado ###\n")
                return 400
            print("O numero deve ter pelo menos 10 e no máximo 11 dígitos")
            number = self.sanitize(
                str(input('Numero do Contato: ')) or '')

        is_favorite = False

        info['number'] = number
        info['favorite'] = is_favorite
        contact[name] = info
        self.contatos.append(contact)
        print('\n### Contato adicionado ###\n')
        return 201

    def show(self, filtered=False):
        """
        filtered controla a exibição dos contatos entre todos e apenas os favoritos
        """
        if self.is_empty():
            print("\n### Agenda ainda está vazia ###\n")
            return 412
        self.pretty_print("Lista de Contatos Favoritos : ") if filtered else self.pretty_print(
            "Lista de Contatos : ")
        for c in self.contatos:
            for k, v in c.items():
                if filtered:
                    if v.get('favorite'):
                        self.show_format(k, v.get('number'))
                else:
                    self.show_format(k, v.get('number'))
        input("Pressione ENTER para continuar")
        system('cls')
        return 200

    def show_one(self, name):
        if len(self.contatos) == 0:
            print("\n### Agenda vazia ###\n")
            return 412
        else:
            try:
                print(self.contatos)
                for c in self.contatos:
                    if c.get(name):
                        print(name, c.get(name))
                        return 200
                return 404
            except Exception:
                return 500

    def update(self, update_type='number'):
        if self.is_empty():
            print("\n### Agenda ainda está vazia ###\n")
            return 412
        name = str(input('Nome do Contato: ')).capitalize() or ''
        while name == '' or len(name) < 3:
            name = str(input('Nome do Contato: ')).capitalize() or ''
        for c in self.contatos:
            if c.get(name):
                if update_type == 'number':
                    number = str(input('Numero do Contato: ')) or ''
                    while len(number) < 9 or number == c.get(name).get('number'):
                        if number == '':
                            print("\n### Atualização abortada ###\n")
                            return 400
                        number = str(input('Numero do Contato: ')) or ''
                    c.get(name).update({'number': number})
                    print(f"O contato {c.get(name)} foi atualizado")
                else:
                    c.get(name).update(
                        {'favorite': not c.get(name).get('favorite')})
                    print(f"O contato {c.get(name)} foi adicionado aos favoritos") if c.get(name).get(
                        'favorite') else print(f"O contato {c.get(name)} foi removido dos favoritos")
                return 204
        print("\n### Nome não encontrado na lista ###\n")
        return 404

    def delete(self):
        if self.is_empty():
            print("\n### Agenda ainda está vazia ###\n")
            return 412
        name = str(input('Nome do Contato: ')).capitalize() or ''
        while len(name) < 3:
            if name == '':
                print("\n### Ação abortada ###\n")
                return 400
            name = str(input('Nome do Contato: ')).capitalize() or ''
        for c in self.contatos:
            if c.get(name):
                return 204
        print("\n### Nome não encontrado na lista ###\n")
        return 404

    def close(self):
        print("\nTchau")
        exit()


agenda = Agenda(True)

if not agenda.testing:
    loop = True
    while loop:
        try:
            op = -1
            while op not in ['1', '2', '3', '4', '5', '6', '0']:
                print("\n 1 - Adicionar Contato \n 2 - Listar Contatos \n 3 - Atualizar Contato\n 4 - (Des)Favoritar Contato\n 5 - Listar contatos Favoritos\n 6 - Deletar Contato\n 0 - Sair\n")
                op = str(input("Selecione uma ação : "))
            action = {
                "1": (agenda.add,), "2": (agenda.show,),
                "3": (agenda.update,), "4": (agenda.update, 'favorite'),
                "5": (agenda.show, True), "0": (agenda.close,)}
            f = action.get(op)
            f[0](f[1])
        except KeyboardInterrupt:
            agenda.close()
        except IndexError:
            f[0]()
