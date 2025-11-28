#Вариант 1.
#Задание 1.

num = int(input())

if num < 0:
    result = -num
elif num == 0:

    result = 1
else:

    result = num

print(result)

#Задание 2.
s = input("Введите строку: ")
has_punctuation = False
for char in s:
    if char == '.' or char == ',':
        has_punctuation = True
        break
print(has_punctuation)

#Задание 3. (Условные Операторы)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a % 3 == 0 and b % 3 == 0:
    print(True)
elif a % 3 == 0 or b % 3 == 0:
    print("Одно число делится на 3")
else:
    print(False)

#Вариант 2.
#Задание 1.
Num = int(input(“Введите число: “)) 
if num > 100: 
    Print(“*”) 
elif num > 0: 
    Print(“*” * num) 
 
#Задание 2. 
Str1 = input(“Первая строка: “) 
Str2 = input(“Вторая строка: “) 
if str1 == str2: 
    Print(True) 
else: 
    Print(False) 
 
#Задание 3.
R = int(input(“R: “)) 
G = int(input(“G: “)) 
B = int(input(“B: “)) 
If r == 0 and g == 0 and b == 0: 
    Print(“Чёрный цвет”) 
elif r == 255 and g == 255 and b == 255: 
    Print(“Белый цвет”) 
elif r == 255 and g == 0 and b == 0: 
    Print(“Красный цвет”) 
elif r == 0 and g == 255 and b == 0: 
    Print(“Зелёный цвет”) 
elif r == 0 and g == 0 and b == 255: 
    Print(“Синий цвет”) 
else: 
    Print(“Нет цвета”) 
 
#Вариант 3.
#Задание 1.
Num = int(input(“Введите число: “)) 
if num > 0: 
    Print(num-1, num, num+1) 
else: 
    Num = 1 
    Print(num-1, num, num+1) 
 
#Задание 2.
Filename = input(“Имя файла: “) 
if filename.endswith(‘.doc’): 
    Print(“Word file”) 
elif filename.endswith(‘.py’): 
    Print(“Python file”) 
elif filename.endswith(‘.txt’): 
    Print(“Text file”) 
else: 
    Print(“Неизвестный формат”) 
 
#Задание 3. 
A = float(input(“Сторона a: “)) 
B = float(input(“Сторона b: “)) 
C = float(input(“Сторона c: “)) 
if a == b == c: 
    Print(“Равносторонний”) 
elif a == b or a == c or b == c: 
    Print(“Равнобедренный”) 
else: 
    Print(“Разносторонний”) 
 
#Вариант 4.
#Задание 1.
Text = ‘important information in one line’ 
Letter = input(“Введите букву: “) 
if letter in text: 
    Print(True) 
else: 
    Print(False) 
 
# Задание 2 
Side1 = float(input(“Первая сторона: “)) 
Side2 = float(input(“Вторая сторона: “)) 
if side1 == side2: 
    Print(“Квадрат, площадь:”, side1 * side2) 
else: 
    Print(“Прямоугольник, площадь:”, side1 * side2) 
 
# Задание 3 
Answer = input(“Как твои дела? “) 
if answer in [“хорошо”, “нормально”, “отлично”]: 
    Print(“😊”) 
elif answer in [“плохо”, “не хорошо”, “…”]: 
    Print(“😢”) 
else: 
    Print(“😐”) 
 
#Вариант 5.
#Задание 1.
Num1 = int(input(“Первое число: “)) 
Num2 = int(input(“Второе число: “)) 
if num1 > num2: 
    Print(num1 ** num2) 
elif num2 > num1: 
    Print(num2 ** num1) 
else: 
    Print(num1 + num2) 
 
#Задание 2.
New_message = “Hello! How are you?” 
User_answer = input(“Введите ответ: “) 
if new_message[0] == user_answer[0]: 
    Print(True) 
else: 
    Print(False) 
 
#Задание 3.
Segment1 = float(input(“Длина первого отрезка: “))
Segment2 = float(input(“Длина второго отрезка: “)) 
if segment1 > segment2: 
    Print(“Первый отрезок длиннее на”, segment1 – segment2) 
elif segment2 > segment1: 
    Print(“Второй отрезок длиннее на”, segment2 – segment1) 
else: 
    Print(“Отрезки равны”) 
 
#Вариант 6.
#Задание 1.
Text = input(“Введите строку: “) 
if text[0] == text[-1]: 
    Print(True) 
else: 
    Print(False) 
 
#Задание 2.
Num = int(input(“Введите число: “)) 
if num % 2 == 0: 
    Print(num ** 2) 
elif num % 3 == 0: 
    Print(num ** 3) 
else: 
    Print(num * 100) 
 
#Задание 3.
Num1 = int(input(“Первое число: “)) 
Num2 = int(input(“Второе число: “)) 
if num1 < 0 and num2 < 0: 
    Print(False) 
elif num1 < 0: 
    Num1 += 1000 
    Print(num1, num2) 
elif num2 < 0: 
    Num2 += 1000 
    Print(num1, num2) 
else: 
    Print(True) 
 
