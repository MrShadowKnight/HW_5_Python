# TASK №1

number1 = int(input("Введіть початкове число: "))           # Вводимо початкове і кінцеве число діапазону
number2 = int(input("Введіть кінцеіе число: "))
list_diapasonu = []

for num in range(number1, number2 + 1):
    if num > 1:
        for i in range(2, num):                             # Якщо число з діапазону ділиться на інше окрім себе і 1 зупиняємо цикл в іншому випадку вводимо в список
            if (num % i) == 0:
                break
        else:
            list_diapasonu.append(num)
print("Прасті числа: ", list_diapasonu)                     # Виводимо список

# TASK №2

for j in range(1, 11):                                      # Вводимо два масиви від 1 до 10
    for i in range(1, 11):
        Production = j * i                                  # Виконуємо дію множення і виводимо на екран результат і дію         
        print(f"{j} * {i} = ", Production)
    print("---------------")                                # Відділяємо від іншої таблиці

# TASK №3

number3 = int(input("Введіть перше число(від 1 до 10): "))  # Вибираємо дві таблиці множення
number4 = int(input("Введіть друге число(від 1 до 10): "))

if number3 == 1:
    for i in range(1, 11):                                  # Вводимо масив від 1 до 10
        Production = number3 * i                            # Виконуємо дію множення і виводимо на екран результат і дію 
        print(f"{number3} * {i} = ", Production)
    print("---------------")                                # Відділяємо від іншої таблиці
elif number3 == 2:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 3:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 4:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 5:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 6:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 7:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 8:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 9:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
elif number3 == 10:
    for i in range(1, 11):
        Production = number3 * i
        print(f"{number3} * {i} = ", Production)
    print("---------------")
else:
    print("Таблиця не розрахована на інші варіанти!")
if number4 == 1:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 2:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 3:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 4:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 5:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 6:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 7:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 8:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 9:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
elif number4 == 10:
    for i in range(1, 11):
        Production = number4 * i
        print(f"{number4} * {i} = ", Production)
    print("---------------")
else:
    print("Таблиця не розрахована на інші варіанти!")