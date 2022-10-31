# Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# N = int(input('Введите N: '))
# from random import randint 
# L = [randint(1,9) for x in range(N)]

# sum = 0
# print(L, end=' ответ: ')
# for i in L:
#     if L.index(i) % 2 != 0:
#         sum += i
#     i+=1

# print(sum)
import math

N = int(input('Введите длину массива: '))
from random import randint 
L = [randint(1,9) for x in range(N)]

print(L, end=' ответ: ')
print(sum(x for i, x in enumerate(L) if i % 2 != 0))