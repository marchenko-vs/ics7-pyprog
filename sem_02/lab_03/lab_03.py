import math as m
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np


def f(x):
    return x*x - 4


def secant_method_1(a, b, eps, n=50):
    i = 0
    condition = True
    while condition:
        if f(a) == f(b):
            break
        if abs(f(a)) < 1e-5:
            x = a
            break
        if abs(f(b)) < 1e-5:
            x = b
            break
        x = a - (b - a) * f(a) / (f(b) - f(a))
        condition = abs(x - a) > eps
        a = b
        b = x
        i += 1
        if i > n:
            return 0
    return x, i

def secant_method_2(a, b, eps, n=50):
    i = 0
    condition = True
    while condition:
        if f(a) == f(b):
            break
        x = a - (b - a) * f(a) / (f(b) - f(a))
        a = b
        b = x
        i += 1
        if i > n:
            return 0
        condition = abs(f(x)) > eps
    return x, i

def submit_func():
    opt = option.get()
    left_b = float(left_b_entry.get())
    right_b = float(right_b_entry.get())
    step = float(step_entry.get())
    eps = float(eps_entry.get())
    answer = []
    if opt == 1:
        current_b = left_b + step
        while current_b <= right_b:
            solution = [0, 0, 0, 0]
            root, iterations = secant_method_1(left_b, current_b, eps)
            solution[0] = left_b
            solution[1] = current_b
            solution[2] = root
            solution[3] = iterations
            answer.append(solution)
            left_b += step
            current_b += step
    elif opt == 2:
        current_b = left_b + step
        while current_b <= right_b:
            solution = [0, 0, 0, 0]
            root, iterations = secant_method_2(left_b, current_b, eps)
            solution[0] = left_b
            solution[1] = current_b
            solution[2] = root
            solution[3] = iterations
            answer.append(solution)
            left_b += step
            current_b += step
    counter = 0
    while counter < len(answer):
        tree.insert(parent='', index='end', iid=counter, text=counter + 1,
                    values=('[ {:5.3f} ; {:5.3f} ]'.format(answer[counter][0],
                                                           answer[counter][1]),
                            '{:8.7f}'.format(answer[counter][2]),
                            '{:.1e}'.format(f(answer[counter][2])),
                            answer[counter][3],
                            '0'))
        counter += 1

    left_b = float(left_b_entry.get())
    right_b = float(right_b_entry.get())
    x_list = np.linspace(left_b, right_b, 500)
    y_list = [f(x) for x in x_list]
    plt.title('График')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_list, y_list)
    for el in answer:
        plt.scatter(el[2], f(el[2]), c='red')
    if f(x_list[0]) - f(x_list[1]) < 0:
        growing = True
    else:
        growing = False
    for i in range(len(x_list) - 1):
        if growing and f(x_list[i + 1]) - f(x_list[i]) < 0:
            plt.scatter(x_list[i], f(x_list[i]), c='green')
            growing = False
        elif not growing and f(x_list[i + 1]) - f(x_list[i]) > 0:
            plt.scatter(x_list[i], f(x_list[i]), c='green')
            growing = True
    plt.grid(True)
    blue_patch = mp.Patch(color='blue', label='f(x)')
    red_patch = mp.Patch(color='red', label='Корни')
    green_patch = mp.Patch(color='green', label='Экстремумы')
    plt.legend(loc='upper left', handles=[blue_patch, red_patch, green_patch])
    plt.show()


main = tk.Tk()
main.title('Лабораторная работа 3')
main.geometry('1235x400+400+250')
main.resizable(False, False)

left_b_label = tk.Label(text='Левая граница', font='15')
left_b_label.place(x='15', y='15')
left_b_entry = tk.Entry(font='15', width='10')
left_b_entry.place(x='150', y='15')

right_b_label = tk.Label(text='Правая граница', font='15')
right_b_label.place(x='260', y='15')
right_b_entry = tk.Entry(font='15', width='10')
right_b_entry.place(x='400', y='15')

step_label = tk.Label(text='Шаг', font='15')
step_label.place(x='510', y='15')
step_entry = tk.Entry(font='15', width='10')
step_entry.place(x='550', y='15')

eps_label = tk.Label(text='Точность', font='15')
eps_label.place(x='660', y='15')
eps_entry = tk.Entry(font='15', width='10')
eps_entry.place(x='780', y='15')

option = tk.IntVar()

first_checkbutton = tk.Radiobutton(font='15', text="Первый\nспособ", value=1,
                                   variable=option, padx=15, pady=10)
first_checkbutton.place(x='900', y='5')

second_checkbutton = tk.Radiobutton(font='15', text="Второй\nспособ", value=2,
                                    variable=option, padx=15, pady=10)
second_checkbutton.place(x='900', y='60')

submit_button = tk.Button(text='Подтвердить', font='15', command=submit_func)
submit_button.place(x='1040', y='15')

tree = ttk.Treeview(main, columns=('1', '2', '3', '4', '5'))
tree.insert(parent='', index='end', iid=-1, text='Номер корня',
            values=('[ x[i] ; x[i + 1] ]', 'x', 'f(x)', 'К-во итераций',
                    'Код ошибки'))
tree.place(x='15', y='130')

tk.mainloop()
