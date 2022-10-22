import pandas as pd

# Lendo o arquivo CSV e carregando para "data"
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# Imprimindo Original no Console
# print(data)

# Descartando colunas com valor nulo para evitar erros
data.dropna(inplace = True)
print(data["Name"].iterrows())
for indice in range(len(data)):
    new02 = data["Name"].str.split(" ", n = indice, expand = True)
    if new02["Name"] != "None":
        new02 = new02["Name"]
print(new02)

# Nova Data com Split das coluna "Name" separado por espaços
new = data["Name"].str.split(" ", n = 1, expand = True)
cor = data["Coluna_cores"].str.split(" ", n = 1, expand = True) # n = quantidade de cores contando a partir de 0.
data["cor01"] = cor[0]
data["cor02"] = cor[1]
data["cor03"] = cor[2]
data.drop(columns=["Name"], inplace=True) # remove a coluna antiga
# Criando a Nova Coluna "First Name" com o new[0]
for indice in range(len(new)):
    data["First Name"] = new[0]
print(data["First Name"])
#
# # Criando a Nova Coluna "Last Name" com o new[1]
# data["Last Name"]= new[1]
#
# # Retirando a antiga coluna "Name"
# data.drop(columns =["Name"], inplace = True)
#
# # Imprimindo Alteração no Console
# print(data)