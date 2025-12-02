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
