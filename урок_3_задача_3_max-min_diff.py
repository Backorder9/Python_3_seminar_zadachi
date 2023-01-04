'''
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов, отличной от 0.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
list_num = []
list_decimals =[]
n = 10
import random
while len(list_num) < n:
    x = random.uniform(1, 10)
    list_item = round(x,2)
    if list_item not in list_num:
        list_num.append(list_item)
        y = round(list_item % 1, 2)
        list_decimals.append(y)
diff_decimals = round (max(list_decimals) - min(list_decimals), 2)

print(f'Создан список случайных вещественных чисел из {n} элементов:')
print(list_num)
print()
print('Максимальная дробная часть элементов списка:', max(list_decimals))
print('Минимальная дробная часть элементов списка:', min(list_decimals))
print('Разница между макс. и мин. дробными частями элементов списка:', diff_decimals)