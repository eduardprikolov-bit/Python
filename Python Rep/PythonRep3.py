#Задание 1.
#Количество минут от пользователя
minutes = int(input(">>> "))

#Часы и минуты
hours = minutes // 60
remaining_minutes = minutes % 60

#Результат
print(">>>", hours)
print(">>>", remaining_minutes)

#Задание 2.
a = int(input())  #минимальное рекомендуемое количество часов
b = int(input())  #максимальное рекомендуемое количество часов
h = int(input())  #сколько часов спит Аня

#Проверка режима сна
if h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
else:
    print("Это нормально")

#Задание 3.
#Ввод длин сторон треугольника
a = float(input())
b = float(input())
c = float(input())

#Вычисление полупериметра
p = (a + b + c) / 2

#Вычисление площади по формуле Герона
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

#Вывод результата
print(area)

#Задание 4.
#Ввод типа фигуры
figure_type = input()

if figure_type == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    #Формула Герона для треугольника
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(area)
    
elif figure_type == "прямоугольник":
    a = float(input())
    b = float(input())
    #Площадь прямоугольника
    area = a * b
    print(area)
    
elif figure_type == "круг":
    r = float(input())
    #Площадь круга (п = 3.14)
    area = 3.14 * r ** 2
    print(area)

#Задание 5.
-
#Задание 6.
# Ввод номера билета
ticket = input(">>> ")

# Проверяем, что номер состоит из 6 цифр
if len(ticket) == 6:
    # Преобразуем каждую цифру в число и складываем
    first_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    second_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    
    # Сравниваем суммы
    if first_sum == second_sum:
        print(">>> Счастливый")
    else:
        print(">>> Обычный")
else:
    print(">>> Неверный номер билета")
































By lonely
