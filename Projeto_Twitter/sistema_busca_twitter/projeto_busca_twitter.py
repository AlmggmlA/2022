import csv
import json
import os
from colorama import Fore, Style

# diretorio_BD = os.path.abspath('../base_dados/db_tweets_2022.csv')
# diretorio = "./db_tweets_2022.csv"


# FUNÇÃO PARA ABRIR ARQUIVO
def abrir_arquivo():
    #diretorio_BD = os.path.abspath('./././././base_dados/db_tweets_2022.csv')
    diretorio_BD = "base_dados/db_tweets_2022.csv"
    with open(diretorio_BD, "r", encoding="UTF-8") as arquivo:
        ler_arquivo = csv.reader(arquivo, delimiter=',', lineterminator='\n')
        lst_csv = list(ler_arquivo)
    return lst_csv

# FUNÇÃO PARA COLETAR DADOS DA PLANILHA
def info_twitter():

    lst_arquivo = abrir_arquivo()

    # dicionário de DATA
    dict_data = {}
    for indice in range(1, len(lst_arquivo)):
        dict_data.update({f'data_{indice}': lst_arquivo[indice][0][0:11][8:10] + '/' + lst_arquivo[indice][0][0:11][
                                                                                       5:7] + '/' + lst_arquivo[indice][
                                                                                                        0][0:11][0:4]})

    # dicionário de CONTEÚDO
    dict_conteudo = {}
    for indice in range(1, len(lst_arquivo)):
        dict_conteudo.update({f'conteudo_{indice}': lst_arquivo[indice][3]})

    # dicionário de ASSUNTO
    dict_assunto = {}
    for indice in range(1, len(lst_arquivo)):
        dict_assunto.update({f'assunto_{indice}': lst_arquivo[indice][4]})

    # juntando dicionários DATA,CONTEÚDO,ASSUNTO
    dict_twitter = {}
    for chave, valor in dict_data.items():
        dict_twitter.update({chave: valor})
    for chave, valor in dict_conteudo.items():
        dict_twitter.update({chave: valor})
    for chave, valor in dict_assunto.items():
        dict_twitter.update({chave: valor})

    # dicionário de TWITTER
    dict_geral_twitter = {}
    i = 1
    for _ in dict_twitter:
        if i <= len(dict_data):
            dict_geral_twitter.update({i: {'titulo': ['data', 'conteudo', 'assunto'],
                                           f'data_{i}': dict_twitter[f'data_{i}'],
                                           f'conteudo_{i}': dict_twitter[f'conteudo_{i}'],
                                           f'assunto_{i}': dict_twitter[f'assunto_{i}']}})
        i += 1
    return dict_geral_twitter

                                    #####################################################
#####################################           FUNÇÕES DE PESQUISA DO SISTEMA          ################################
                                    #####################################################

dict_geral_twitter = info_twitter()

# PESQUISA POR DATA
data_recebida = ""
tbl_resultado_data = []
def busca_twt_data():
    '''
    Realiza a pesquisa dos assuntos por data.
    :return:
    retorna a data pesquisada juntamente com o conteúdo e o assunto.
    '''
    global data_recebida
    global tbl_resultado_data

    data_recebida = input("Informe a data que deseja pesquisar (dd/mm/aaaa): ")

    # TABELA DO RESULTADO DA CONSULTA POR data
    qtd_data = 0
    tbl_resultado_data.append(dict_geral_twitter[1]['titulo'])
    qtd_data = sum([qtd_data + 1
                    for indice in range(1, len(dict_geral_twitter) + 1)
                    if data_recebida in dict_geral_twitter[indice][f'data_{indice}']])

    [
        tbl_resultado_data.append([dict_geral_twitter[indice][f'data_{indice}'],
                                   dict_geral_twitter[indice][f'conteudo_{indice}'],
                                   dict_geral_twitter[indice][f'assunto_{indice}']])
                                   for indice in range(1, len(dict_geral_twitter) + 1)
                                   if data_recebida in dict_geral_twitter[indice][f'data_{indice}']
    ]
    # Chama a função que apresenta o resultada da busca na tela do usuário.
    apresentar_resultado_data(tbl_resultado_data, qtd_data, data_recebida)

# DICIONÁRIO DO RESULTADO DA CONSULTA POR data
def dct_busca_twt_data():
    dict_resultado_data = {}
    lst_data_busca = []
    lst_conteudo = []
    lst_assunto = []
    for indice in range(1, len(dict_geral_twitter) + 1):
        if data_recebida in dict_geral_twitter[indice][f'data_{indice}']:
            lst_data_busca.append(dict_geral_twitter[indice][f'data_{indice}'])
            lst_conteudo.append(dict_geral_twitter[indice][f'conteudo_{indice}'])
            lst_assunto.append(dict_geral_twitter[indice][f'assunto_{indice}'])
        dict_resultado_data.update({'data': lst_data_busca, 'conteudo': lst_conteudo, 'assunto': lst_assunto})
    return dict_resultado_data

