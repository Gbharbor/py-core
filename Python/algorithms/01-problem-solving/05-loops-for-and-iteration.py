# contador
for n in range(0, 100):
    print(n)


# numeros_pares
for n in range(0, 101, 2):
    print(n)


# tabuada
valor = int(input("Enter value: "))

for contador in range(1, 11):
    print(f"{valor} x {contador} = {valor * contador}")


# potencia
x = 3

for z in range(0, 11):
    y = x ** z
    print(f"{x}^{z} = {y}")


# soma dos 10 primeiros termos (1/1 + 1/2 + ... + 1/10)
soma = 0.0

for i in range(1, 11):
    soma += 1 / i

print("Sum of first 10 terms:", soma)