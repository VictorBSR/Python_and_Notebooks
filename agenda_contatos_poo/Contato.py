# MINI PROJETO 2 DO SQUAD CINZA-B - DSD 2021 #
# Integrantes: Victor, Thomas e Rodrigo

class Contato:
    
    def __init__(self, id, nome, sobrenome, lista_tel, lista_email, status = "ativo"):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.tel = lista_tel
        self.email = lista_email
        self.status = status

    def exibir_contato(self, style = 'detailed'):
        if style == 'simple':
            # treating spaces and tabulation
            """ if len(contato['nome']) > 15: contato['nome'] = contato['nome'][:12] + '...'
            if len(contato['nome']) < 8: contato['nome'] = contato['nome'] + ' '*3
            if len(contato['sobrenome']) > 15: contato['nome'] = contato['nome'][:12] + '...'
            if len(contato['sobrenome']) < 8: contato['nome'] = contato['nome'] + ' '*3
            if len(contato['tel']) > 2: contato['tel'] = [contato['tel'][0],contato['tel'][1],"..."]
            if len(contato['tel']) == 2: contato['tel'] = '[' + ', '.join(contato['tel']) + ']\t'
            if len(contato['tel']) < 2: contato['tel'] = '[' + ', '.join(contato['tel']) + ']\t\t\t'
            if len(contato['email']) > 2: contato['email'] = [contato['email'][0],contato['email'][1],"..."]
            if len(contato['email']) == 2: contato['email'] = '[' + ', '.join(contato['email']) + ']\t'
            if len(contato['email']) < 2: contato['email'] = '[' + ', '.join(contato['email']) + ']\t\t\t' """
            # print("ID\t\tNome\t\t\tSobrenome\t\t\tTelefone\t\t\t\tE-mail\t\t\t\t\tGrupos") # table header
            print(f"{self.id}\t\t{self.nome.title()}\t\t\t{self.sobrenome.title()}\t\t\t\t{self.tel}\t\t\t\t{self.email}")

        elif style == 'detailed':
            print(f"Contato ID nº {self.id}:")
            print(f"\tNome: {self.nome.title() + ' ' + self.sobrenome.title()}")
            print(f"\tTelefone: {self.tel}")
            print(f"\tE-mail: {self.email}")

    @staticmethod
    def add_tel_email(lista, tipo):
        dado = input(f"Digite o {tipo} a ser adicionado. [0] para cancelar: ").lower().strip()
        if dado == "0":
            print("Operação cancelada.")
            pass
        else:
            while dado == "" or dado.isspace():
                dado = input(f"Inválido. Digite o {tipo} a ser adicionado. [0] para cancelar: ").lower().strip()
            if dado == "0":
                print("Operação cancelada.")
            else:
                lista.append(dado)
                print(f"{tipo.title()} adicionado.")
        return lista

    @staticmethod
    def rmv_tel_email(lista, tipo):
        if not lista:
            print(f"Não há {tipo}s para serem removidos.")
        else:
            dado = input(f"Digite o {tipo} a ser removido. [0] para cancelar: ").lower().strip()
            if dado == "0":
                print("Operação cancelada.")
                pass
            else:
                while dado not in lista:
                    dado = input(f"Inválido. Digite o {tipo} a ser removido. [0] para cancelar: ").lower().strip()
                    if dado == "0":
                        print("Operação cancelada.")
                        break
                try:
                    lista.remove(dado)
                except:
                    print("Valor não é válido.")
                print(f"{tipo.title()} removido.")
        return lista

    def mod_contato(self):
        opt = ''
        num_opts = ['1','2','3','4','0']
        while opt not in num_opts:
            opt = input("Digite a opção referente ao campo a ser modificado: \n\t1 - Nome\n\t2 - Sobrenome\n\t3 - Telefone\n\t4 - E-mail\n\t0 - Cancelar\n")

        if opt == "0":
            print("Operação cancelada.\n")
        elif opt == "1":
            value = ''
            while value == '' or value.isspace():
                value = input("Informe o novo nome: \n").lower().strip()
            self.nome = value
            print("Nome atualizado com sucesso.")
        elif opt == "2":
            value = ''
            while value == '' or value.isspace():
                value = input("Informe o novo sobrenome: \n").lower().strip()
            self.sobrenome = value
            print("Sobrenome atualizado com sucesso.")
        elif opt == "3":
            add = True
            while add:
                print(f"Lista de telefones: {self.tel}")
                escolha = input("O que deseja fazer?\n\t1 - Adicionar telefone\n\t2 - Remover telefone\n\t0 - Cancelar\n")
                if escolha == "1":
                    self.tel = Contato.add_tel_email(self.tel,"telefone")
                elif escolha == "2":
                    self.tel = Contato.rmv_tel_email(self.tel,"telefone")
                elif escolha == "0":
                    print("Operação cancelada.")
                    add = False
                    break

                escolha = input(f"Deseja realizar outra operação? [S/N]").lower()
                if escolha == "n":
                    add = False
                    break
        elif opt == "4":
            add = True
            while add:
                print(f"Lista de e-mails: {self.email}")
                escolha = input("O que deseja fazer?\n\t1 - Adicionar e-mail\n\t2 - Remover e-mail\n\t0 - Cancelar\n")
                if escolha == "1":
                    self.email = Contato.add_tel_email(self.email,"e-mail")
                elif escolha == "2":
                    self.email = Contato.rmv_tel_email(self.email,"e-mail")
                elif escolha == "0":
                    print("Operação cancelada.")
                    add = False
                    break

                escolha = input(f"Deseja realizar outra operação? [S/N]").lower()
                if escolha == "n":
                    add = False
                    break
