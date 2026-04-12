# repita_ate_100
n = 0

while True:
    print(n)
    n += 1
    if n > 100:
        break


# soma_inteiro_positivo_ate_100 (pares)
n = 2
soma = 0

while True:
    soma += n
    n += 2
    if n > 100:
        break

print("Sum of even numbers up to 100:", soma)


# repetir_um_caractere
n = 1

while True:
    print(f"{n} HELLO!")
    n += 1
    if n > 10:
        break


# tabuada
valor = int(input("Multiplication table of: "))
contador = 1

while True:
    print(f"{valor} x {contador} = {valor * contador}")
    contador += 1
    if contador > 10:
        break