def calculate_salary_adjustment(current_salary):
    if current_salary <= 1000:
        adjustment_percentage = 0.10
    elif current_salary < 2000:
        adjustment_percentage = 0.08
    else:
        adjustment_percentage = 0.06

    return current_salary * (1 + adjustment_percentage)


def get_adjustment_percentage(current_salary):
    if current_salary <= 1000:
        return 0.10
    elif current_salary < 2000:
        return 0.08
    else:
        return 0.06


def is_adult(age):
    return age >= 18


def calculate_cube(number):
    return number ** 3


def convert_km_to_miles(km):
    return km * 0.62


print("Welcome to the Complete Functions System!")
print("Choose an option:")
print("1 - Salary Adjustment")
print("2 - Check Legal Age")
print("3 - Calculate Cube")
print("4 - Convert KM to Miles")
print("5 - Salary Adjustment with Percentage")

option = int(input("Enter your option: "))

match option:
    case 1:
        salary = float(input("Enter employee salary: "))
        corrected_salary = calculate_salary_adjustment(salary)
        print(f"Corrected salary: R$ {corrected_salary:.2f}")

    case 2:
        age = int(input("Enter age: "))
        if is_adult(age):
            print("Is an adult!")
        else:
            print("Is not an adult!")

    case 3:
        number = int(input("Enter a number to calculate the cube: "))
        cube = calculate_cube(number)
        print(f"The cube of {number} is: {cube}")

    case 4:
        km = float(input("Enter value in KM: "))
        miles = convert_km_to_miles(km)
        print(f"{km} KM is equal to {miles:.2f} miles.")

    case 5:
        salary = float(input("Enter employee salary: "))
        adjustment_percentage = get_adjustment_percentage(salary)
        corrected_salary = salary * (1 + adjustment_percentage)

        print(f"Adjustment percentage: {adjustment_percentage * 100:.2f}%")
        print(f"Corrected salary: R$ {corrected_salary:.2f}")

    case _:
        print("Invalid option.")

print("\nThanks for using the system!")