#Etapa - Calculo do IMC--
def calculo_imc(imc):
    imc = peso /(altura*2)

#Etapa - Teste do IMC
def teste_imc(valor_imc):
    if valor_imc >= 25:
        return "ACIMA DO PESO!"
    else:
        return "NORMAL"

#Etapa 3
def resultado_imc(mensagem):
    if mensagem == "ACIMA DO PESO":
        return "Atenção, Procure um Médico!"
