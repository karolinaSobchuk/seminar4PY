#Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
#И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

import random

lengh = int(input('Введите длину: '))
width = int(input('Введите ширину: '))

l = []
w = []

for i in range(width):
    l.append(list())
    sum = 0
    for j in range(lengh):
        l[i].append(random.randint(0,100))
        sum += l[i][j]
    w.append(sum // lengh)
    print(f'{l[i]} - {w[i]}')