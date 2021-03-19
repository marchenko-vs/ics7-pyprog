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

def sort_init_array():
    init_array = init_arr_entry.get()
    init_array = list(map(int, init_array.split()))
    sorted_arr_entry.delete(0, "end")
    sorted_arr_entry.insert(0, insert_sort_with_barrier(init_array))

def get_arr_len():
    array_len_var = array_len_entry.get()
    array_len_var = array_len_var.split()
    n1, n2, n3 = map(int, array_len_var)
    '''# Случайные массивы
    random_array_1 = [r.randint(-100, 250) for i in range(n1)]
    random_array_2 = [r.randint(-100, 250) for i in range(n2)]
    random_array_3 = [r.randint(-100, 250) for i in range(n3)]
    # Упорядоченные массивы
    ordered_array_1 = sorted(random_array_1)
    ordered_array_2 = sorted(random_array_2)
    ordered_array_3 = sorted(random_array_3)
    # Обратно упорядоченные массивы
    reversed_array_1 = ordered_array_1[::-1]
    reversed_array_2 = ordered_array_2[::-1]
    reversed_array_3 = ordered_array_3[::-1]'''



# GUI
main = tk.Tk()
main.title("Lab 2")
main.geometry("700x450")

init_arr_label = tk.Label(text="Initial array:", font="20")
init_arr_label.place(x="25", y="25")
sorted_arr_label = tk.Label(text="Sorted array:", font="20")
sorted_arr_label.place(x="25", y="60")
array_len_label = tk.Label(text="N1, N2, N3:", font="20")
array_len_label.place(x="25", y="120")

# table

table_label_1 = tk.Label(text="Sorted array", font="20")
table_label_1.place(x="25", y="230")
table_label_2 = tk.Label(text="Random array", font="20")
table_label_2.place(x="25", y="280")
table_label_3 = tk.Label(text="Reversed array", font="20")
table_label_3.place(x="25", y="330")

table_label_4 = tk.Label(text="N1", font="20")
table_label_4.place(x="240", y="200")
table_label_5 = tk.Label(text="N2", font="20")
table_label_5.place(x="390", y="200")
table_label_6 = tk.Label(text="N3", font="20")
table_label_6.place(x="535", y="200")

table_entry_1 = tk.Entry(font="20", width="15")
table_entry_1.place(x="180", y="230")
table_entry_2 = tk.Entry(font="20", width="15")
table_entry_2.place(x="180", y="280")
table_entry_3 = tk.Entry(font="20", width="15")
table_entry_3.place(x="180", y="330")
table_entry_4 = tk.Entry(font="20", width="15")
table_entry_4.place(x="330", y="230")
table_entry_5 = tk.Entry(font="20", width="15")
table_entry_5.place(x="330", y="280")
table_entry_6 = tk.Entry(font="20", width="15")
table_entry_6.place(x="330", y="330")
table_entry_7 = tk.Entry(font="20", width="15")
table_entry_7.place(x="480", y="230")
table_entry_8 = tk.Entry(font="20", width="15")
table_entry_8.place(x="480", y="280")
table_entry_9 = tk.Entry(font="20", width="15")
table_entry_9.place(x="480", y="330")



initial_array = tk.StringVar()
array_len_var = tk.StringVar()

init_arr_entry = tk.Entry(font="20", textvariable="initial_array")
init_arr_entry.place(x="130", y="27")
sorted_arr_entry = tk.Entry(font="20")
sorted_arr_entry.place(x="130", y="60")
array_len_entry = tk.Entry(font="20", textvariable="array_len_var")
array_len_entry.place(x="130", y="120")

init_arr_button = tk.Button(text="Submit", font="20", command=sort_init_array)
init_arr_button.place(x="350", y="23")

init_arr_button = tk.Button(text="Submit", font="20", command=get_arr_len)
init_arr_button.place(x="350", y="115")

main.mainloop()
'''
# Вывод времени, просто пример.
sort_time = t.time()
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
