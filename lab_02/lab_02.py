#  Метод вставок с барьером

import random as r
import time as t
import tkinter as tk

def insert_sort_with_barrier(array):
    array = [0] + array
    for i in range(1, len(array)):
        array[0] = array[i]
        j = i - 1
        while (array[0] < array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = array[0]
    return array[1:]


#  Задание первое
example_array = [-2, 5, 3, 0, -7, 10, -8, -4, -15, 9]
example_array_sorted = insert_sort_with_barrier(example_array)
print(example_array_sorted)
#  Задание второе
n1, n2, n3 = map(int, input("Enter three sizes of lists: ").split())
#  Случайные массивы
random_array_1 = [r.randint(-100, 250) for i in range(n1)]
random_array_2 = [r.randint(-100, 250) for i in range(n2)]
random_array_3 = [r.randint(-100, 250) for i in range(n3)]
#  Упорядоченные массивы
ordered_array_1 = sorted(random_array_1)
ordered_array_2 = sorted(random_array_2)
ordered_array_3 = sorted(random_array_3)
#  Обратно упорядоченные массивы
reversed_array_1 = ordered_array_1[::-1]
reversed_array_2 = ordered_array_2[::-1]
reversed_array_3 = ordered_array_3[::-1]

#  Сделать GUI : вывод первоначального массива в одном лейбле, вывод сортированного во втором.
#  Ввод размеров N в одном поле через пробел (.split()), типы массивов в лейблах.
#  Время вывести тоже в лейблах.

#  Вывод времени, просто пример.
'''sort_time = t.time()
insert_sort_with_barrier(ordered_array_1)
print(("Ordered array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(random_array_1)
print(("Random array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(reversed_array_1)
print(("Reversed array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(ordered_array_2)
print(("Ordered array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(random_array_2)
print(("Random array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(reversed_array_2)
print(("Reversed array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(ordered_array_3)
print(("Ordered array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(random_array_3)
print(("Random array: {:10.9f}").format(t.time() - sort_time))

sort_time = t.time()
insert_sort_with_barrier(reversed_array_3)
print(("Reversed array: {:10.9f}").format(t.time() - sort_time))'''
