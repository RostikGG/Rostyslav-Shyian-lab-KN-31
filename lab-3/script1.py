# change this code
number = 20           # Змінена змінна number на 20, щоб виконати перший if
second_number = 0     # Змінена змінна second_number на 0, щоб виконати останній if
first_array = [1]     # Додано елемент в first_array, щоб виконати четвертий if
second_array = [1, 2, 3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
