diretorio = "./convidados.txt"

# with open(diretorio,"r",encoding="utf-8") as arquivo_txt:
#     convidado = arquivo_txt.read().lower().split()
# print(convidado)
#
# def nome_convidado(convidado):
#     rodar_programa = True
#     while rodar_programa:
#         nome = input('Nome do convidado: ').strip().lower()
#
#         if nome in convidado:
#             print(f'{nome} - Está na lista')
#         else:
#             print(f'{nome} - Não está na lista')
#         finalizar = int(input('deseja finalizar o programa?\n digite 1 - sim ou 2 - não\n'))
#         if finalizar == 1:
#             print("programa finalizado!")
#             rodar_programa = False

with open(diretorio,"r",encoding="utf-8") as arquivo:
    convidado = arquivo.readlines()
print(convidado)

def nome_convidado(convidado):
    rodar_programa = True
    while rodar_programa:
        nome = input('Nome do convidado: ').strip().lower()

        for linha in convidado:
            print(linha)
            if nome in linha:
                print(f'{nome} - Está na lista')

        print(f'{nome} - Não está na lista')
        finalizar = int(input('deseja finalizar o programa?\n digite 1 - sim ou 2 - não\n'))
        if finalizar == 1:
            print("programa finalizado!")
            rodar_programa = False

nome_convidado(convidado)
