import os # Biblioteca para interagir com o sistema operacional


os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal
print("""
     
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      \n""")

print("1. Cadastrar restaurante")
print("2. Listar restaurantes")
print('3. Ativar restaurante')
print("4. Sair\n")



opcao_escolhida = int(input("Escolha uma opção: "))
print(f"A opçao escolhida foi: {opcao_escolhida}")
if opcao_escolhida == 1:
    print("Cadastrar restaurante")
elif opcao_escolhida == 2:
    print("Listar restaurantes")
elif opcao_escolhida == 3:
    print("Ativar restaurante")
elif opcao_escolhida == 4:
    print("Sair")
else:
    print("Opção inválida")
