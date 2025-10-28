# 1. Mostrar uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# 2. Implementar funcionalidade para adicionar um contato (Nome, Telefone, Email, Favorito)
# 3. Desenvolver visualização da lista de contatos cadastrados
# 4. Criar funcionalidade para editar um contato existente
# 5. Implementar uma opção para marcar ou desmarcar um contato como favorito
# 6. Desenvolver uma lista para a visualização de contatos favoritos
# 7. Criar funcionalidade para apagar um contato

[
    {
        "Luccas" : 
            [
                {
                "number" : "123321123"
                }
            ]
        }
]

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
    def add(self):
        self.contact = dict()
        self.info_list = list()
        self.info = dict()
        
        self.name = str(input('Nome do Contato: ')).capitalize() or ''
        is_dup = self.dups(self.name)
        while self.name == '' or len(self.name) < 3 or is_dup:
            if is_dup:
                print("O nome já está cadastrado na agenda")
            else:
                print("O nome deve ter pelo menos 3 caracteres")
            self.name = str(input('Nome do Contato: ')).capitalize() or ''
        
        self.number = str(input('Numero do Contato: ')) or ''
        while self.number == '' or len(self.number) < 10:
            print("O numero deve ter pelo menos 10 caracteres")
            self.number = str(input('Numero do Contato: ')) or ''
        
        self.is_favorite = False
        
        self.info['number'] = self.number
        self.info['favorite'] = self.is_favorite
        self.contact[self.name] = self.info
        self.contatos.append(self.contact)
    
    def show(self, filtered=False):
        if self.is_empty():
            print("Agenda ainda está vazia")
            return 
        for c in self.contatos:
            for k,v in c.items():
                if filtered:                                                         # CHECK             
                    if v.get('favorite'):                                            # CHECK    
                        number = v.get('number')                                     # CHECK  
                        print(f"{k} - ({number[0:2]}) {number[2:6]}-{number[6:]}")   # CHECK  
                else:
                    
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
                    c.get(name).update({'number' : number })
                else:
                    c.get(name).update({'favorite':not c.get(name).get('favorite')})
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
        while op not in ['1','2','3','4','-1']:
            print("1- Adicionar Contato \n2- Listar Contatos \n3- Atualizar Contato\n")
            op = str(input("Selecione uma ação : "))
        action = {"1": (agenda.add,), "2": (agenda.show,), "3":(agenda.update,), "4":(agenda.update,'favorite'), "-1":(agenda.close,)}
        f = action.get(op)
        f[0](f[1])
    except KeyboardInterrupt:
        agenda.close()
    except IndexError:
        f[0]()
    