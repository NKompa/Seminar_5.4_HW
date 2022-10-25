# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [int(num) for num in input('Введите несколько чисел через пробел: ').split()]
print(list)
unique_list = []
for number in list:
    count = list.count(number)
    if count > 1: continue
    else: unique_list.append(number)

print(unique_list)