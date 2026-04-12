def reajuste_salarial():
    sal = float(input("Salary: "))

    if sal < 500:
        nsal = sal + (sal * 15 / 100)
    elif 500 <= sal <= 1000:
        nsal = sal + (sal * 10 / 100)
    else:
        nsal = sal + (sal * 5 / 100)

    print(f"New salary: {nsal:.2f}")


def pagamento_anual():
    id_number = int(input("ID number: "))
    final = id_number % 10

    if final == 0:
        print("PAY JAN")
    elif final == 1:
        print("PAY FEB")
    else:
        print("PAY MAR")


def maior_entre_tres():
    a = int(input("First: "))
    b = int(input("Second: "))
    c = int(input("Third: "))

    if a == b == c:
        print("Equal")
    elif a >= b and a >= c:
        print(f"Bigger: {a}")
    elif b >= a and b >= c:
        print(f"Bigger: {b}")
    else:
        print(f"Bigger: {c}")


def calculator_1():
    numa = float(input("Number: "))
    ope = input("Operator: ")
    numb = float(input("Number: "))

    if ope == "+":
        result = numa + numb
    elif ope == "-":
        result = numa - numb
    elif ope == "*":
        result = numa * numb
    elif ope == "/":
        result = numa / numb
    else:
        print("Invalid operator.")
        return

    print(f"{numa} {ope} {numb} = {result}")