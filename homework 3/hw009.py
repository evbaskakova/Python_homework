# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов в массиве: "))
list_1 = []
for i in range(n):
    list_1.append(int(input(f"Введите элемент массива: ")))
print(*list_1)
x = int(input("Введите число: "))

count = list_1[0]
for i in list_1:
    if abs(i - x) < abs(count - x):
        count = i

print(count) 