"""
Calculo de IMC
"""


def calcular_imc(peso, altura):
    return peso / (altura**2)


def classificar_imc(imc):
    if imc < 19.1:
        return "Abaixo do peso"
    elif imc <= 25.8:
        return "Peso normal"
    elif imc <= 27.3:
        return "Pouco acima do peso"
    elif imc <= 32.3:
        return "Acima do peso"
    else:
        return "Obesidade"


print("=== CALCULO DE IMC ===")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)
categoria = classificar_imc(imc)

print(f"Seu IMC e: {imc:.2f}")
print(f"Classificacao: {categoria}")
