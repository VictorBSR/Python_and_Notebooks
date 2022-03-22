# MINI PROJETO 2 DO SQUAD CINZA-B - DSD 2021 #
# Integrantes: Victor, Thomas e Rodrigo

import os, csv, sys
from os.path import isfile, join


class CorrigeCSV:
    '''
    Classe para identificar arquivos csv no diretório atual e propor padronização de campos de lista de contatos:
    :string nome, email, telefone
    Salva cópia do arquivo corrigido, preservando o original, e retorna mensagem de sucesso.
    '''
    @staticmethod
    def run():
        fileDir = os.getcwd()
        #print('============ Bem vindo ao programa corretor de arquivos ============\n')
        try:
            lista_arquivos = CorrigeCSV.check_files()
        except:
            print('Houve um erro ao ler arquivos csv no diretório atual. Favor verificar se os arquivos .csv e o código em execução estão na mesma pasta.')
        else:
            if len(lista_arquivos) == 1:
                print(f'Existe {len(lista_arquivos)} arquivo na pasta {fileDir}. Selecione abaixo a opção que deseja importar:\n')
            else:
                print(f'Existem {len(lista_arquivos)} arquivos na pasta {fileDir}. Selecione abaixo a opção que deseja importar:\n')

            for a in lista_arquivos:
                print(f'Opção {lista_arquivos.index(a)+1}: {a}')

            opcao = int(input('Importar opção: '))
            while opcao < 1 or opcao > len(lista_arquivos):
                opcao = int(input('Inválido, favor selecionar novamente: '))
            selecao = lista_arquivos[int(opcao)-1]

            lista_baguncada = CorrigeCSV.cria_lista(selecao)
            CorrigeCSV.separa_lista(lista_baguncada)
            #print("Encerrando o programa.")
            #print("=======================================================================")
            #sys.exit()

    @staticmethod
    def check_files():
        fileDir = os.getcwd()
        fileExt = r".csv"
        lista_arquivos = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]
        if len(lista_arquivos) == 0:
            raise FileNotFoundError
        return lista_arquivos

    @staticmethod
    def cria_lista(selecao):
        arquivo = open(selecao, 'r+', encoding="utf-8")
        tabela_contatos = csv.reader(arquivo, delimiter=";", lineterminator="\n")
        lista_contatos = []
        for linha in tabela_contatos: #loop usado para transformar os dados em uma lista com os dados já presentes
            lista_contatos.append(linha)
        arquivo.close()
        return lista_contatos # exibe a lista

    @staticmethod
    def separa_lista(lista_baguncada):
        nome = []
        tel = []
        email = []

        for contatos in range(len(lista_baguncada)):
            for dados in range(3):
                CorrigeCSV.verifica_nome(nome, lista_baguncada[contatos][dados])
                CorrigeCSV.verifica_tel(tel, lista_baguncada[contatos][dados])
                CorrigeCSV.verifica_email(email, lista_baguncada[contatos][dados])
        
        tamanho_lista = len(lista_baguncada)
        CorrigeCSV.reconstroi_lista(nome, tel, email, tamanho_lista)

    @staticmethod
    def verifica_nome(nome, dado):
        if dado.isalpha():
            nome.append(dado)

    @staticmethod
    def verifica_tel(tel, dado):
        if dado.isnumeric():
            tel.append(dado)

    @staticmethod
    def verifica_email(email, dado):
        if '@'in dado:
            email.append(dado)

    @staticmethod
    def reconstroi_lista(nome, tel, email, tamanho_lista):
        lista_reconst = []
        lista_reconst_parc = []

        for contatos in range(tamanho_lista):
            lista_reconst_parc.append(nome[contatos])
            lista_reconst_parc.append(tel[contatos])
            lista_reconst_parc.append(email[contatos])
            lista_reconst.insert(contatos, lista_reconst_parc)
            lista_reconst_parc = []

        CorrigeCSV.salva_lista_em_csv(lista_reconst,'contatos_corrigido.csv')
        print("A correção foi realizada com sucesso e a lista foi salva no arquivo 'contatos_corrigido.csv'")

    @staticmethod
    def salva_lista_em_csv(lista, nome_arquivo):
        '''
        Função salva uma lista em um arquivo .csv onde cada linha é o primeiro nível da lista e 
        os elementos de segundo nível da lista são separados entre si por ponto e vírgula ';'.   
        '''
        arquivo = open(nome_arquivo, 'w+', encoding='utf-8')
        csv.writer(arquivo, delimiter=';', lineterminator='\n').writerows(lista)
        arquivo.close()

#CorrigeCSV.run()