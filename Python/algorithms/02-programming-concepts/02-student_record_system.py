from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    age: int
    gender: str
    registration: int
    course: str
    grades: list[float] = field(default_factory=list)
    average: float = 0.0
    status: str = ""


students = []

for i in range(1, 6):
    print(f"\nStudent {i}")

    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender (M/F): ")
    registration = int(input("Registration number: "))
    course = input("Course: ")

    grades = []
    for j in range(1, 4):
        grade = float(input(f"Grade {j}: "))
        grades.append(grade)

    average = sum(grades) / len(grades)

    if average >= 6 or age > 30:
        status = "APPROVED"
    else:
        status = "FAILED"

    student = Student(
        name=name,
        age=age,
        gender=gender,
        registration=registration,
        course=course,
        grades=grades,
        average=average,
        status=status
    )

    students.append(student)

print("\nStudent Report:")

for student in students:
    print(f"\nName: {student.name}")
    print(f"Age: {student.age}")
    print(f"Gender: {student.gender}")
    print(f"Registration: {student.registration}")
    print(f"Course: {student.course}")
    print(f"Grades: {student.grades}")
    print(f"Average: {student.average:.2f}")
    print(f"Status: {student.status}")

print("\nStudents over 30:")

found_over_30 = False
for student in students:
    if student.age > 30:
        print(f"{student.name} - {student.course}")
        found_over_30 = True

if not found_over_30:
    print("No students over 30.")

highest_average = students[0].average
lowest_average = students[0].average
best_student = students[0].name
worst_student = students[0].name

for student in students:
    if student.average > highest_average:
        highest_average = student.average
        best_student = student.name

    if student.average < lowest_average:
        lowest_average = student.average
        worst_student = student.name

print("\nSummary:")
print(f"Registered students: {len(students)}")
print(f"General average: {sum(student.average for student in students) / len(students):.2f}")
print(f"Highest average: {highest_average:.2f} ({best_student})")
print(f"Lowest average: {lowest_average:.2f} ({worst_student})")