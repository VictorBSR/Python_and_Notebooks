# MINI PROJETO 2 DO SQUAD CINZA-B - DSD 2021 #
# Integrantes: Victor, Thomas e Rodrigo

from Contato import Contato
from prettytable import PrettyTable

class Grupo:
    
    grupos = {}   # dicionário de grupos -> chave = nome_grupo, valores = ids dos contatos que pertencem ao grupo
    
    @staticmethod
    def cria_grupo(nome_grupo):
        if nome_grupo not in Grupo.grupos:
            Grupo.grupos[nome_grupo] = []
            print(f'Grupo {nome_grupo.title()} adicionado com sucesso.')
        else:
            print('Já existe um grupo com esse nome.')
    
    @staticmethod
    def remove_grupo(nome_grupo):
        if nome_grupo in Grupo.grupos:
            del Grupo.grupos[nome_grupo]
            print(f'Grupo {nome_grupo.title()} removido com sucesso.')
        else:
            print('Não existe um grupo com esse nome.')
    
    @staticmethod
    def adiciona_contato_grupo(id_contato, nome_grupo):
        if id_contato not in Grupo.grupos[nome_grupo]:        # incluir verificação se id do contato existe
            Grupo.grupos[nome_grupo].append(id_contato)
            print(f'Contato ID {id_contato} incluído ao grupo {nome_grupo.title()} com sucesso.')
        else:
            print('Contato já faz parte desse grupo.')
    
    @staticmethod
    def remove_contato_grupo(id_contato, nome_grupo, flag_print = True):
        if id_contato in Grupo.grupos[nome_grupo]:
            Grupo.grupos[nome_grupo].remove(id_contato)
            if flag_print:
                print(f'Contato ID {id_contato} removido do grupo {nome_grupo.title()} com sucesso.')
        else:
            if flag_print:
                print(f'Não foi possível remover, pois contato não pertence ao grupo.')
    
    @staticmethod
    def mostrar_contatos_grupo(nome_grupo, lista_contatos):
        if nome_grupo in Grupo.grupos:
            print(f'Contatos do grupo {nome_grupo.title()}:')
            t = PrettyTable(["ID","Nome","Sobrenome","Telefone","E-mail"])
            #print("ID\t\tNome\t\t\tSobrenome\t\t\tTelefone\t\t\t\tE-mail\t\t\t\tGrupos") # table header          
            for ident in sorted(Grupo.grupos[nome_grupo]):
                for contato in lista_contatos:
                    if contato.id == ident:
                        t.add_row([contato.id, contato.nome.title(), contato.sobrenome.title(), contato.tel, contato.email])
            print(t)
        elif nome_grupo in Grupo.grupos and len(Grupo.grupos[nome_grupo]) == 0:
            print(f'Contatos do grupo {nome_grupo.title()}:')
            print('-----------------------------------')
            print('Grupo sem contatos') 
            print('-----------------------------------')
        else:
            print('Não existe um grupo com esse nome.')

    @staticmethod
    def lista_grupos():
        print('Lista de grupos:')
        print('-----------------------------------')
        for nome_grupo in sorted(Grupo.grupos.keys()):
            print(f'{nome_grupo.title()} - {len(Grupo.grupos[nome_grupo])} contatos')
        print('-----------------------------------')