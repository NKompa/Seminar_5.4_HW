# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число: '))
factors = []
i = 2
while i <= N:
    if N % i == 0:
        factors.append(i)
        N /= i
    else: i+=1
print(f'Простые множители числа: {factors}')