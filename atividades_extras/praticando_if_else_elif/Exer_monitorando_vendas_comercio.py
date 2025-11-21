quant_macas_vendidas = int(input("Digite a quantidades de macãs vendidas: "))
quant_bananas_vendidas = int(input("Digite a quantidades de bananas vendidas: "))

if quant_macas_vendidas > quant_bananas_vendidas:
    print(f"Numero de Maçãs vendidas {quant_macas_vendidas} é maior que o numero de Bananas {quant_bananas_vendidas}")

elif quant_bananas_vendidas > quant_macas_vendidas:
    print(f"Numero de Bananas vendidas {quant_bananas_vendidas} é maior que o numero de Maçãs {quant_macas_vendidas}")
else:
    print(f"A quantidade de Maçãs {quant_macas_vendidas} e a quantidade de Bananas {quant_bananas_vendidas} são iguais")
