from display_sistema import tela_sistema as tela
from sistema_busca_twitter import projeto_busca_twitter as proj_twt

def verificarDigito(opcao_entrada):
    while not opcao_entrada.isdigit():
        print("Informe um valor numérico entre 1 e 5")
        opcao_entrada = input('Informe uma opção: ')
    else:
        return opcao_entrada

if __name__ == '__main__':
    rodar_programa = True
    flag_opcao_entrada = []

    tela.tela_inicial()
    opcao_entrada = input('Informe uma opção: ')
    entrada_usuario = verificarDigito(opcao_entrada)

    while rodar_programa:

        if entrada_usuario != '5' and entrada_usuario != '4':
            if int(entrada_usuario) not in flag_opcao_entrada:
                flag_opcao_entrada.append(int(entrada_usuario))

        if entrada_usuario == '1':
            tela.tela_buscar_data()
            proj_twt.busca_twt_data()
            print(" ")
            tela.tela_inicial()
            opcao_entrada = input('Informe uma opção: ')
            entrada_usuario = verificarDigito(opcao_entrada)
        elif entrada_usuario == '2':
            tela.tela_buscar_termo()
            proj_twt.busca_twt_termo()
            print(" ")
            tela.tela_inicial()
            opcao_entrada = input('Informe uma opção: ')
            entrada_usuario = verificarDigito(opcao_entrada)
        elif entrada_usuario == '3':
            tela.tela_buscar_assunto()
            proj_twt.busca_twt_assunto()
            print(" ")
            tela.tela_inicial()
            opcao_entrada = input('Informe uma opção: ')
            entrada_usuario = verificarDigito(opcao_entrada)
        elif entrada_usuario == '4':
            tela.tela_salvar()
            proj_twt.salvar(flag_opcao_entrada)
            print(" ")
            tela.tela_inicial()
            opcao_entrada = input('Informe uma opção: ')
            entrada_usuario = verificarDigito(opcao_entrada)
        elif entrada_usuario == '5':
            tela.tela_sair()
            print("Programa finalizado...")
            rodar_programa = False

