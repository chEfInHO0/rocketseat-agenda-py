# 1. Mostrar uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# 2. Implementar funcionalidade para adicionar um contato (Nome, Telefone, Email, Favorito)
# 3. Desenvolver visualização da lista de contatos cadastrados
# 4. Criar funcionalidade para editar um contato existente
# 5. Implementar uma opção para marcar ou desmarcar um contato como favorito
# 6. Desenvolver uma lista para a visualização de contatos favoritos
# 7. Criar funcionalidade para apagar um contato


class Agenda:
    def __init__(self):
        self.contatos = list()

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
        print(f"{contato} - {self.format_number(number)}".rjust(25, " "))

    def add(self):
        self.contact = dict()
        self.info = dict()

        self.name = str(input('Nome do Contato: ')).capitalize() or ''

        while self.name == '' or len(self.name) < 3 or self.dups(self.name):
            if self.dups(self.name):
                print("O nome já está cadastrado na agenda")
            else:
                print("O nome deve ter pelo menos 3 caracteres")
            self.name = str(input('Nome do Contato: ')).capitalize() or ''

        self.number = str(input('Numero do Contato: ')) or ''

        while self.number == '' or len(self.number) < 10 or len(self.number) > 11:
            print("O numero deve ter pelo menos 10 e no máximo 11 dígitos")
            self.number = str(input('Numero do Contato: ')) or ''

        self.is_favorite = False

        self.info['number'] = self.number
        self.info['favorite'] = self.is_favorite
        self.contact[self.name] = self.info
        self.contatos.append(self.contact)

    def show(self, filtered=False):
        """
        filtered controla a exibição dos contatos entre todos e apenas os favoritos
        """
        if self.is_empty():
            print("Agenda ainda está vazia")
            return
        self.pretty_print("Lista de Contatos Favoritos : ") if filtered else self.pretty_print(
            "Lista de Contatos : ")
        for c in self.contatos:
            for k, v in c.items():
                if filtered:
                    if v.get('favorite'):
                        self.show_format(k, v.get('number'))
                else:
                    self.show_format(k, v.get('number'))

    def update(self, update_type='number'):
        if self.is_empty():
            print("Agenda ainda está vazia")
            return
        name = str(input('Nome do Contato: ')).capitalize() or ''
        while name == '' or len(name) < 3:
            self.name = str(input('Nome do Contato: ')).capitalize() or ''
        for c in self.contatos:
            if c.get(name):
                if update_type == 'number':
                    number = str(input('Numero do Contato: ')) or ''
                    while number == '' or len(number) < 9 or number == c.get(name).get('number'):
                        number = str(input('Numero do Contato: ')) or ''
                    c.get(name).update({'number': number})
                else:
                    c.get(name).update(
                        {'favorite': not c.get(name).get('favorite')})
                return True
        print("Nome não encontrado na lista")

    def close(self):
        print("\nTchau")
        exit()


agenda = Agenda()

loop = True
while loop:
    try:
        op = 0
        while op not in ['1', '2', '3', '4', '5', '-1']:
            print("1- Adicionar Contato \n2- Listar Contatos \n3- Atualizar Contato\n")
            op = str(input("Selecione uma ação : "))
        action = {
            "1": (agenda.add,), "2": (agenda.show,),
            "3": (agenda.update,), "4": (agenda.update, 'favorite'),
            "5": (agenda.show, True), "-1": (agenda.close,)}
        f = action.get(op)
        f[0](f[1])
    except KeyboardInterrupt:
        agenda.close()
    except IndexError:
        f[0]()
