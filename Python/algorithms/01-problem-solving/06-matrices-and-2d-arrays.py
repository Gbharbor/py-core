# multiplicar_matriz
mat = []

print("Enter elements of 5x5 matrix:")

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Value [{i+1}][{j+1}]: "))
        linha.append(valor)
    mat.append(linha)

x = int(input("Multiply matrix by: "))

print(f"Matrix multiplied by {x}:")

for i in range(5):
    for j in range(5):
        print(mat[i][j] * x, end=" ")
    print()  # new line


# soma_diagonal_principal
mat = []

print("Enter elements of matrix:")

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Value [{i+1}][{j+1}]: "))
        linha.append(valor)
    mat.append(linha)

print("Matrix:")

for i in range(5):
    for j in range(5):
        print(mat[i][j], end=" ")
    print()

soma_d = 0

for i in range(5):
    soma_d += mat[i][i]

print("Main diagonal sum:", soma_d)