#Вариант 7.
#Задание 1.
Text = input(“Введите строку: “) 
if text[-1] in [‘я’, ‘и’, ‘е’, ‘ю’]: 
    Print(True) 
else: 
    Print(False) 
 
#Задание 2.
A = float(input(“Сторона a: “)) 
B = float(input(“Сторона b: “)) 
C = float(input(“Сторона c: “)) 
if a > 0 and b > 0 and c > 0: 
    if a + b > c and a + c > b and b + c > a: 
        Print(True) 
    else: 
        Print(False) 
else: 
    Print(False) 
 
#Задание 3.
Num = int(input(“Введите число: “)) 
Last_digit = num % 10 
if last_digit == 0: 
    Print(num ** 10) 
elif last_digit == 1: 
    Print(num % 3) 
elif last_digit == 2: 
    Print(num // 2) 
else: 
    Print(num ** 2) 
 
#Вариант 8.
#Задание 1.
Password = input(“Введите пароль: “) 
if len(password) < 8 or password == “qwerty123”: 
    Print(False) 
else: 
    Print(True) 
 
#Задание 2.
Pc_number = 777 
Num1 = int(input(“Первое число: “)) 
Num2 = int(input(“Второе число: “)) 
if (num1 < pc_number < num2) or (num2 < pc_number < num1): 
    Print(True) 
else: 
    Print(False) 
 
#Задание 3.
Lamp_1 = 0 
Lamp_2 = 0 
Choice = input(“Какую лампочку зажечь? “) 
if choice == “1”: 
    Lamp_1 = 1 
    Print(“Лампочка 1 горит”) 
elif choice == “2”: 
    Lamp_2 = 1 
    Print(“Лампочка 2 горит”) 
else: 
    Print(“Обе лампочки не горят”) 
 
#Вариант 9.
#Задание 1.
Switch_1 = False 
Switch_2 = False 
Answer = input(“Включить? “) 
if answer == “да”: 
    Switch_1 = True 
    Switch_2 = True 
    Print(“Всё включено”) 
    Print(“switch_1 =”, switch_1) 
    Print(“switch_2 =”, switch_2) 
else: 
    Print(“switch_1 =”, switch_1) 
    Print(“switch_2 =”, switch_2) 
 
#Задание 2.
Num = int(input(“Введите число: “)) 
If num > 0: 
    If num % 2 == 0: 
        Print(True, “even”) 
    else: 
        Print(True, “odd”) 
else: 
    Print(False) 
 
#Задание 3.
Text = input(“Введите строку: “) 
if text.startswith(‘/’): 
    Print(“command”) 
else: 
    Print(“It’s string”) 
 
#Вариант 10.
#Задание 1.
Text = input(“Введите строку: “) 
Length = len(text) 
if length == 0: 
    Print(None) 
elif length <= 5: 
    Print(“short”) 
elif 6 <= length <= 10: 
    Print(“normal”) 
else: 
    Print(“long”) 
 
#Задание 2.
Num = int(input(“Введите число: “)) 
if num < 0: 
    Num = 1000000 
    Print(num) 
elif num == 0: 
    Num = 2 
    Print(num ** 2) 
else: 
    Print(num ** 3) 
 
#Задание 3.
Number_1 = 10 
Number_2 = 100 
User_num = int(input(“Введите число: “)) 
if number_1 < user_num < number_2: 
    Print(True) 
else: 
    Print(False) 
 
#Вариант 11.
#Задание 1.
Prog_num = 0 
Num1 = int(input(“Первое число: “)) 
Num2 = int(input(“Второе число: “)) 
if num1 < 0 and num2 < 0: 
    Prog_num = num1 + num2 
    Print(prog_num) 
elif num1 > 0 and num2 > 0: 
    Prog_num = num1 – num2 
    Print(prog_num) 
else: 
    Print(False)
#Задание 2.
Num = int(input(“Введите число: “)) 
if num % 2 == 1: 
    Num += 1 
    Print(num) 
else: 
    Print(True) 
 
#Задание 3.
Text = input(“Введите строку: “) 
if len(text) > 10: 
    Print(text[:5]) 
else: 
    Print(text) 
 
#Вариант 12.
#Задание 1.
Ru = ‘a6Brдеёжзийклинопрстуфхцчищbblbэюя’ 
En = ‘abcdefghijklmnopqrstuvwxyz’ 
Letter = input(“Введите букву: “) 
if letter in ru: 
    Print(“rus”) 
elif letter in en: 
    Print(“eng”) 
else: 
    Print(None) 
 
#Задание 2.
Pc_num = 10 
User_num = int(input(“Введите число: “)) 
if user_num == pc_num or user_num == pc_num-1 or user_num == pc_num+1: 
    Print(True) 
else: 
    Print(False) 
 
#Задание 3.
Print(‘(221 – 13) * 2’) 
Correct_answer = (221 – 13) * 2 
User_answer = int(input(“Ваш ответ: “)) 
if user_answer == correct_answer: 
    Print(True) 
elif user_answer > correct_answer: 
    Print(“>”) 
else: 
    Print(“<”)
