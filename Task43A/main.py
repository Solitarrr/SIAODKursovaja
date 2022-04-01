n = int(input())  # Ввод пользователем данных, а именно кол-во строк
arr = []    # Массив
for i in range(n):  # Цикл for от i до n
    val = input()   # Ввод назвиний команд
    arr.append(val) # Append добавляет элемент в конец списка
a = arr[0]
a_count = 0
b_count = 0
for i in range(n):   # Цикл for от i до n
    if arr[i] == a:  # Если элемент i равен а
        a_count += 1
    else:
        b = arr[i]
        b_count += 1
if b_count > a_count: # В случае если b_count больше a_count
    print(b)   # Вывести b
else:
    print(a)   # Или же вывести а
