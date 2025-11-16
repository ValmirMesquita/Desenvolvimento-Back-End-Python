# Condicionais if, else e elif

#nome = "Start"
#nome = "Alura"
# nome = "Latam"

# if nome == "Alura":
#     print("Boas vindas a Alura")  
# elif nome == "Latam":
#     print("Bem vindo a latam")
# else:
#     print("Nome desconhecido")

# Operadores de comparação 
# -----------------------------------------------
#  >  Maior               x >  10
#  <  Menor               x <  10  
#  == Igual               x == 10
#  != Diferente           x != 10
#  >= Maior ou igual      x >= 10
#  <= Menor ou igual      x >= 10

# idade = int(input("Informe sua idade: "))
# tem_documento = input("Tem documento? (Sim/Não)")

# if idade >= 18 and tem_documento == "sim":
#     print("Entrada permitida")
# else:
#     print("Entrada negada")

feriado = input("Hoje e  feriado? (Sim/Não)")
folga   = input("Voçe tem folga hoje? (Sim/Não)")

if feriado == "sim" or folga == "sim":
    print("Voçê pode descansar hoje")
else:
    print("Dia normal de trabalho")