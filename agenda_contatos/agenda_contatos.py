import csv
import os
from os.path import isfile, join
import sys

def cria_lista():

    print('============ Bem vindo ao programa corretor de arquivos ============\n')

    fileDir = os.getcwd()
    fileExt = r".csv"
    lista_arquivos = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]

    print(f'Existem {len(lista_arquivos)} arquivos na pasta {fileDir}. Selecione abaixo a opção que deseja importar:\n')

    for a in lista_arquivos:
        print(f'Opção {lista_arquivos.index(a)+1}: {a}')

    selecao = lista_arquivos[int(input('Importar opção: '))-1]
    arquivo = open(selecao, 'r+', encoding="utf-8")
    tabela_contatos = csv.reader(arquivo, delimiter=";", lineterminator="\n")

    lista_contatos = []
    for linha in tabela_contatos: #loop usado para transformar os dados em uma lista com os dados já presentes
        lista_contatos.append(linha)

    arquivo.close()
    return lista_contatos # exibe a lista

def verifica_nome(nome, dado):
    if dado.isalpha():
        nome.append(dado)

def verifica_tel(tel, dado):
    if dado.isnumeric():
        tel.append(dado)

def verifica_email(email, dado):
    if '@'in dado:
        email.append(dado)

def separa_lista(lista_baguncada):

    nome = []
    tel = []
    email = []

    for contatos in range(len(lista_baguncada)):
        for dados in range(3):
            verifica_nome(nome, lista_baguncada[contatos][dados])
            verifica_tel(tel, lista_baguncada[contatos][dados])
            verifica_email(email, lista_baguncada[contatos][dados])
    
    tamanho_lista = len(lista_baguncada)
    reconstroi_lista(nome, tel, email, tamanho_lista)

def reconstroi_lista(nome, tel, email, tamanho_lista):

    lista_reconst = []
    lista_reconst_parc = []

    for contatos in range(tamanho_lista):
        lista_reconst_parc.append(nome[contatos])
        lista_reconst_parc.append(tel[contatos])
        lista_reconst_parc.append(email[contatos])
        lista_reconst.insert(contatos, lista_reconst_parc)
        lista_reconst_parc = []

    salva_lista_em_csv(lista_reconst,'contatos_corrigido.csv')
    print("A correção foi realizada com sucesso e a lista foi salva no arquivo 'contatos_corrigido.csv'")

def salva_lista_em_csv(lista, nome_arquivo):
    '''
    Função salva uma lista em um arquivo .csv onde cada linha é o primeiro nível da lista e 
    os elementos de segundo nível da lista são separados entre si por ponto e vírgula ';'.   
    '''
    
    arquivo = open(nome_arquivo, 'w+', encoding='utf-8')
    csv.writer(arquivo, delimiter=';', lineterminator='\n').writerows(lista)
    arquivo.close()

def operations():
    
    brk = "\n"
    opt0 = "Digite a operação desejada:"
    opt1 = "[1] - Buscar por um registro"
    opt2 = "[2] - Adicionar um fornecedor"
    opt3 = "[3] - Remover um fornecedor"
    opt4 = "[0] - Encerrar"
    quit_msg = "Encerrando operação..."

    fileDir = os.getcwd()
    fileExt = r".csv"
    lista_arquivos = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    lista_contatos = []
    
    if any(lista_arquivos):
        arquivo = open('contatos_corrigido.csv', 'r+', encoding="utf-8")
        tabela_contatos = csv.reader(arquivo, delimiter=";", lineterminator="\n")
            
        for linha in tabela_contatos: #loop usado para transformar os dados em uma lista com os dados já presentes
            lista_contatos.append(linha)
        
        arquivo.close()

    # main loop
    while True:
        print(brk+opt0+"\n"+opt1+"\n"+opt2+"\n"+opt3+"\n"+opt4)
        select = input()
        
        if select == '0':
            print(quit_msg)
            arquivo.close()
            break

        elif select not in ["1","2","3","4"]:
            print("Opção inválida, favor tentar novamente.")
        
        # functions
        else:
            if select == '1':
                buscar_remover_registro(lista_contatos, "buscar")
            elif select == '2':
                add_registro(lista_contatos)
                salva_lista_em_csv(lista_contatos,'contatos_corrigido.csv')
            elif select == '3':
                buscar_remover_registro(lista_contatos, "remover")
                salva_lista_em_csv(lista_contatos,'contatos_corrigido.csv')
            
