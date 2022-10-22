from colorama import Fore, Style

def tela_inicial():
    print(
    f"""
            Boas vindas ao nosso sistema!
        {'####' * 9}
        |{' ' * 3}1 - Buscar tweets por data{' ' * 5}|
        |{' ' * 3}2 - Buscar tweets por termo{' ' * 4}|
        |{' ' * 3}3 - Buscar tweets por assunto{' ' * 2}|
        |{' ' * 3}4 - Salvar resultado da busca{' ' * 2}|
        |{' ' * 3}5 - Sair{' ' * 23}|
        {"####" * 9}
    """)

def tela_buscar_data():
    print(
    f"""
        
        {"####" * 9}            
        |{' ' * 1}► {Fore.LIGHTCYAN_EX}1 - Buscar tweets por data{Style.RESET_ALL} ◄{' ' * 3}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}2 - Buscar tweets por termo{Style.RESET_ALL}{' ' * 4}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}3 - Buscar tweets por assunto{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}4 - Salvar resultado da busca{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}5 - Sair{Style.RESET_ALL}{' ' * 23}|
        {"####" * 9}
    """)

def tela_buscar_termo():
    print(
    f"""
        
        {"####" * 9}
        |{' ' * 3}{Fore.LIGHTBLACK_EX}1 - Buscar tweets por data{Style.RESET_ALL}{' ' * 5}|
        |{' ' * 1}► {Fore.LIGHTCYAN_EX}2 - Buscar tweets por termo{Style.RESET_ALL} ◄{' ' * 2}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}3 - Buscar tweets por assunto{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}4 - Salvar resultado da busca{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}5 - Sair{Style.RESET_ALL}{' ' * 23}|
        {"####" * 9}
    """)

def tela_buscar_assunto():
    print(
    f"""
        {"####" * 9}    
        |{' ' * 3}{Fore.LIGHTBLACK_EX}1 - Buscar tweets por data{Style.RESET_ALL}{' ' * 5}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}2 - Buscar tweets por termo{Style.RESET_ALL}{' ' * 4}|
        |{' ' * 1}► {Fore.LIGHTCYAN_EX}3 - Buscar tweets por assunto{Style.RESET_ALL} ◄{''}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}4 - Salvar resultado da busca{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}5 - Sair{Style.RESET_ALL}{' ' * 23}|
        {"####" * 9}
    """)

def tela_salvar():
    print(
    f"""
        
        {"####" * 9}        
        |{' ' * 3}{Fore.LIGHTBLACK_EX}1 - Buscar tweets por data{Style.RESET_ALL}{' ' * 5}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}2 - Buscar tweets por termo{Style.RESET_ALL}{' ' * 4}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}3 - Buscar tweets por assunto{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 1}► {Fore.LIGHTCYAN_EX}4 - Salvar resultado da busca{Style.RESET_ALL} ◄{''}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}5 - Sair{Style.RESET_ALL}{' ' * 23}|
        {"####" * 9}
    """)

def tela_sair():
    print(
    f"""
        
        {"####" * 9}        
        |{' ' * 3}{Fore.LIGHTBLACK_EX}1 - Buscar tweets por data{Style.RESET_ALL}{' ' * 5}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}2 - Buscar tweets por termo{Style.RESET_ALL}{' ' * 4}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}3 - Buscar tweets por assunto{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 3}{Fore.LIGHTBLACK_EX}4 - Salvar resultado da busca{Style.RESET_ALL}{' ' * 2}|
        |{' ' * 1}► {Fore.LIGHTCYAN_EX}5 - Sair{Style.RESET_ALL} ◄{' ' * 21}|
        {"####" * 9}
    """)