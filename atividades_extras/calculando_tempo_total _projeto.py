# Calculando o tempo total de projeto
dias_A = int(input("Informe os dias para a atividade A: "))
dias_B = int(input("Informe os dias para a atividade B: "))
dias_C = int(input("Informe os dias para a atividade C: "))

erro = "Os dias não pode ser negativos"

if dias_A >= 0 and dias_B >= 0 and dias_C >= 0:
    tempo_total = dias_A + dias_B + dias_C
    print(f"O tempo total do projeto é de: {tempo_total}")
else:
    print(f"Erro: {erro}")