def add_registro(lista_corrigida):
    
    ativo = True
    while ativo: #loop incluído para manter o preenchimento de novos cadastro até o usuário solicitar para interromper
        contato_novo = []
            
        # ======= Inserindo o nome =======
        nome = input("Insira o nome do fornecedor: ").strip().title()
        while nome.isdigit() == True or nome == "":
            nome = input("Dados inválidos. Por favor digite o nome novamente: ").strip().title()
        contato_novo.append(nome)
        
        # ======= Inserindo o telefone =======
        telefone = input(f"Digite o número de telefone para o fornecedor {nome}: ").strip()
        telefone = telefone.replace(" ", "")
        while not telefone.isnumeric():
            telefone = input("Por favor digite somente números. Digite o telefone novamente: ").strip()
            telefone = telefone.replace(" ", "")
        contato_novo.append(telefone)

        # ======= Inserindo o e-mail =======
        email = input(f"Digite o e-mail para o fornecedor {nome}: ").strip().lower()
        while "@" not in email or "." not in email or " " in email:
            email = input("Dados inválidos. Por favor digite o e-mail novamente: ").strip().lower()
        contato_novo.append(email)

        lista_corrigida.append(contato_novo)

        #O bloco a seguir refere-se pergunta de incluir mais um contato antes de sair da função.

        resposta = input("Deseja incluir mais um contato na lista? Digite [S/N]")
        resposta = resposta.upper()

        while resposta != "N" and resposta != "S":
            resposta = input("Digite apenas \"S\" ou \"N\" ")
            resposta = resposta.upper()

        if resposta == "N":
            ativo = False
        #Fim do bloco

