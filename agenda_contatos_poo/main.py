from CorrigeCSV import CorrigeCSV
from Agenda import Agenda
import os

'''
Programa referente ao mini-projeto 2 do curso Data Science Degree da Let's Code - 2021.
Interface para corrigir colunas de arquivo csv desorganizado com 'nome', 'telefone' e 'email' de fornecedores.
A partir do arquivo organizado, criar uma agenda de contatos de no máximo 75 contatos, contendo ID, nome, sobrenome, telefones e emails.
Opções de navegação e operações tais como remoção, adição, filtros e grupos.
'''

def close():
    print("Encerrando programa...")
    print("===============================================================")
    #sys.exit(0)
    os._exit(1)

try:
    print("=====================================================")
    lista_arquivos = CorrigeCSV.check_files()
    if 'agenda.csv' not in lista_arquivos:
        if 'contatos_corrigido.csv' not in lista_arquivos:
            print("Não foi encontrado arquivo de csv corrigido no diretório atual.")
            print("Corrigindo CSV...")
            try:
                CorrigeCSV.run()
            except:
                print("Houve um erro ao tentar corrigir o CSV original.")
            print("CSV corrigido.")
                
        print("Criando agenda...")
        try:
            Agenda.criar_agenda()
        except:
            print("Houve um erro ao criar a agenda a partir do CSV corrigido.")
            close()
        
    print("Abrindo agenda...")
    try:
        ag = Agenda()
    except:
        print("Houve um erro durante a execução da agenda.")

    close()

except:
    print("Houve um erro.")