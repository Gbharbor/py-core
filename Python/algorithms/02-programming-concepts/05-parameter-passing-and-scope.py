num1 = 0
num2 = 0
imc = 0.0
soma = 0


def swap_by_value(x, y):
    temp = x
    x = y
    y = temp
    print(f"Inside swap_by_value: x = {x}, y = {y}")


def swap_by_return(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def swap_global():
    global num1, num2

    temp = num1
    num1 = num2
    num2 = temp


def apply_discount(discount, total):
    total = total - discount
    print(f"Local total with discount: {total}")


def calculate_imc(weight, height):
    return weight / (height * height)


def sum_between_numbers(a, b):
    total = 0
    for i in range(a + 1, b):
        total += i
    return total


# swap_by_value
num1 = int(input("Enter the first value (num1): "))
num2 = int(input("Enter the second value (num2): "))

print(f"Before swap_by_value: num1 = {num1}, num2 = {num2}")
swap_by_value(num1, num2)
print(f"After swap_by_value: num1 = {num1}, num2 = {num2}")


# swap_by_return
a = int(input("\nEnter the first value (a): "))
b = int(input("Enter the second value (b): "))

print(f"Before swap_by_return: a = {a}, b = {b}")
a, b = swap_by_return(a, b)
print(f"After swap_by_return: a = {a}, b = {b}")


# swap_global
num1 = int(input("\nEnter the first global value (num1): "))
num2 = int(input("Enter the second global value (num2): "))

print(f"Before global swap: num1 = {num1}, num2 = {num2}")
swap_global()
print(f"After global swap: num1 = {num1}, num2 = {num2}")


# local scope example
total = 1000
print(f"\nOriginal total: {total}")
apply_discount(50, total)
print(f"Final total unchanged outside function: {total}")


# calculate_imc
weight = float(input("\nEnter your weight: "))
height = float(input("Enter your height: "))

imc = calculate_imc(weight, height)
print(f"Your BMI is: {imc:.2f}")


# sum_between_numbers
first_number = int(input("\nEnter the first positive number: "))
second_number = int(input("Enter the second positive number: "))

if first_number > 0 and second_number > 0 and first_number < second_number:
    soma = sum_between_numbers(first_number, second_number)
    print(f"The sum of numbers between {first_number} and {second_number} is: {soma}")
else:
    print("Only positive values are allowed, and the first number must be smaller than the second.")