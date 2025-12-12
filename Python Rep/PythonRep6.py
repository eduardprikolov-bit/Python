#Задание 1.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matrix:")
for row in matrix:
    print(row)

print("нечётные числа matrix")
odd_numbers = []
even_count = 0

for row in matrix:
    for num in row:
        if num % 2 != 0:
            odd_numbers.append(str(num))
        else:
            even_count += 1

print(" ".join(odd_numbers))
print(f"кол-во чётных: {even_count}")

#Задание 2.
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

answer_matrix = [[0 for _ in range(len(matrix_1[0]))] for _ in range(len(matrix_1))]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]

print(answer_matrix)

for i in range(len(answer_matrix)):
    row_sum = sum(answer_matrix[i])
    print(f"{answer_matrix[i]} сумма строки: {row_sum}")


#Задание 3.
fruits = [['Banana', 'apple'],
        ['apricot', 'Avocado'],
        ['lime', 'lemon'],
        ['Mango', 'grapes']]

print("Способ 1:")
for row in fruits:
    for fruit in row:
        if fruit[0].isupper():
            print(fruit)

print("\nСпособ 2:")
capital_fruits = [fruit for row in fruits for fruit in row if fruit[0].isupper()]
print(capital_fruits)

print("\nСпособ 3:")
for row in fruits:
    for fruit in row:

        if fruit[0].isupper():
            print(fruit)

#Задание 4.
random_elements = [
    ['toy', 'bee', 'cheese', 'ear'],
    [False, 'word', '0110110', 10],
    ['happiness', '(」°ロ°)」', 'luck', None],
    ['car', '<- code ->', 4.7, True]]

print
for index, row in enumerate(random_elements):
    if index % 2 == 1:
        print(f"Строка с индексом {index}: {row}")

#Задание 5.
# 1. Ввод количества строк
rows = int(input("Введите количество строк: "))

# 2. Ввод количества столбцов
cols = int(input("Введите количество столбцов: "))

# 3. Пустой массив для будущей матрицы
matrix = []

# 4. Цикл в диапазоне количества строк
for i in range(rows):
    # 5. Пустой массив для строк
    row = []
    
    # 6. Цикл в диапазоне количества столбцов
    for j in range(cols):
        # 7. Ввод чисел
        value = float(input(f"Введите значение элемента [{i}][{j}]: "))
        # 8. В массив для строк добавляются числа
        row.append(value)
    
    # 9. Массивы (строки) с числами добавляются в массив матрицы
    matrix.append(row)

# 10. Вывод массива матрицы
print("\nВаш двумерный массив:")
for row in matrix:
    print(row)















By lonely