# PESQUISA POR TERMO
termo_recebido = ''
tbl_resultado_termo = []
def busca_twt_termo():
    '''
    Realiza a pesquisa dos assuntos por um termo qualquer informado pelo usuário.
    :return:
    retorna a data, o conteúdo e o assunto referentes ao termo pesquisado.
    '''
    global termo_recebido
    global tbl_resultado_termo

    termo_recebido = input("Informe uma palavra que deseja pesquisar: ")

    # TABELA DO RESULTADA DA CONSULTA POR termo
    tbl_resultado_termo.append(dict_geral_twitter[1]['titulo'])
    qtd_termo = 0
    qtd_termo = sum([qtd_termo + 1
                     for indice in range(1, len(dict_geral_twitter) + 1)
                     if termo_recebido in dict_geral_twitter[indice][f'conteudo_{indice}'] or
                     termo_recebido in dict_geral_twitter[indice][f'assunto_{indice}']])

    [
        tbl_resultado_termo.append([dict_geral_twitter[indice][f'data_{indice}'],
                                    dict_geral_twitter[indice][f'conteudo_{indice}'],
                                    dict_geral_twitter[indice][f'assunto_{indice}']])
                                    for indice in range(1, len(dict_geral_twitter) + 1)
                                    if termo_recebido in dict_geral_twitter[indice][f'conteudo_{indice}' or
                                       termo_recebido in dict_geral_twitter[indice][f'assunto_{indice}']]
    ]
    # Chama a função que apresenta o resultada da busca na tela do usuário.
    apresentar_resultado_termo(tbl_resultado_termo,qtd_termo,termo_recebido)

# DICIONÁRIO DO RESULTADO DA CONSULTA POR termo
def dct_busca_twt_termo():
    dict_resultado_termo = {}
    lst_termo_busca = []
    lst_conteudo = []
    lst_assunto = []
    for indice in range(1, len(dict_geral_twitter) + 1):
        if termo_recebido in dict_geral_twitter[indice][f'conteudo_{indice}'] or termo_recebido in dict_geral_twitter[indice][f'assunto_{indice}']:
            lst_termo_busca.append(dict_geral_twitter[indice][f'data_{indice}'])
            lst_conteudo.append(dict_geral_twitter[indice][f'conteudo_{indice}'])
            lst_assunto.append(dict_geral_twitter[indice][f'assunto_{indice}'])
        dict_resultado_termo.update({'data': lst_termo_busca, 'conteudo': lst_conteudo, 'assunto': lst_assunto})
    return dict_resultado_termo


# PESQUISA POR ASSUNTO
assunto_recebido = ''
tbl_resultado_assunto = []
def busca_twt_assunto():
    '''
    Realiza a pesquisa do conteúdo por assunto.
    :return:
    retorna a data,o conteúdo e o assunto pesquisado.
    '''
    global assunto_recebido
    global tbl_resultado_assunto

    assunto_recebido = input("Informe uma palavra que deseja pesquisar o assunto: ")

    # TABELA DO RESULTADA DA CONSULTA POR termo
    tbl_resultado_assunto.append(dict_geral_twitter[1]['titulo'])
    qtd_assunto = 0
    qtd_assunto = sum([qtd_assunto + 1
                       for indice in range(1, len(dict_geral_twitter) + 1)
                       if assunto_recebido in dict_geral_twitter[indice][f'assunto_{indice}']])

    [
        tbl_resultado_assunto.append([dict_geral_twitter[indice][f'data_{indice}'],
                                      dict_geral_twitter[indice][f'conteudo_{indice}'],
                                      dict_geral_twitter[indice][f'assunto_{indice}']])
                                      for indice in range(1, len(dict_geral_twitter) + 1)
                                      if assunto_recebido in dict_geral_twitter[indice][f'assunto_{indice}']
    ]
    apresentar_resultado_assunto(tbl_resultado_assunto,qtd_assunto,assunto_recebido)

# DICIONÁRIO DO RESULTADO DA CONSULTA POR assunto
def dct_busca_twt_assunto():
    dict_resultado_assunto = {}
    lst_assunto_busca = []
    lst_conteudo = []
    lst_assunto = []
    for indice in range(1, len(dict_geral_twitter) + 1):
        if assunto_recebido in dict_geral_twitter[indice][f'assunto_{indice}']:
            lst_assunto_busca.append(dict_geral_twitter[indice][f'data_{indice}'])
            lst_conteudo.append(dict_geral_twitter[indice][f'conteudo_{indice}'])
            lst_assunto.append(dict_geral_twitter[indice][f'assunto_{indice}'])
        dict_resultado_assunto.update({'data': lst_assunto_busca, 'conteudo': lst_conteudo, 'assunto': lst_assunto})
    return dict_resultado_assunto


                                    #####################################################

#####################################             FUNÇÃO PARA SALVAR ARQUIVO            ################################
                                    #####################################################

