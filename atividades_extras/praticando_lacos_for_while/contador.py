contador = 0

print("DEFINIÇÕES DE CONTAGEM COM (WHILE)")
while contador < 10:
    
    print(f"Contador atual: {contador}")

    #Á uma grande difereça entre os dois
    #Este faz a contagem ate o numero determinado no caso 10
    contador += 1
    #Este conta infinitamente o valor 1 depois do zero
    #contador =+ 1

print("===============================================")
print("DEFINIÇÕES DE CONTAGEM COM (FOR)")
for contador in range(0,50):
    
    contador += 1
    print(f"Valor atual: {contador}")
    
print("===============================================")
print("DEFINIÇÕES DE CONTAGEM COM (FOR DE 2 EM 2 ")
for contador in range(0,100,2):
    #Ultilizar esta linha se caso queira contar comente os numeros impares
    #contador += 1 
    print(f"Valor atual: {contador}")