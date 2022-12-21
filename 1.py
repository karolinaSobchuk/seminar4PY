#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

lenth = int(input('Введите длину списка: '))
sum = []
for i in range(lenth):
    sum.append(random.randint(0, 10))
summ = 0
for i in range(1, len(sum), 2):
    summ += sum[i]

print(sum)
print(summ)

