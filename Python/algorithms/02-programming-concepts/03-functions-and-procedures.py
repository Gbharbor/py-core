from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    grades: list[float] = field(default_factory=list)
    average: float = 0.0


def add_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    total = num1 + num2
    print(f"Sum: {total}")


def add_by_arguments(num1, num2):
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")


def calculate_average(a, b):
    return (a + b) / 2


def calculate_square(number):
    result = number * number
    print(f"The square of {number} is: {result}")


def register_students():
    students = []

    print("Student Registration:")

    for i in range(1, 6):
        name = input(f"Enter student name {i}: ")

        grades = []
        for j in range(1, 4):
            grade = float(input(f"Enter grade {j} for {name}: "))
            grades.append(grade)

        average = sum(grades) / len(grades)
        students.append(Student(name=name, grades=grades, average=average))

    print("\nStudent Report:")
    for student in students:
        print(f"Student: {student.name}")
        print(f"Average: {student.average:.2f}")


print("Welcome to the Multiuse System!")
print("Choose an option:")
print("1 - Add two numbers")
print("2 - Calculate the square of a number")
print("3 - Register students and calculate averages")
print("4 - Add numbers multiple times")
print("5 - Add numbers by arguments")
print("6 - Calculate arithmetic mean of two numbers")

option = int(input("Option: "))

match option:
    case 1:
        add_two_numbers()

    case 2:
        number = int(input("Enter an integer: "))
        calculate_square(number)

    case 3:
        register_students()

    case 4:
        n = int(input("How many times do you want to repeat the addition? "))
        for i in range(1, n + 1):
            print(f"Execution {i} of {n}")
            add_two_numbers()

    case 5:
        n = int(input("How many times do you want to perform the addition? "))
        for i in range(1, n + 1):
            print(f"Execution {i} of {n}")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            add_by_arguments(num1, num2)

    case 6:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        average = calculate_average(num1, num2)
        print(f"Arithmetic mean: {average}")

    case _:
        print("Invalid option!")

print("\nThanks for using the system!")