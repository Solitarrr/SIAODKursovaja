n = int(input()) # Ввод значения в n
for i in range(n):  # Цикл for от элемента i до n
    a, b = input().split()   # Делит начальную строку на подстроки
    if a != b:   # Если а не равно значению b
        print("Happy Alex")   # То вывести Happy Alex
        exit()   # И выйти
print("Poor Alex")   # Либо же вывести Poor Alex