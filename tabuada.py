print("Tabuada Digital")
numero = int(input("Qual Número Você Quer Saber a Tabuada? "))
print(f"---Tabuada Do {numero}---")
for i in range(1, 11):
    resultado = numero * i 
    print(f"{numero} X {i} = {resultado}")
