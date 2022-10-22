from tkinter import filedialog,Tk
Tk().withdraw()

diretorio = filedialog.askopenfilename().replace("'\'","'/'")

with open(diretorio,"r",encoding="utf-8") as arquivo_txt:
    texto = arquivo_txt.read().lower().split()

def conta_palavras(frase):

    lista_vogais = ["a","e","i","o","u"]
    lista_palavra = [palavra for palavra in texto
                             for vogal in lista_vogais
                             if palavra.startswith(vogal)]

    dicionario = {}
    for palavra in lista_palavra:
        if palavra not in dicionario:
            dicionario.update({palavra: 0})
        dicionario[palavra] += 1

    return dicionario
print(conta_palavras(texto))