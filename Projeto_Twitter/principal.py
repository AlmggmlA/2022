from display_sistema import tela_sistema as tela
from sistema_busca_twitter import projeto_busca_twitter as proj_twt

tela.tela_inicial()
opcao_entrada = int(input('Informe uma opção: '))

if __name__ == '__main__':
    rodar_programa = True
    flag_opcao_entrada = []
    while rodar_programa:
        if opcao_entrada != 5 and opcao_entrada != 4:
            flag_opcao_entrada.append(opcao_entrada)

        if opcao_entrada == 1:
            tela.tela_buscar_data()
            proj_twt.busca_twt_data()

            print(" ")
            tela.tela_inicial()
            opcao_entrada = int(input('Informe uma opção: '))
        elif opcao_entrada == 2:
            tela.tela_buscar_termo()
            proj_twt.busca_twt_termo()
            print(" ")
            tela.tela_inicial()
            opcao_entrada = int(input('Informe uma opção: '))
        elif opcao_entrada == 3:
            tela.tela_buscar_assunto()
            proj_twt.busca_twt_assunto()
            print(" ")
            tela.tela_inicial()
            opcao_entrada = int(input('Informe uma opção: '))
        elif opcao_entrada == 4:
            tela.tela_salvar()
            proj_twt.salvar(flag_opcao_entrada)
            print(" ")
            tela.tela_inicial()
            opcao_entrada = int(input('Informe uma opção: '))
        elif opcao_entrada == 5:
            tela.tela_sair()
            print("Programa finalizado...")
            rodar_programa = False