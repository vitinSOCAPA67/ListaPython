#- Simulador de Investimento--
deposito_mensal = 50
total = 0
for mes in range(1, 7):
    total = total + deposito_mensal
    print(f"Mês {mes}:Saldo total = R$ {total}")
print(f"Ao Final de 6 Meses, Você Terá: R${total}")