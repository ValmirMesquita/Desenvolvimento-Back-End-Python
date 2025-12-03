# Sintaxe
#lambda argumentos: expressão

soma = lambda a, b: a + b
print(soma(3, 52)) # Saída: 55

# Exemplo com múltiplos argumentos
def multiplicador(n): # Função externa
    def multiplica(x): # Closure
        return x * n
    return multiplica # Retorna a função interna

triplo = multiplicador(5) # Cria uma função que multiplica por 5
valor = triplo(10)
print(valor) # Saída: 50