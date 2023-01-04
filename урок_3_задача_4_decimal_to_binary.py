'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10
'''
dec_num = int(input("Введите целое десятичное число: "))
whole = dec_num
bin_list = []
bin_list_reversed = []
while whole > 1:
    bin = whole % 2
    bin_list.append(bin)
    whole = whole // 2
    if whole == 1:
        bin_list.append(whole)
print(f'Десятичное число {dec_num} в двоичной записи =', "".join(map(str, list(reversed(bin_list)))))