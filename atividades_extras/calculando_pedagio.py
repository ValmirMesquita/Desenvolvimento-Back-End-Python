nome_usuaria = input("Digite o nome da usuaria: ")
distancia_percorrida = float(input("Digite a distancia percorrida (em Km):"))

if distancia_percorrida <= 100:
    print(nome_usuaria)
    print("Valor do pedagio: 10.00")

elif 100 < distancia_percorrida <= 200:
    print(nome_usuaria)
    print("Valor do pedagio: 20.00")

elif distancia_percorrida > 200:
    print(nome_usuaria)
    print("Valor do pedagio: 30.00")


