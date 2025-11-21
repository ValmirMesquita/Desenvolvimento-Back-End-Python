valor_da_renda = float(input("Digite o valor da sua renda: "))
valor_parcelas = int(input("Digite o valor de parcelas: "))

limite_maximo_parcela = valor_da_renda * 0.30
limite_maximo_parcela = valor_da_renda  * 0.30

condicao1 = valor_da_renda  > 2000.00
condicao2 = valor_parcelas <= limite_maximo_parcela

if condicao1 and condicao2:
    status_emprestimo = "APROVADO"
else:
    status_emprestimo = "NEGADO"

print(f"Renda mensal informada: R$ {valor_da_renda :.2f}")
print(f"Valor da parcela desejada: R$ {valor_parcelas:.2f}")
print(f"Limite máximo da parcela (30% da renda): R$ {limite_maximo_parcela:.2f}")
print("-" * 30)
print(f"Status do empréstimo: {status_emprestimo}")