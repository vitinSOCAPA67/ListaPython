#Simulador de Poupança--
aporte = float(input("Quanto Você Vai Depositar Por Mês? "))
juros = float(input("Qual é a Taxa de Juros Atual da Poupança? "))
meses = int(input("Por Quantos Meses Você Vai Investir? "))
juros_decimal = juros/100
total = 0
for mes in range (1, meses +1):
    total = total + aporte
    total = total + (total * juros_decimal)
    print(f"Mês {mes}: Saldo Total = R${total:.2f}")
print(f"Ao Final de {meses} meses, Você Terá o Valor de R$:{total:.2f}")