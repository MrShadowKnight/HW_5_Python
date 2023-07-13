# TASK №1

number1 = int(input("Введіть початкове число: "))           # Вводимо початкове і кінцеве число діапазону
number2 = int(input("Введіть кінцеіе число: "))
list_diapasonu = []
if number1 > number2:
    print("Початкове число не може бути більше кінцевого!") # Робимо перевірку
else:
    for num in range(number1, number2 + 1):
        if num > 1:
            for i in range(2, num):                         # Якщо число з діапазону ділиться на інше окрім себе і 1 зупиняємо цикл в іншому випадку вводимо в список
                if (num % i) == 0:
                    break
                else:
                    list_diapasonu.append(num)
print("Прасті числа: ", list_diapasonu)                     # Виводимо список

# TASK №2

for j in range(1, 11):                                      # Вводимо два масиви від 1 до 10
    for i in range(1, 11):
        production = j * i                                  # Виконуємо дію множення і виводимо на екран результат і дію         
        print(f"{j} * {i} = ", production)
    print("---------------")                                # Відділяємо від іншої таблиці

# TASK №3

start = int(input("Введіть початкове число: "))             # Вибираємо діапазон таблиці множення
end = int(input("Введіть кінцеве число: "))

if start > end:
    print("Початкове число не може бути більше кінцевого!") # Робимо перевірку
else:
    print(f"Таблиця множення від {start} до {end}: ")
    for t in range(start, end + 1):                         # Вводимо масив від start до end
        for k in range(1, 11):                              # Вводимо масив від 1 до 10
            product = t * k                                 # Виконуємо дію множення і виводимо на екран результат і дію 
            print(f"{t} * {k} = ", product)
        print("---------------")                            # Відділяємо від іншої таблиці