a = ["00:00","01:10","02:20","03:30","04:40","05:50","10:01","11:11","12:21","13:31","14:41","15:51","20:02","21:12","22:22","23:32"] # Массив А со значениями времени, которые являютя палиндромами
b = input() # Пользователь вводит время
for i in range(len(a)):   # Цикл for от i до значения в рамках, равной длине a
    if a[i] > b: exit(print(a[i]))  # Если элемент i в массиве a больше введеного значения, то выйти из цикла с выводом i
print("00:00") # Если же значение i в массиве a меньше b, то вывести 00:00