def buscar_remover_registro(lista_contatos, option):
    
    ativo = True

    while ativo: #while incluído para verificar se a operação será reiniciada pelo usuário
        if option == "buscar":
            print("============ Busca de fornecedores ============")
        elif option == "remover":
            print("============ Remoção de fornecedores ============")

        while True:
            if option == "buscar":
                campo = input("Digite a opção do campo pelo qual você deseja buscar o fornecedor:"
                              "\n\t[1] - Nome"
                              "\n\t[2] - Telefone"
                              "\n\t[3] - E-mail"
                              "\n\t[0] - Voltar"
                              "\n"
                             )
                while campo not in ["1","2","3","0"]:
                    campo = input("Opção inválida. Digite a opção do campo pelo qual você deseja buscar o fornecedor:"
                                "\n\t[1] - Nome"
                                "\n\t[2] - Telefone"
                                "\n\t[3] - E-mail"
                                "\n\t[0] - Voltar"
                                "\n"
                                )
                    
            elif option == "remover":
                campo = input("Digite a opção do campo pelo qual você deseja remover o fornecedor:"
                              "\n\t[1] - Nome"
                              "\n\t[2] - Telefone"
                              "\n\t[3] - E-mail"
                              "\n\t[0] - Voltar"
                              "\n"
                             )
                while campo not in ["1","2","3","0"]:
                    campo = input("Opção inválida. Digite a opção do campo pelo qual você deseja remover o fornecedor:"
                                "\n\t[1] - Nome"
                                "\n\t[2] - Telefone"
                                "\n\t[3] - E-mail"
                                "\n\t[0] - Voltar"
                                "\n"
                                )

            found = False
            if campo == "1": # nome

                if option == "buscar":
                    nome = input("Digite o nome do fornecedor a ser buscado: ").strip().title()
                    while nome == "":
                        nome = input("Nome inválido. Digite o nome do fornecedor a ser buscado: ").strip().title()

                    for contato in lista_contatos:
                        if contato[0] == nome:
                            print("Resultado encontrado:",contato,"\n")
                            found = True
                    if not found:
                        print("Não foram encontrados resultados para o nome fornecido.")
                        
                elif option == "remover":
                    nome = input("Digite o nome do fornecedor a ser removido: ").strip().title()
                    while nome == "":
                        nome = input("Nome inválido. Digite o nome do fornecedor a ser removido: ").strip().title()

                    for contato in lista_contatos:
                        if contato[0] == nome:
                            resposta = input(f"Confirma exclusão do seguinte fornecedor [S/N]? {contato} \n").upper()
                            while resposta != "S" and resposta != "N":
                                resposta = input("Resposta incorreta. Digite apenas \"S\" ou \"N\": ").upper()
                            if resposta == "S":
                                lista_contatos.remove(contato)
                                print("Fornecedor removido com sucesso =>",contato,"\n")
                            found = True
                            break
                    if not found:
                        print("Não foram encontrados resultados para o nome fornecido.")


            elif campo == "2":
                
                if option == "buscar":
                    telefone = input("Digite o telefone do fornecedor a ser buscado: ").strip()
                    while telefone == "":
                        telefone = input("Telefone inválido. Digite o telefone do fornecedor a ser buscado: ").strip()

                    for contato in lista_contatos:
                        if contato[1] == telefone:
                            print("Resultado encontrado:",contato)
                            found = True
                    if not found:
                        print("Não foram encontrados resultados para o telefone fornecido.")
                    
                elif option == "remover":
                    telefone = input("Digite o telefone do fornecedor a ser removido: ").strip()
                    while telefone == "":
                        telefone = input("Telefone inválido. Digite o telefone do fornecedor a ser removido: ").strip()

                    for contato in lista_contatos:
                        if contato[1] == telefone:
                            resposta = input(f"Confirma exclusão do seguinte fornecedor [S/N]? {contato} \n").upper()
                            while resposta != "S" and resposta != "N":
                                resposta = input("Resposta incorreta. Digite apenas \"S\" ou \"N\": ").upper()
                            if resposta == "S":
                                lista_contatos.remove(contato)
                                print("Fornecedor removido com sucesso =>",contato,"\n")
                            found = True
                            break
                    if not found:
                        print("Não foram encontrados resultados para o nome fornecido.")
                    

            elif campo == "3":
                
                if option == "buscar":
                    email = input("Digite o e-mail do fornecedor a ser buscado: ").strip().lower()
                    while email == "":
                        email = input("E-mail inválido. Digite o e-mail do fornecedor a ser buscado: ").strip().lower()

                    for contato in lista_contatos:
                        if contato[2] == email:
                            print("Resultado encontrado:",contato,"\n")
                            found = True
                    if not found:
                        print("Não foram encontrados resultados para o e-mail fornecido.")
                    
                elif option == "remover":
                    email = input("Digite o e-mail do fornecedor a ser removido: ").strip().title()
                    while email == "":
                        email = input("E-mail inválido. Digite o e-mail do fornecedor a ser removido: ").strip().title()

                    for contato in lista_contatos:
                        if contato[2] == email:
                            resposta = input(f"Confirma exclusão do seguinte fornecedor [S/N]? {contato} \n").upper()
                            while resposta != "S" and resposta != "N":
                                resposta = input("Resposta incorreta. Digite apenas \"S\" ou \"N\": ").upper()
                            if resposta == "S":
                                lista_contatos.remove(contato)
                                print("Fornecedor removido com sucesso =>",contato,"\n")
                            found = True
                            break
                    if not found:
                        print("Não foram encontrados resultados para o nome fornecido.")

            
            elif campo == "0":
                print("Operação cancelada.")
                ativo = False
                break

    #linhas abaixo para perguntar se operação será reiniciada
    resposta = input(f"Deseja {option} um novo usuário? [S/N]: ")
    resposta = resposta.upper()

    while resposta != "S" and resposta != "N":
        resposta = input("Resposta incorreta. Digite apenas \"S\" ou \"N\": ")
        resposta = resposta.upper()

    if resposta == "N":
        ativo = False
    # fim do bloco para verificar se a reinicia a operação

    print("===============================================")

lista_baguncada = cria_lista()
separa_lista(lista_baguncada)
opcao = input("Deseja editar o arquivo corrigido? [S/N]").upper()
while opcao != "S" and opcao != "N":
    opcao = input("Opção inválida. Deseja editar o arquivo corrigido? [S/N]").upper()

if opcao == "S":
    operations()

print("Encerrando o programa.")
sys.exit()