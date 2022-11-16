# string = "CREATE TABLE IF NOT EXISTS mensagens_telegram (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"+\
#                                                             "links TEXT NOT NULL,"+\
#                                                             "mensagem_enviada INTEGER DEFAULT 0,"+\
#                                                             "data_entrada TIMESTAMP DEFAULT DATETIME('now','localtime')"')'
#
# print(string)
# print(f'"{string}"')
#
# "CREATE TABLE links_telegram (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, links text NOT NULL, mensagem_enviada INTEGER DEFAULT 0)"
#
# string02 = 'CREATE TABLE '"mensagens_telegram"' (\
# 	'"id"'	INTEGER NOT NULL,\
# 	'"links"'	TEXT NOT NULL,\
# 	'"mensagem_enviada"'	INTEGER DEFAULT 0,\
# 	'"data_entrada"' TIMESTAMP DEFAULT '"DATETIME('now','localtime'),\
# 	PRIMARY KEY("'id AUTOINCREMENT)\
# )'
#
# print(string02)
import csv
import pandas as pd
diretorio = 'teste.xlsx'

arquivo = pd.read_excel(diretorio)
df_arquivo = pd.DataFrame(arquivo)


# for valor in arquivo:
#     print(valor)

for valor in arquivo['link_encontrado']:
    print(valor)
