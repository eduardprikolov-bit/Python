#Задание 1.
data = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]

print("начальный список")
for row in data:
    print(row)

modified_data = [row[:] for row in data]

print("\nбез папок и с заменой data")
for i in range(len(modified_data)):
    new_row = []
    for j in range(len(modified_data[i])):
        if modified_data[i][j] != 'folder':
            # Заменяем data.accdb на data.sql
            if modified_data[i][j] == 'data.accdb':
                new_row.append('data.sql')
            else:
                new_row.append(modified_data[i][j])
    modified_data[i] = new_row

for row in modified_data:
    print(row)

print("\nЭлементы с расширением .py:")
py_files = []
for row in data:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)

print(py_files)

print("\nЭлементы с расширением .js с добавлением new_:")
js_files_new = []
for row in data:
    for item in row:
        if item.endswith('.js'):
            js_files_new.append('new_' + item)

print(js_files_new)
