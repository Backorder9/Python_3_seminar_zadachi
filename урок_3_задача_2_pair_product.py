'''
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
'''
list_num = []
n = 10
import random
while len(list_num) < n:
    list_item = random.randint(1, 10)
    if list_item not in list_num:
        list_num.append(list_item)
pairs_prod = []
for i in range(0, n//2):
    prod = list_num[i]*list_num[n-1-i]
    pairs_prod.append(prod)
print(f'Создан список случайных целых чисел из {n} элементов:')
print(list_num)
print()
print('Список произведений пар симметричных элементов:')
print(pairs_prod)