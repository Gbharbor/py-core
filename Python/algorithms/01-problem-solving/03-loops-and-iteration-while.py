# repeticao_0_a_100
n = 0
while n < 100:
    n += 1
    print(n)


# soma_pares
n = 2
soma = 0
while n <= 100:
    soma += n
    n += 2

print("Sum of even numbers:", soma)


# repetir_hello
n = 1
while n <= 10:
    print("HELLO")
    n += 1


# tabela_multiplicacao
valor = int(input("Multiply: "))
contador = 1

while contador <= 10:
    print(f"{valor} x {contador} = {valor * contador}")
    contador += 1


# soma_positivos
contador = 1
soma = 0

while contador <= 10:
    n = int(input(f"Enter number {contador}: "))
    if n > 0:
        soma += n
    contador += 1

print("Sum of positives:", soma)


# fatorial
numero = int(input("Enter number: "))
fat = 1
contador = numero

while contador > 1:
    fat *= contador
    contador -= 1

print("Factorial:", fat)