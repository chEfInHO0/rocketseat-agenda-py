# 1. Mostrar uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# 2. Implementar funcionalidade para adicionar um contato (Nome, Telefone, Email, Favorito)
# 3. Desenvolver visualização da lista de contatos cadastrados
# 4. Criar funcionalidade para editar um contato existente
# 5. Implementar uma opção para marcar ou desmarcar um contato como favorito
# 6. Desenvolver uma lista para a visualização de contatos favoritos
# 7. Criar funcionalidade para apagar um contato
from string import digits
from os import system
import re

class Agenda:
    def __init__(self):
        self.contatos = list()
        self.preserve_state(preserve='', state='clear')

    def reset_state(self):
        self.__preserve_name = None
        self.__preserve_number = None
        self.__preserve_email = None

    def preserve_state(self, preserve:str, state:str):
        if preserve == 'name':
            self.__preserve_name = state
        elif preserve == 'number':
            self.__preserve_number = state
        elif preserve == 'email':
            self.__preserve_email = state
        else:
            self.reset_state()

    def dups(self,key, value):
        for c in self.contatos:
            if c.get(key) == value:
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

    def pretty_print(self, msg:str):
        print("#"*40)
        print(msg.center(40))
        print("#"*40)

    def show_format(self, contato, number, email):
        print(f"{contato} - {self.format_number(number)} - {email}".center(35))

    def sanitize(self, stdout):
        _accept = list(digits)
        for i in stdout:
            if i not in _accept:
                stdout = stdout.replace(i, '')
        return stdout

    def check_email(self, email:str):
        EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if len(email) > 254:
            self.pretty_print(f"❌ E-mail muito longo: {email}")
            return '',401
            
        if re.fullmatch(EMAIL_REGEX, email):
            return email,200  
        else:
            self.pretty_print(f"❌ o email {email} é inválido")
            return '',401

    def request_name(self, update=False):
        if self.__preserve_name is None:
            self.pretty_print("NOME")
            name = str(input('Nome do Contato: ')) or ''
        if self.__preserve_name is not None :
            print(f"Deseja usar o ultimo valor digitado para nome como busca? NOME : {self.__preserve_name}")
            try:
                r = input("[S]Sim / [N]Não ").strip().upper()[0]
            except IndexError:
                r = "N"
            if r == 'S':
                name = self.__preserve_name
            else:
                self.reset_state()
                name = str(input('Nome do Contato: ')) or ''
        if len(name) < 3 or (not update and self.dups('name',name)):
            if name == '':
                self.pretty_print("CADASTRO ABORTADO")
                return '',400
            if not update and self.dups('name',name):
                self.pretty_print("O nome já está cadastrado")
                return '',401
            else:
                self.pretty_print("O nome deve ter pelo menos 3 caracteres")
                return '',401
        else:
            self.preserve_state('name',name)
            return name,200
        
    def request_number(self):
        if self.__preserve_number is None:
            self.pretty_print("NÚMERO")
            number = self.sanitize(str(input('Numero do Contato: ')) or '')
        if self.__preserve_number is not None :
            print(f"Deseja usar o ultimo valor digitado para nome como busca? NOME : {self.__preserve_number}")
            try:
                r = input("[S]Sim / [N]Não ").strip().upper()[0]
            except IndexError:
                r = "N"
            if r == 'S':
                number = self.__preserve_number
            else:
                self.reset_state()
        
        if len(number) < 10 or len(number) > 11:
            if number == '':
                self.pretty_print("CADASTRO ABORTADO")
                return '',400
            else:
                self.pretty_print("O numero deve ter pelo menos 10 e no máximo 11 digitos")
                return '',401
        else:
            self.preserve_state('number',number)
            return number,200

    def request_email(self):
        if self.__preserve_email is None:
            self.pretty_print("EMAIL")
            email, email_status = self.check_email(str(input('Email do Contato: ')).strip()) or ''
        if self.__preserve_email is not None :
            print(f"Deseja usar o ultimo valor digitado para nome como busca? NOME : {self.__preserve_email}")
            try:
                r = input("[S]Sim / [N]Não ").strip().upper()[0]
            except IndexError:
                r = "N"
            if r == 'S':
                email = self.__preserve_email
            else:
                self.reset_state()
        if email_status == 200:
            for c in self.contatos:
                if self.dups('email',email):
                    return '',401
            self.preserve_state('email',email)
            return email,200  
        return '',401
    
    def add(self):
        info = dict()
        self.pretty_print("Adicionar contato")
        name,name_status = self.request_name()
        if name_status != 200:
            return 401
        
        number,number_status = self.request_number()
        if number_status != 200:
            return 401
        email, email_status = self.request_email()
        if email_status != 200:
            return 401
        is_favorite = False
        
        info['name'] = name
        info['number'] = number
        info['email'] = email
        info['favorite'] = is_favorite
        self.contatos.append(info)
        print('\n### Contato adicionado ###\n')
        self.reset_state()
        return 201

    def show(self, filtered=False):
        """
        filtered controla a exibição dos contatos entre todos e apenas os favoritos
        """
        self.reset_state()
        if self.is_empty():
            print("\n### Agenda ainda está vazia ###\n")
            return 412
        self.pretty_print("Lista de Contatos Favoritos : ") if filtered else self.pretty_print(
            "Lista de Contatos : ")
        for c in self.contatos:
            if filtered:
                if c.get('favorite'):
                    self.show_format(c.get('name'), c.get('number'), c.get('email'))
            else:
                self.show_format(c.get('name'), c.get('number'), c.get('email'))
        input("Pressione ENTER para continuar")
        system('cls')
        return 200

    def show_one(self, name):
        if len(self.contatos) == 0:
            print("\n### Agenda vazia ###\n")
            return 412
        else:
            try:
                for c in self.contatos:
                    if c.get('name') == name:
                        print(c.get('name'), c.get('number'), c.get('email') )
                        return 200
                return 404
            except Exception:
                return 500

    def update(self, update_type='number'):
        if self.is_empty():
            print("\n### Agenda ainda está vazia ###\n")
            return 412
        self.pretty_print("Atualizar contato")
        name,name_status = self.request_name(update=True)
        if name_status != 200:
            return 401
        for c in self.contatos:
            if c.get('name') == name:
                if update_type == 'number':
                    number,number_status = self.request_number()
                    if number_status != 200:
                        return 401
                    c.update({'number': number})
                    self.pretty_print(f"O contato {name} foi atualizado")
                elif update_type == 'email':
                    email,email_status = self.request_email()
                    if email_status != 200:
                        return 401
                    c.update({'email': email})
                    self.pretty_print(f"O contato {name} foi atualizado")
                else:
                    c.update(
                        {'favorite': not c.get('favorite')})
                    self.pretty_print(f"O contato {name} foi adicionado aos favoritos") if c.get(
                        'favorite') else self.pretty_print(f"O contato {name} foi removido dos favoritos")
                return 204
        print("\n### Nome não encontrado na lista ###\n")
        return 404

    def delete(self):
        if self.is_empty():
            print("\n### Agenda ainda está vazia ###\n")
            return 412
        self.pretty_print("Deletar contato")
        name = str(input('Nome do Contato: ')).capitalize() or ''
        while len(name) < 3:
            if name == '':
                print("\n### Ação abortada ###\n")
                return 400
            name = str(input('Nome do Contato: ')).capitalize() or ''
        for c in self.contatos:
            if c.get('name') == name:
                self.contatos.remove(c)
                print("\n### Contato deletado ###\n")
                return 204
        print("\n### Nome não encontrado na lista ###\n")
        return 404

    def close(self):
        print("\nTchau")
        exit()



agenda = Agenda()


loop = True
while loop:
    try:
        op = -1
        while op not in ['1', '2', '3', '4', '5', '6', '0']:
            print("\n 1 - Adicionar Contato \n 2 - Listar Contatos \n 3 - Atualizar Contato\n 4 - (Des)Favoritar Contato\n 5 - Listar contatos Favoritos\n 6 - Deletar Contato\n 0 - Sair\n")
            try:
                op = str(input("Selecione uma ação : "))[0]
            except IndexError:
                op = '-1'
        action = {
            "1": (agenda.add,None), "2": (agenda.show,None),
            "3": (agenda.update,None), "4": (agenda.update, 'favorite'),
            "5": (agenda.show, True), "6" : (agenda.delete,None),
              "0": (agenda.close,None)}
        f = action.get(op)
        if f[1] is not None:
            f[0](f[1])
        else:
            f[0]()
    except KeyboardInterrupt:
        agenda.close()