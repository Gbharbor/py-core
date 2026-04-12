"""
AULA: Fundamentos + Input + Condicionais
"""

print("=== PRIMEIRO PROGRAMA ===")
print("hello world")


print("\n=== VARIAVEIS E TIPOS ===")

nome = "Harbor"
idade = 90
preco = 19.90

print(nome)
print(idade)
print(preco)


print("\n=== REATRIBUICAO ===")

nome = "Harbor"
nome = 50

print(nome)
print(type(nome))
print(type(preco))


print("\n=== OPERACOES ARITMETICAS ===")

resultado = 10 / 2
print(resultado)
print(type(resultado))

numero1 = 10
numero2 = 5

soma = numero1 + numero2
print(soma)


print("\n=== CASTING ===")

numero1 = 10
numero2 = int("5")

soma = numero1 + numero2
print(soma)

nome_numero = str(10)
print(type(nome_numero))


print("\n=== INPUT E STRINGS ===")

user_name = input("Qual seu nome? ").title()
user_age = int(input("Qual sua idade? "))

print("Nome: " + user_name)
print("Idade: " + str(user_age))
print("O seu nome e " + user_name + " e voce tem " + str(user_age) + " anos.")

numero = 10 + 5

print(
    f"O seu nome e {user_name} "
    f"({len(user_name)} caracteres) "
    f"e voce tem {user_age} anos. "
    f"Eu gosto do numero {numero}. "
    f"Posso calcular 10+2 aqui mesmo: {10 + 2}. "
    f"Daqui 10 anos voce tera: {user_age + 10}."
)

texto = "algo"

print(texto.upper())
print(texto.lower())
print(texto.title())
print(f"O nome tem {len(user_name)} caracteres.")


print("\n=== IF / ELIF / ELSE ===")

idade_alistamento = int(input("Qual sua idade? "))

if idade_alistamento == 17:
    print("Hora de alistar")
elif idade_alistamento < 17:
    print("Cedo demais...")
else:
    print("Tarde demais...")


print("\n=== OPERADOR AND ===")

idade_user = int(input("Qual sua idade? "))

if 12 <= idade_user < 18:
    print("É um adolescente.")
elif idade_user >= 18:
    print("É um adulto.")
else:
    print("É uma criança.")


print("\n=== OPERADOR OR ===")

idade_user2 = int(input("Qual sua idade (alistamento)? "))

if idade_user2 == 17 or 21 <= idade_user2 < 25:
    print("Pode se alistar.")
elif idade_user2 >= 22:
    print("Não pode se alistar.")
