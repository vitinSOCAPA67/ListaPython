#Etapa1- Calculo do IMC--
def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

#Etapa2- Classificar o IMC-- 
def classificar_imc(valor_imc):
    if valor_imc >= 25:
        return "ACIMA DO PESO!"
    else:
        return "PESO NORMAL!"

#Etapa3- Mensagem de Saída
def mensagem(status):
    if status == "ACIMA DO PESO!":
        return "Procure um Médico"
    else:
        return "Parábens, Continue Mantendo Uma Boa Alimentação"
#Etapa4 - Integração do Projeto
valor_peso = float(input("Digite Seu Peso Atual: "))
valor_altura = float(input("Digite Sua Altura: "))
resultado = calculo_imc(valor_peso, valor_altura)
saida = mensagem(classificar_imc)

print("=" * 50)
print(f"Seu IMC é: {resultado:.1f}")
print(f"{saida}")
print("=" * 50)
