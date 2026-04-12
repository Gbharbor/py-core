from dataclasses import dataclass


@dataclass
class Student:
    id: int
    name: str
    age: int


@dataclass
class Person:
    name: str
    age: int
    sex: str


def count_adults_in_file():
    adults = 0

    try:
        with open("data/pessoas.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, age = line.split(",")
                age = int(age.strip())

                if age >= 18:
                    adults += 1

        print("Number of adults:", adults)

    except FileNotFoundError:
        print("File 'data/pessoas.txt' not found.")


def register_person_in_agenda():
    name = input("Enter person's name: ")
    age = int(input("Enter person's age: "))
    height = float(input("Enter person's height (e.g. 1.75): "))
    sex = input("Enter person's sex (M/F): ")
    donor = input("Is the person an organ donor? (Y/N): ")

    with open("data/AGENDA.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}, {age}, {height:.2f}, {sex}, {donor}\n")

    print("Person data successfully saved in data/AGENDA.txt.")


def process_students_file():
    students = []

    try:
        with open("data/estudantes.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                student_id, name, age = line.split(",")
                student = Student(
                    id=int(student_id.strip()),
                    name=name.strip(),
                    age=int(age.strip())
                )
                students.append(student)

    except FileNotFoundError:
        print("File 'data/estudantes.txt' not found.")
        return

    print("Number of students read:", len(students))

    if students:
        oldest_student = students[0]

        for student in students:
            if student.age > oldest_student.age:
                oldest_student = student

        print(f"Oldest student: {oldest_student.name} ({oldest_student.age} years old)")
    else:
        print("No students were read from the file.")


def save_people_records():
    with open("data/dados.txt", "a", encoding="utf-8") as file:
        while True:
            name = input("Enter person's name: ")
            sex = input("Enter person's sex (M/F): ")
            age = int(input("Enter person's age: "))

            person = Person(name=name, age=age, sex=sex)
            file.write(f"{person.name}, {person.sex}, {person.age}\n")

            while True:
                choice = input("Add another record? (Y/N): ").strip().upper()
                if choice in ("Y", "N"):
                    break
                print("Invalid option. Enter Y or N.")

            if choice == "N":
                break

    print("Records saved successfully in 'data/dados.txt'.")


print("Choose an option:")
print("1 - Count adults in file")
print("2 - Register person in agenda")
print("3 - Process students file")
print("4 - Save people records")

option = int(input("Option: "))

match option:
    case 1:
        count_adults_in_file()
    case 2:
        register_person_in_agenda()
    case 3:
        process_students_file()
    case 4:
        save_people_records()
    case _:
        print("Invalid option.")