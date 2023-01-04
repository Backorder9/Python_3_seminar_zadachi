'''
Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка,
стоящих на позиции с нечётным индексом.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
list_num = []
n = int(input('Введите количество элементов списка: '))
import random
while len(list_num) < n:
    list_item = random.randint(1, 100)
    if list_item not in list_num:
        list_num.append(list_item)
sum = 0
for i in range(0, n):
    if i%2 == 0:
        pass
    if i%2 != 0:
        sum = sum + list_num[i]
print(f'Создан список случайных целых чисел из {n} элементов:')
print(list_num)
print()
print(f'Сумма элементов списка с нечётными индексами: {sum}')