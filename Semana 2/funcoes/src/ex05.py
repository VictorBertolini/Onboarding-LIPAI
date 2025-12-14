"""
Exercício 5 - Funções

Implemente uma calculadora de Índice de Massa Corporal (IMC)
usando as diretrizes da OMS. O programa deve:
○ Solicitar ao usuário seu peso (kg) e altura (m).
○ Calcular o IMC:
■ IMC = peso / (altura * altura)
■ IMC Classificação
■ -----------------------------------
■ < 18,5 Baixo peso
■ 18,5 a 24,9 Peso normal
■ 25,0 a 29,9 Excesso de peso
■ 30,0 a 34,9 Obesidade de Classe 1
■ 35,0 a 39,9 Obesidade de Classe 2
■ >= 40,00 Obesidade de Classe 3
○ Apresentar também a situação atual do indivíduo em relação ao peso
normal: "normal" , "perder peso" , "ganhar peso"
"""

def calcular_imc(individuo: dict):
    return individuo["peso"] / (individuo["altura"]**2)

def obter_classificacao(imc: float):
    if imc >= 40:
        return "Obesidade de Classe 3"
    elif imc >= 35:
        return "Obesidade de Classe 2"
    elif imc >= 30:
        return "Obesidade de Classe 1"
    elif imc >= 25:
        return "Excesso de peso"
    elif imc >= 18.5:
        return "Peso Normal"
    else:
        return "Baixo peso"
    
def situacao_individuo(imc: float):
    if imc < 18.5:
        return "Ganhar Peso"
    elif 18.5 <= imc <= 25:
        return "Normal"
    else:
        return "Perder Peso"

individuo = {
    'altura':1.79,
    'peso':78.5
}

imc = calcular_imc(individuo)
classificacao = obter_classificacao(imc)
situacao = situacao_individuo(imc)

print(f"O IMC do indivíduo é de: {imc:.2f}, sua classificação é: {classificacao} e sua situação é para {situacao}")

