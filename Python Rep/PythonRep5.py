#Задание 1.
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']


m_copy = m.copy()

names_of_shapes = ['круг', 'квадрат', 'треугольник', 'овал']


for item in m_copy:

    if not isinstance(item, str) or item not in names_of_shapes:

        m.remove(item)

print(m)

#Задание 2.
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

for i in range(4, 0, -1):
    del abc[i]

print(abc)

#Задание 3.
numbers = [1, 4]
numbers.insert(1, 3)
numbers.insert(1, 2)
print(numbers)

#Задание 4.
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]

positive_numbers = []
for num in mass:
    if num >= 0:
        positive_numbers.append(num)

ascending = sorted(positive_numbers)

descending = sorted(positive_numbers, reverse=True)

print(ascending)
print(descending)

#Задание 5.
# Создаем три списка
negative_numbers = []
positive_numbers = []
zero_list = []

# Получаем количество чисел от пользователя
try:
    n = int(input("Введите количество чисел: "))
    
    for i in range(n):
        try:
            num = float(input(f"Введите число {i+1}: "))
            
            if num < 0:
                negative_numbers.append(num)
            elif num > 0:
                positive_numbers.append(num)
            else:
                zero_list.append(num)
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")

    if negative_numbers:
        negative_sum = sum(negative_numbers)
        print(f"\n1. Сумма отрицательных чисел: {negative_sum}")
        print(f"   Отрицательные числа: {negative_numbers}")
    else:
        print("\n1. Отрицательных чисел нет")

    if positive_numbers:
        positive_avg = sum(positive_numbers) / len(positive_numbers)
        print(f"\n2. Среднее арифметическое положительных чисел: {positive_avg:.2f}")
        print(f"   Положительные числа: {positive_numbers}")
    else:
        print("\n2. Положительных чисел нет")
    
    if zero_list:

        zero_list_stars = ['*' for _ in zero_list]
        
        print(f"\n3. Список с нулями:")
        print(f"   Количество элементов: {len(zero_list)}")
        print(f"   Элементы (нули заменены на '*'): {zero_list_stars}")
        print(f"   Исходные нули: {zero_list}")
    else:
        print("\n3. Нулей нет")

    print("\n" + "="*50)
    print("Итоговая информация:")
    print(f"Всего введено чисел: {n}")
    print(f"Отрицательных чисел: {len(negative_numbers)}")
    print(f"Положительных чисел: {len(positive_numbers)}")
    print(f"Нулей: {len(zero_list)}")

except ValueError:
    print("Ошибка! Пожалуйста, введите целое число для количества чисел.")














By lonely
