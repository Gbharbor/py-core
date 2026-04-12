def calc_escolha():
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
        if numb == 0:
            print("Error: division by zero")
            return
        result = numa / numb
    else:
        print("Error: invalid operator")
        return

    print(f"{numa} {ope} {numb} = {result}")