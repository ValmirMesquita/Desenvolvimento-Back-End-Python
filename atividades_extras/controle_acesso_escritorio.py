usuarios_de_acesso = ["Valmir","Ana Raquel","Maria Eduarda","Maria Leticia","Poliana Santos"]
horarios_acesso = [8,9,10,11,12,13,14,15,16,17,18]

nome_usuario = input("Digite seu nome: ")
acesso_escritorio = int(input("Digite o horario de acesso: "))

if nome_usuario in usuarios_de_acesso and acesso_escritorio in horarios_acesso:  
    print("Acesso permitido 🔓 ")
else:
    print("Acesso negado 🔒 ")
