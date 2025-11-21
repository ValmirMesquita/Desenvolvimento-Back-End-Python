nome_aluno = input("Nome do aluno: ")
media_1 = int(input("Digite a primeira media:"))
media_2 = int(input("Digite a segunda media:"))
media_3 = int(input("Digite a terceira media:"))
media_4 = int(input("Digite a quarta media:"))

resultado_final = (media_1 + media_2 + media_3 + media_4 )/4

if resultado_final >= 7:
    print(f"Aluno {nome_aluno}, Aprovado!")
elif resultado_final == 6:
    print(f"Aluno {nome_aluno} de recuuperação")
elif resultado_final < 6:
    print(f"Aluno {nome_aluno} reprovado")
