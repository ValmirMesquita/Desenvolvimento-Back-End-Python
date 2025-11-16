nome = input("Digite seu nome: ")
peso_atual = float(input("Digite seu peso em (Kg): "))
altura = float(input("Digite sua altura em (mt): "))

IMC = peso_atual /(altura * altura)
valor_IMC = IMC

print(f"Ola {nome}")
print(f"Seu peso: {peso_atual}")
print(f"Sua altura: {altura}")
print(f"Seu IMC: {valor_IMC}")
print("---------------------------------- \n")

if valor_IMC < 18.5:
    print("Abaixo do peso.")
elif 18.5  <= valor_IMC  - 24.9:
    print("Peso normal ")
elif 25.0 > valor_IMC - 29.9:
    print("Sobrepeso")
elif valor_IMC >= 30.0:
    print("Obesidade")


