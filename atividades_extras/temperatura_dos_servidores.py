#Temperatura dos servidores
for contrle_temp in range(10):
  
    temperatura = 25
    temperatura_atual= float(input("Digite a temperatura atual:"))

    if temperatura_atual > temperatura:
        print("Temperatura acima do limite permitido")
        print("Assionar o refrigerador \n")
    elif temperatura_atual < temperatura:
        print("Temperatura normal, estabilizada.\n")
    elif temperatura_atual == temperatura:
        print("Temperatura no limite maximo.\n")
    else:
        print("Nenhuma das alternativas.\n")