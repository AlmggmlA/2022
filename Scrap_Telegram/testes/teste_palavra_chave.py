import csv
import re

diretorio = '../palavras_chaves.txt'

def palavra_chave():
    with open(diretorio,'r', encoding='UTF-8') as palavra_chave:
        lista_filtro = ''
        ler_arquivo = csv.reader(palavra_chave,lineterminator='\n')
        for palavras in ler_arquivo:
            lista_filtro += ''.join(palavras).strip() + '|'
    #print(lista_filtro[:-1])
    return lista_filtro[:-1]

# EXTRAIR LINK
#
import requests
from bs4 import BeautifulSoup

link = 'https://www.udemy.com/course/ayurveda-for-womens-wellness/'
def filtrar_palavras_link(link):
    try:
        pagina = requests.get(link)
        conteudo = BeautifulSoup(pagina.content,'html.parser')
        htmlTexto = conteudo.find_all('span')

        lst_conteudo = []
        for indice in range(len(htmlTexto)):
            if htmlTexto[indice].text != '':
                lst_conteudo.append(htmlTexto[indice].text)

        conjunto_palavras = ''
        for palavra in lst_conteudo:
            conjunto_palavras = conjunto_palavras + ''.join(palavra) + ' '

        palavras_filtradas = re.sub(r'[^a-zA-Z]', ' ', conjunto_palavras)

        lst_palavras = palavras_filtradas.split()

        palavras_chaves = re.compile(f'({palavra_chave()})+')
        print(palavras_chaves)

        for conteudo in lst_palavras:
            if palavras_chaves.match(fr'^{conteudo.lower()}'):
                print(conteudo)
                #return palavras


    except requests.exceptions.HTTPError as e:
        print('Erro HTTPError: ',e)
    except requests.exceptions.InvalidSchema as e:
        print('Erro InvalidSchema: ',e)
    except requests.exceptions.RequestException as e:
        print('{} é uma URL inválida!'.format(link))
    except Exception as e:
        print('Erro encontrado:',e)

# filtrar_palavras_link(link)


def filtrar_palavras(conteudo):
    #lst_conteudo = []
    lst_palavra = palavra_chave()
    lst_palavra = lst_palavra.split('|')

    for msg in conteudo:
        mensagem_telegram = msg

    msg_concatena = ''
    for msg in mensagem_telegram:
        msg_concatena = msg_concatena + ''.join(msg) + ''

    #print(msg_concatena)
    #print(type(msg_concatena))

    teste = msg_concatena.strip()
    teste02 = teste.split('||')
    #print(teste02)

    lst_palavra_filter = []
    for palavra in teste02:
        palavra_filter = re.sub(r'[^a-zA-Z]', ' ', palavra)
        lst_palavra_filter.append(palavra_filter.strip())
    print(lst_palavra_filter)




with open('msg_concatena_02.txt','r',encoding='utf-8') as arquivo_mensagem:
    conteudo = arquivo_mensagem.readlines()
    filtrar_palavras(conteudo)