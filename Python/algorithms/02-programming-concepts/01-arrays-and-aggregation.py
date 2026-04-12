# maioridade
maior = 0
menor = 0

for i in range(1, 21):
    idade = int(input(f"Enter age of person {i}: "))

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print("Adults:", maior)
print("Minors:", menor)


# maior_e_menor_nota
notas = []

for i in range(1, 11):
    nota = float(input(f"Enter grade {i}: "))
    notas.append(nota)

maior = notas[0]
menor = notas[0]

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

print("Highest grade:", maior)
print("Lowest grade:", menor)