# Controlando orçamentos mensais

limite_Etabelecido = float(input(f"Digite o valor estabelecido mensalmente para controle:"))
print(f"Valor estabelecido: { limite_Etabelecido:.2f} ")

total_despesa = float(input("Digite o total de despesa:"))

saldo_disponivel = limite_Etabelecido - total_despesa

if total_despesa < limite_Etabelecido:
    print(f"Parabens! voçe não ultapassou seu limete atual R$: {limite_Etabelecido:.2f} 💰💲 💦 ")
    print(f"Saldo disponivel acumulado: R$ {saldo_disponivel} 💰💰💰💰💰💰 ")
else:
    print(f"Atenção! Voce ultrapassou seu limite orçamentario R$: {total_despesa:.2f} 🔥💥 " )
    


