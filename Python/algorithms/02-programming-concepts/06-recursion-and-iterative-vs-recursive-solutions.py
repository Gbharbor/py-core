def factorial_iterative(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_iterative(n):
    a = 0
    b = 1

    if n == 0:
        return a
    if n == 1:
        return b

    for _ in range(2, n + 1):
        temp = a + b
        a = b
        b = temp

    return b


def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def recursive_sum(n1, n2):
    if n2 == 0:
        return n1
    return recursive_sum(n1 + 1, n2 - 1)


def recursive_multiplication(n1, n2):
    if n2 == 0:
        return 0
    return n1 + recursive_multiplication(n1, n2 - 1)


print("Choose an option:")
print("1 - Factorial (iterative)")
print("2 - Factorial (recursive)")
print("3 - Fibonacci (iterative)")
print("4 - Fibonacci (recursive)")
print("5 - Recursive sum")
print("6 - Recursive multiplication")

option = int(input("Option: "))

match option:
    case 1:
        number = int(input("Enter a number to calculate factorial: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial_iterative(number)
            print(f"Factorial of {number}: {result}")

    case 2:
        number = int(input("Enter a number to calculate factorial: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        elif number > 15:
            print("Number too large. Recursive version may be impractical for this exercise.")
        else:
            result = factorial_recursive(number)
            print(f"Factorial of {number}: {result}")

    case 3:
        number = int(input("Enter a number to calculate Fibonacci: "))
        if number < 0:
            print("Only non-negative numbers are allowed.")
        else:
            result = fibonacci_iterative(number)
            print(f"Fibonacci of {number}: {result}")

    case 4:
        number = int(input("Enter a number to calculate Fibonacci: "))
        if number < 0:
            print("Fibonacci is not defined for negative numbers.")
        elif number > 20:
            print("Number too large. Recursive Fibonacci may have poor performance.")
        else:
            result = fibonacci_recursive(number)
            print(f"Fibonacci of {number}: {result}")

    case 5:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))

        if n2 < 0:
            print("This recursive sum version expects the second number to be non-negative.")
        else:
            result = recursive_sum(n1, n2)
            print(f"Sum of {n1} and {n2}: {result}")

    case 6:
        n1 = int(input("Enter the first natural number: "))
        n2 = int(input("Enter the second natural number: "))

        if n1 >= 0 and n2 >= 0:
            result = recursive_multiplication(n1, n2)
            print(f"Product of {n1} and {n2}: {result}")
        else:
            print("Only natural numbers are allowed.")

    case _:
        print("Invalid option.")