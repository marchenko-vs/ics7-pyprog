import tkinter as tk
from tkinter import messagebox


position = 0  # Variable for text insertion


def four_in_ten(number):
    if number < 0:
        negative = 0
        number = str(number)[1::]
    else:
        negative = 1
        number = str(number)
    result = 0
    power = 0
    for i in number:
        if i == '.':
            break
        power += 1
    power -= 1
    for i in number:
        if i != '.':
            result += int(i) * 4 ** power
            power -= 1
    if not negative:
        return -float(result)
    else:
        return float(result)


def ten_in_four(number):
    if number < 0:
        negative = 0
        int_part = int(abs(number) // 1)
        number = str(abs(number))
    else:
        negative = 1
        int_part = int(number // 1)
        number = str(number)
    int_part_result = ''
    float_part_result = ''
    float_part = '0'
    for i in range(len(str(int_part)), len(number)):
        float_part += number[i]
    while int_part != 0:
        mod = int_part // 4
        int_part_result += str(int(int_part % 4))
        int_part = mod
    float_part = float(float_part)
    for i in range(5):
        mod = float_part * 4
        float_part_result += str(int(mod // 1))
        float_part = mod - mod // 1
    if not negative:
        return -float(int_part_result[::-1] + '.' + float_part_result)
    else:
        return float(int_part_result[::-1] + '.' + float_part_result)


def info_click():
    messagebox.showinfo("Инфо", "Автор программы - Марченко Владислав, группа ИУ7-23Б.\n"
                                "Программа дает возможность выполнять сложение и вычитание"
                                " вещественных чисел в четверичной системе счисления.")


def clear_input():
    global position
    input_entry.delete(0, 'end')
    position = 0


def clear_output():
    output_entry.delete(0, 'end')


def clear_all():
    clear_input()
    clear_output()


def add_zero():
    global position
    input_entry.insert(position, 0)
    position += 1


def add_one():
    global position
    input_entry.insert(position, 1)
    position += 1


def add_two():
    global position
    input_entry.insert(position, 2)
    position += 1


def add_three():
    global position
    input_entry.insert(position, 3)
    position += 1


def add_dot():
    global position
    input_entry.insert(position, '.')
    type_dot = False
    position += 1


def add_plus():
    global position
    input_entry.insert(position, ' + ')
    position += 3


def add_minus():
    global position
    operator = '-'
    input_entry.insert(position, ' - ')
    position += 3


def equals():
    expression = input_entry.get().split()
    if expression[1] == '+':
        result = ten_in_four(four_in_ten(float(expression[0])) + four_in_ten(float(expression[2])))
    else:
        result = ten_in_four(four_in_ten(float(expression[0])) - four_in_ten(float(expression[2])))
    output_entry.delete(0, 'end')
    output_entry.insert(0, str(result))


main = tk.Tk()
main.title('ЛР 1')
main.geometry("255x350")
main.resizable(height=False, width=False)

main_menu = tk.Menu()

do_menu = tk.Menu(tearoff=0)
do_menu.add_command(label="Сложение", command=add_plus)
do_menu.add_command(label="Вычитание", command=add_minus)

clear_menu = tk.Menu(tearoff=0)
clear_menu.add_command(label="Поле ввода", command=clear_input)
clear_menu.add_command(label="Поле вывода", command=clear_output)
clear_menu.add_command(label="Все поля", command=clear_all)

main_menu.add_cascade(label="Действия", menu=do_menu)
main_menu.add_cascade(label="Очистить", menu=clear_menu)
main_menu.add_cascade(label="Инфо", command=info_click)

input_label = tk.Label(text='Ввод')
input_label.place(x='20', y='10')
input_entry = tk.Entry(font=10)
input_entry.place(x='20', y='30', height='25', width='215')

output_label = tk.Label(text='Вывод')
output_label.place(x='20', y='70')
output_entry = tk.Entry(font=10)
output_entry.place(x='20', y='90', height='25', width='215')

three_button = tk.Button(text='3', command=add_three, font=10)
three_button.place(x='20', y='140', height='50', width='50')

two_button = tk.Button(text='2', command=add_two, font=10)
two_button.place(x='100', y='140', height='50', width='50')

one_button = tk.Button(text='1', command=add_one, font=10)
one_button.place(x='180', y='140', height='50', width='50')

zero_button = tk.Button(text='0', command=add_zero, font=10)
zero_button.place(x='20', y='210', height='50', width='50')

plus_button = tk.Button(text='+', command=add_plus, font=10)
plus_button.place(x='100', y='210', height='50', width='50')

minus_button = tk.Button(text='-', font=10, command=add_minus)
minus_button.place(x='180', y='210', height='50', width='50')

dot_button = tk.Button(text='.', font=10, command=add_dot)
dot_button.place(x='60', y='280', height='50', width='50')

equal_button = tk.Button(text='=', command=equals, font=10)
equal_button.place(x='140', y='280', height='50', width='50')

main.config(menu=main_menu)

main.mainloop()
