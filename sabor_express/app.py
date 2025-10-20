import os # Biblioteca para interagir com o sistema operacional

# Função para exibir o cabeçalho do aplicativo
def exibir_cabecalho():
    
    print("""
        
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
\n""")


 # Função para finalizar o aplicativo
def finalizar_app():
    os.system('cls')
    print("Finalizando o aplicativo...")

def exibir_opcao():   
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print('3. Ativar restaurante')
    print("4. Sair\n")
    print("=====================================")


def escolher_opcao():          
    opcao_escolhida = int(input("Escolha uma opção: "))
    
    print(f"A opçao escolhida foi: {opcao_escolhida}")
    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        print("Opção inválida")
 
# Função principal do aplicativo   
def main():
    # Aqui você pode adicionar mais funcionalidades conforme necessário
    exibir_cabecalho()
    exibir_opcao()
    escolher_opcao()
   
        
# Executa a função principal se o script for executado diretamente   
if __name__== "__main__":
    main()
