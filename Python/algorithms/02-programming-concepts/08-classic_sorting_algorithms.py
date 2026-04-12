def bubble_sort(numbers):
    size = len(numbers)

    for i in range(size - 1):
        for j in range(size - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def insertion_sort(numbers):
    size = len(numbers)

    for i in range(1, size):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


def selection_sort(numbers):
    size = len(numbers)

    for i in range(size - 1):
        min_index = i

        for j in range(i + 1, size):
            if numbers[j] < numbers[min_index]:
                min_index = j

        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


numbers = []

for i in range(1, 11):
    value = float(input(f"Enter number {i}: "))
    numbers.append(value)

print("\nChoose sorting method:")
print("1 - Bubble Sort")
print("2 - Insertion Sort")
print("3 - Selection Sort")

option = int(input("Option: "))

if option == 1:
    sorted_numbers = bubble_sort(numbers.copy())
    print("\nSorted with Bubble Sort:")
elif option == 2:
    sorted_numbers = insertion_sort(numbers.copy())
    print("\nSorted with Insertion Sort:")
elif option == 3:
    sorted_numbers = selection_sort(numbers.copy())
    print("\nSorted with Selection Sort:")
else:
    sorted_numbers = None
    print("\nInvalid option.")

if sorted_numbers is not None:
    for number in sorted_numbers:
        print(number)