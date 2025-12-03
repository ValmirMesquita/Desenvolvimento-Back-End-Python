def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(bom_dia("Valmir")) # Saída: Bom dia, Valmir!
print(boa_noite("Ana")) # Saída: Boa noite, Ana!
print(bom_dia("Leticia")) # Saída: Bom dia, Leticia!
print(boa_noite("Duda")) # Saída: Boa noite, Duda!