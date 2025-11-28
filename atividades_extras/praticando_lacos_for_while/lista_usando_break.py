#Lista de nomes com laço for
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

# Itera sobre a lista de nomes e imprime uma saudação para cada nome
for nome in nomes:
    # Usa o break para sair do loop quando encontrar "Carlos"
    if nome == "Carlos":
        print(f"Nome encontado {nome}! saindo do loop.")
        break 
    print(f"Olá, {nome}!")
    
#