# FUNÇÃO PARA SALVAR
def salvar(flag_opcao_entrada):

    # chama a função flag_opcao_entrada para identificar as buscas a serem salvas
    for opcao in flag_opcao_entrada:
        # SALVAR pesquisa por data
        if opcao == 1:
            dict_twitter = dct_busca_twt_data()

            # FORMATO JSON
            # dicionário para JSON
            arquivo_json_data = json.dumps(dict_twitter)
            # escrevendo JSON em arquivo
            with open("arquivos_salvos/twt_resultado_data.json", "w", encoding='UTF-8') as resultado_data_json:
                json.dump(arquivo_json_data, resultado_data_json)

            # FORMATO CSV
            tbl_resultado_data
            with open('arquivos_salvos/resultado_data.csv', 'w', encoding='UTF-8') as arquivo_csv:
                escrever_csv = csv.writer(arquivo_csv,
                                          delimiter='|',
                                          lineterminator='\n')
                escrever_csv.writerows(tbl_resultado_data)

        # SALVAR pesquisa por termo
        if opcao == 2:
            dict_twitter = dct_busca_twt_termo()

            # FORMATO JSON
            # dicionário para JSON
            arquivo_json_termo = json.dumps(dict_twitter)
            # escrevendo JSON em arquivo
            with open("arquivos_salvos/twt_resultado_termo.json", "w",encoding='UTF-8') as resultado_termo_json:
                json.dump(arquivo_json_termo, resultado_termo_json)

            # FORMATO CSV
            tbl_resultado_termo
            with open('arquivos_salvos/resultado_termo.csv', 'w', encoding='UTF-8') as arquivo_csv:
                escrever_csv = csv.writer(arquivo_csv,
                                          delimiter='|',
                                          lineterminator='\n')
                escrever_csv.writerows(tbl_resultado_termo)

        # SALVAR pesquisa por assunto
        if opcao == 3:
            dict_twitter = dct_busca_twt_assunto()

            # FORMATO JSON
            # dicionário para JSON
            arquivo_json_assunto = json.dumps(dict_twitter)
            # escrevendo JSON em arquivo
            with open("arquivos_salvos/twt_resultado_assunto.json", "w", encoding='UTF-8') as resultado_assunto_json:
                json.dump(arquivo_json_assunto, resultado_assunto_json)

            # FORMATO CSV
            tbl_resultado_assunto
            with open('arquivos_salvos/resultado_assunto.csv', 'w', encoding='UTF-8') as arquivo_csv:
                escrever_csv = csv.writer(arquivo_csv,
                                          delimiter='|',
                                          lineterminator='\n')
                escrever_csv.writerows(tbl_resultado_assunto)

    print("Arquivo salvo com sucesso!")


                              ############################################################
###############################   FUNÇÕES PARA EXIBIR RESULTADO DA PESQUISA DO SISTEMA   ###############################
                              ############################################################

# FUNÇÕES PARA EXIBIR RESULTADO NA TELA DO USUÁRIO

# Imprime na tela o resultado por DATA
def apresentar_resultado_data(tabela_data,qtd_data,data_recebida):
    print(" ")
    for indice in range(0,len(tabela_data)):
        if indice == 0:
            print("  "*2+tabela_data[0][0] + "  |   " + tabela_data[0][1] + "    |   " + tabela_data[0][2])
        else:
            print("|"+tabela_data[indice][0]+"|"+tabela_data[indice][1]+"|"+tabela_data[indice][2])
    print(f"\nA sua pesquisa retornou: {Fore.LIGHTGREEN_EX}{qtd_data}{Style.RESET_ALL} resultado(s) para a data {Fore.LIGHTGREEN_EX}{data_recebida}{Style.RESET_ALL}")

# Imprime na tela o resultado por TERMO
def apresentar_resultado_termo(tabela_termo,qtd_termo,termo_recebido):
    print(" ")
    for indice in range(0,len(tabela_termo)):
        if indice == 0:
            print("  "*2+tabela_termo[0][0] + "  |   " + tabela_termo[0][1] + "    |   " + tabela_termo[0][2])
        else:
            print("|"+tabela_termo[indice][0]+"|"+tabela_termo[indice][1]+"|"+tabela_termo[indice][2])
    print(f"\nA sua pesquisa retornou: {Fore.LIGHTGREEN_EX}{qtd_termo}{Style.RESET_ALL} resultado(s) para o termo {Fore.LIGHTGREEN_EX}{termo_recebido}{Style.RESET_ALL}.")

# Imprime na tela o resultado por ASSUNTO
def apresentar_resultado_assunto(tabela_assunto,qtd_assunto,assunto_recebido):
    print(" ")
    for indice in range(0,len(tabela_assunto)):
        if indice == 0:
            print("  "*2+tabela_assunto[0][0] + "  |   " + tabela_assunto[0][1] + "    |   " + tabela_assunto[0][2])
        else:
            print("|"+tabela_assunto[indice][0]+"|"+tabela_assunto[indice][1]+"|"+tabela_assunto[indice][2])
    print(f"\nA sua pesquisa retornou: {Fore.LIGHTGREEN_EX}{qtd_assunto}{Style.RESET_ALL} resultado(s) para o assunto {Fore.LIGHTGREEN_EX}{assunto_recebido}{Style.RESET_ALL}.")