# MINI PROJETO 2 DO SQUAD CINZA-B - DSD 2021 #
# Integrantes: Victor, Thomas e Rodrigo
import csv, os, json, sys
from typing import DefaultDict

import prettytable
from CorrigeCSV import CorrigeCSV
from Contato import Contato
from Grupo import Grupo
import pip

class Agenda:
    '''
    Classe para operar arquivo 'agenda.csv'
    '''
    @staticmethod
    def criar_agenda():
        lista = CorrigeCSV.cria_lista('contatos_corrigido.csv')
        lista_dict = Agenda.conv_Miniprojeto2(lista)

        header = ['id','nome','sobrenome','tel','email', 'status']          ##### passei de dicionário para lista
        arquivo = open('agenda.csv', 'w+', encoding='utf-8', newline='')    ##### incluído newline
        writer = csv.DictWriter(arquivo, fieldnames=header, delimiter=";")
        writer.writeheader()
        for contato in lista_dict:
            writer.writerow(contato)

        arquivo.close()

    @staticmethod
    def div():
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

    @staticmethod
    def conv_Miniprojeto2(lista):
        '''
        Função para criar uma lista no formato do Miniprojeto 2
        [ { 'id': '','nome': '',     'sobrenome': '','tel': [],'email': [] } ]
        a partir de uma lista no formato do Miniprojeto 1 
        ['nome', 'telefone', 'email'].
        '''
        lista_contatos = []
        contato = {}
        for dados in lista:
            contato = {}
            contato['id'] = lista.index(dados)+1
            contato['nome'] = dados[0].lower()
            contato['sobrenome'] = ''
            contato['tel'] = [dados[1]]
            contato['email'] = [dados[2]].lower()
            contato['status'] = 'ativo'
            lista_contatos.append(contato)
        return lista_contatos

    @staticmethod
    def import_or_install(package):
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])

    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # carrega parametros inciais e lê arquivos
        self.load()
        self.exibir_completo()

        # main loop
        lista_opcoes = [str(i) for i in range(0,13)]
        while True:
            opcao = ""
            while opcao not in lista_opcoes:
                print("\n")
                opcao = input("Digite o número referente a uma das opções a seguir:"
                    "\n\t [1] - Exibir todos os contatos da agenda"
                    "\t\t [8] - Criar um grupo novo"
                    "\n\t [2] - Exibir informações detalhadas de um contato"
                    "\t [9] - Remover um grupo"
                    "\n\t [3] - Buscar contato"
                    "\t\t\t\t\t [10] - Listar grupos"
                    "\n\t [4] - Adicionar um contato"
                    "\t\t\t\t [11] - Remover contato de um grupo"
                    "\n\t [5] - Remover um contato"
                    "\t\t\t\t [12] - Listar contatos do grupo"
                    "\n\t [6] - Modificar um contato"
                    "\t\t\t\t [0]  - Salvar modificações e sair"
                    "\n\t [7] - Incluir o contato em algum grupo\n")

            # exibir todos
            if opcao == "1":
                self.exibir_completo()
            
            # exibir único
            elif opcao == "2":
                ident = input("Digite o ID do contato. [0] para cancelar: ")
                while ident not in self.ids_ativos and ident != "0":
                    ident = input("ID não encontrado. Digite o ID novamente ou [0] para cancelar: ")
                if ident == "0":
                    print("Operação cancelada.")
                else:
                    for contato in self.lista_contatos:
                        if contato.id == ident:
                            contato.exibir_contato()
            
            # buscar contato
            elif opcao == "3":
                contato = self.buscar_contato()
                if contato != "":
                    contato.exibir_contato()
                else:
                    print("Contato não encontrado, favor verifique os parâmetros informados e tente novamente")
            #T
            # adicionar contato
            elif opcao == "4":
                self.add_contato()
            #T
            # remover contato
            elif opcao == "5":
                self.rmv_contato()
            #V
            # modificar contato
            elif opcao == "6":
                ident = input("Digite o ID do contato a ser modificado. [0] para cancelar: ")
                while ident not in self.ids_ativos and ident != "0":
                    ident = input("ID não encontrado. Digite o ID do contato a ser modificado ou [0] para cancelar: ")
                if ident == "0":
                    print("Operação cancelada.")
                else:
                    for contato in self.lista_contatos:
                        if contato.id == ident:
                            print("\nO contato a seguir será modificado:")
                            contato.exibir_contato()
                            contato.mod_contato()
            #R
            # incluir contato em grupo
            elif opcao == "7":
                print("-------Adicionar um contato em um grupo------")
                escolha = "N"
                while escolha == "N":
                    nome_grupo = input ("Digite o nome do grupo que você deseja incluir o usuário: ").lower()
                    id_contato = input("Digite o número do ID do contato que deseja incluir: ")#aqui se considera o ID como uma string
                    if id_contato in self.ids_ativos:
                        escolha = input(f"Deseja incluir o usuário de ID {id_contato} no grupo {nome_grupo}? [S/N] ").upper()
                        if escolha != "S":
                            escolha = "N"
                            break
                        else:
                            Grupo.adiciona_contato_grupo(id_contato, nome_grupo)
                    else:
                        print("ID informado é inválido.")
                        break
            #R
            # criar um grupo
            elif opcao == "8":
                print("-------Criar um grupo novo-------")
                escolha = "N"
                while escolha == "N":
                    nome_grupo = input("Digite o nome do grupo que deseja criar: ").lower()
                    escolha = input(f"Nome digitado: {nome_grupo}. Deseja confirmar esse nome?[S/N] ").upper()
                    if escolha != "S":
                        escolha = "N"
                        break
                Grupo.cria_grupo(nome_grupo)
            #R
            elif opcao == "9":
                print("-------Remover um grupo-------")
                escolha = "N"
                while escolha == "N":
                    nome_grupo = input("Digite o nome do grupo que deseja remover: ").lower()
                    escolha = input(f"Nome digitado: {nome_grupo}. Deseja confirmar esse nome?[S/N] ").upper()
                    if escolha != "S":
                        escolha = "N"
                        break
                Grupo.remove_grupo(nome_grupo)
            #R
            elif opcao == "10":
                Grupo.lista_grupos()
            #R
            elif opcao == "11":
                print("-------Remover contato de um grupo-------")
                escolha = "N"
                while escolha == "N":
                    nome_grupo = input ("Digite o nome de qual grupo deseja remover o usuário: ").lower()
                    id_contato = input("Digite o número do ID do contato que deseja remover: ")#aqui se considera o ID como uma string
                    if id_contato in self.ids_ativos:
                        escolha = input(f"Deseja incluir o usuário de ID {id_contato} no grupo {nome_grupo}? [S/N] ").upper()
                        if escolha != "S":
                            escolha = "N"
                            break
                        else:
                            Grupo.remove_contato_grupo(id_contato, nome_grupo)
                    else:
                        print("ID informado é inválido.")
                        break
            #R
            elif opcao == "12":
                print("-------Listar contatos do grupo-------")
                nome_grupo = input("Digite o nome do grupo cujos contatos deseja ver: ").lower()
                Grupo.mostrar_contatos_grupo(nome_grupo, self.lista_contatos)

            else:
                # print("Encerrando o programa...")
                break

        self.save() # escreve agenda no agenda.csv e grupos no json
        # os.system('cls')
        # sys.exit()

    def load(self):
        # install packages
        Agenda.import_or_install('prettytable')

        # obter dados de grupos salvos no csv (mesmo ou outro?) ou json
        try:
            with open("grupos.json") as f_obj:
                Grupo.grupos = json.load(f_obj)
        except FileNotFoundError:
            Grupo.grupos = {}

        # obter lista de contatos
        self.lista_contatos = []
        try:
            with open('agenda.csv', 'r+', encoding="utf-8") as f:
                tabela_contatos = csv.reader(f, delimiter=";", lineterminator="\n")
                for linha in tabela_contatos:
                    contato = Contato(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
                    self.lista_contatos.append(contato)
                self.lista_contatos.pop(0) # pop header
        except FileNotFoundError:
            self.lista_contatos = []
            print("Houve um erro ao fazer a leitura da agenda.")
        
        # obter ids e ids ativos
        self.get_ids()
        self.get_ativos()
        self.tamanho = len(self.ids_ativos)
        self.limite = 75

    def save(self):
        # salvar dados de grupos
        if Grupo.grupos:
            with open("grupos.json", 'w') as f_obj:
                json.dump(Grupo.grupos, f_obj)

        # salvar agenda
        header = ['id','nome','sobrenome','tel','email', 'status']          ##### passei de dicionário para lista
        arquivo = open('agenda.csv', 'w+', encoding='utf-8', newline='')    ##### incluído newline
        writer = csv.DictWriter(arquivo, fieldnames=header, delimiter=";")
        writer.writeheader()
        for contato in self.lista_contatos:
            writer.writerow(contato.__dict__)

        arquivo.close()

    def get_ativos(self):
        ids = []
        for contato in self.lista_contatos:
            if contato.status == "ativo":
                ids.append(contato.id)
        ids.sort()
        self.ids_ativos = ids
    
    def get_ids(self):
        ids = []
        for contato in self.lista_contatos:
            ids.append(contato.id)
        ids = [int(i) for i in ids]
        ids.sort()
        ids = [str(i) for i in ids]
        self.ids = ids

    def exibir_completo(self):
        Agenda.div()
        t = prettytable.PrettyTable(["ID","Nome","Sobrenome","Telefone","E-mail"])
        #print("ID\t\tNome\t\t\tSobrenome\t\t\tTelefone\t\t\t\tE-mail") # table header
        for contato in self.lista_contatos:
            if contato.status == "ativo":
                t.add_row([contato.id, contato.nome.title(), contato.sobrenome.title(), contato.tel, contato.email])
                #contato.exibir_contato("simple")
        print(t)

    def buscar_contato(self):
        opt = ''
        desc_opts = ['nome', 'sobrenome', 'telefone (somente números)', 'e-mail']
        num_opts = ['1','2','3','4','0']
        while opt not in num_opts:
            opt = input("Digite a opção pela qual deseja buscar um contato: \n\t1 - Nome\n\t2 - Sobrenome\n\t3 - Telefone\n\t4 - E-mail\n\t0 - Cancelar\n")

        if opt == "0":
            print("Operação cancelada.\n")
        else:
            value = ''
            while value == '' or value.isspace():
                value = input(f"Informe o {desc_opts[int(opt)-1]}: \n").lower()

            for contato in self.lista_contatos:
                if opt == "1":
                    attr = contato.nome
                elif opt == "2":
                    attr = contato.sobrenome
                elif opt == "3":
                    attr = contato.tel
                elif opt == "4":
                    attr = contato.email

                if value in attr and contato.status == "ativo":
                    return contato
        return ""
                    

    def add_contato(self):
        self.ids = [int(i) for i in self.ids]
        self.ids.sort()
        new_id = int(self.ids[-1]) + 1
        self.ids = [str(i) for i in self.ids]
        if str(new_id) in self.ids: # não vai acontecer na teoria
            print("Houve um erro ao adicionar novo contato.")
        elif self.tamanho >= self.limite:
            print(f"Não é possível adicionar mais contatos. Limite máximo [{self.limite}] atingido.")
        else:
            # nome
            nome = input("Digite o nome: ").lower().strip()
            while nome == "" or nome.isspace():
                nome = input("Inválido. Digite o nome: ").lower().strip()
            print("Nome adicionado.")

            # sobrenome;
            sobrenome = input("Digite o sobrenome: ").lower().strip()
            while sobrenome == "" or sobrenome.isspace():
                sobrenome = input("Inválido. Digite o sobrenome: ").lower().strip()
            print("Sobrenome adicionado.")

            # telefone
            lista_tel = []
            lista_tel = Contato.add_tel_email(lista_tel, "telefone")
            add = True
            while add == True:
                add_other = ""
                while add_other not in ["s", "n"]:
                    add_other = input("Deseja adicionar novo telefone? [S/N]").lower()
                if add_other == "s":
                    lista_tel = Contato.add_tel_email(lista_tel, "telefone")
                else:
                    add = False

            # email
            lista_email = []
            lista_email = Contato.add_tel_email(lista_email, "e-mail")
            add = True
            while add == True:
                add_other = ""
                while add_other not in ["s", "n"]:
                    add_other = input("Deseja adicionar novo e-mail? [S/N]").lower()
                if add_other == "s":
                    lista_email = Contato.add_tel_email(lista_email, "e-mail")
                else:
                    add = False

            contato = Contato(str(new_id), nome, sobrenome, lista_tel, lista_email, "ativo")
            self.lista_contatos.append(contato)

            self.get_ids()
            self.get_ativos()
            self.tamanho = len(self.ids_ativos)

            print("Contato adicionado com sucesso.")

    def rmv_contato(self):
        if not self.ids_ativos:
            print("Não há contatos na agenda.")
        else:
            ident = input("Digite o ID do contato a ser removido. [0] para cancelar: ")
            while ident not in self.ids_ativos and ident != "0":
                ident = input("ID não encontrado. Digite o ID do contato a ser removido ou [0] para cancelar: ")
            
            if ident == "0":
                print("Operação cancelada.")
            else:
                for contato in self.lista_contatos:
                    if contato.id == ident:
                        print("O contato a seguir será removido:")
                        contato.exibir_contato()
                        opt = input("Tem certeza que deseja continuar? [S/N]")
                        while opt.lower() not in ["s", "n"]:
                            opt = input("Opção inválida. Tem certeza que deseja continuar? [S/N]")

                        if opt.lower() == "s":
                            for nome_grupo in Grupo.grupos:
                                Grupo.remove_contato_grupo(contato.id, nome_grupo, False)
                            contato.status = "inativo"
                            print("Contato removido com sucesso")
                            self.get_ids()
                            self.get_ativos()
                            self.tamanho = len(self.ids_ativos)
                        else:
                            print("Operação cancelada.")


'''
Método "Exibir contato" para printar na tela um contato, passando o ID como input -> id+nome+snome -> função BASE, as outras utilizam
Método "Exibir completo" -> exibe tudo -> função BASE, as outras utilizam
Método "Buscar contato" -> input id, nome ou email ou tel e retorna resultados encontrados
Método CONTAR numero de linhas com status ativo para limitar em 75 a criação de contato !
Método "Adicionar Contato" -> chamar método de CONTAR autom. e barrar/SUMIR OPÇÃO caso esteja cheio -> criar objeto Contato
Método "Remover Contato" -> remover por id, mostrar infos antes de remover p/ confirmar
Opcional (se der tempo...) -> colocar num csv de removidos/histórico + data de remoção
Método "Modificar Contato" -> escolher por ID, ver infos, e depois número correspondente ao campo desejado (1 = nome, 2 = email...)
Método para atribuir um grupo (kv ex.: "grupo":"admin", número ou letra) a um contato #- Método "Atribuir grupo" -> grupo pode ser outro dict, com chave sendo os grupos e valores os ids
Método "Criar grupo", "Remover grupo"
Método "Filtrar grupo" -> input "G1", procurar valores com nome do grupo, add numa lista e loop para jogar na tela
'''