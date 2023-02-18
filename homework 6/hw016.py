# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("Введите количество элементов в массиве: "))
import random
list_1=[random.randint(-100, 100) for i in range(n)]
print(*list_1)

maxnumber = int(input("Введите максимальное число: "))
minnumber = int(input("Введите минимательное число: "))
list_res = []
if maxnumber >= minnumber:
   for i in range(len(list_1)):
      if maxnumber >= list_1[i] and minnumber <= list_1[i]:
          list_res.append(i)
   print("Количество значений от заданного минимума до заданного максимума:",len(list_res))
   print("Индексы значений от заданного минимума до заданного максимума:",*list_res)
