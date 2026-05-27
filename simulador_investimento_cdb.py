#Investimento CDB--
print("Bem-Vindo(a) ao Centro de Investimento CDB")
print("Taxa de Juros Atual do CDB: 1,24%")
aporte = float(input("Quanto Você Vai Depositar Por Mês? "))
juros = 0.0124
meses = int(input("Por Quantos Meses Você Vai Investir? "))
total = 0
for mes in range (1, meses +1):
    total = total + aporte
    total = total + (total * juros)
    print(f"Mês {mes}: Saldo Total = R${total:.2f}")
print(f"Ao Final de {meses} meses, Você Terá o Valor de R$:{total:.2f}")
#Victor Hugo Cardoso 2EDS--