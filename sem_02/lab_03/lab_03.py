import math
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np


def f(x):
    return math.sin(x)


def secant_method(left_b, right_b, eps, option, max_iter=500):
    i = 0
    condition = True
    while condition:
        if f(left_b) == f(right_b):
            return 0, i, 1
        x = left_b - (right_b - left_b) * f(left_b) / (f(right_b) - f(left_b))
        left_b = right_b
        right_b = x
        i += 1
        if i > max_iter:
            print('Not Convergent!')
            break
        if option == 1:
            condition = abs(x - left_b) > eps
        else:
            condition = abs(f(x)) > eps
    return x, i, 0

def submit_func():
    choice = opt.get()
    left_b = float(left_b_entry.get())
    right_b = float(right_b_entry.get())
    step = float(step_entry.get())
    epsilon = float(eps_entry.get())
    roots = list()
    answer = list()
    current_l = left_b
    current_r = left_b + step
    while current_r <= right_b:
        solution = [0, 0, 0, 0, 0]
        root, iterations, code = secant_method(current_l, current_r, epsilon,
                                               choice)
        if abs(f(root)) < epsilon and current_l <= root <= current_r and root \
                not in roots:
            solution[0] = current_l
            solution[1] = current_r
            solution[2] = root
            solution[3] = iterations
            solution[4] = code
            roots.append(root)
            answer.append(solution)
        current_l += step
        current_r += step
    if len(answer) == 0:
        messagebox.showinfo("Error", "No roots")
    counter = 0
    while counter < len(answer):
        tree.insert(parent='', index='end', iid=counter, text=counter + 1,
                    values=('[ {:5.3f} ; {:5.3f} ]'.format(answer[counter][0],
                                                           answer[counter][1]),
                            '{:8.7f}'.format(answer[counter][2]),
                            '{:.1e}'.format(f(answer[counter][2])),
                            answer[counter][3],
                            '{}'.format(answer[counter][4])))
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
main.title('Laboratory work 3')
main.geometry('1235x400+400+250')
main.resizable(False, False)

left_b_label = tk.Label(text='Left border', font='15')
left_b_label.place(x='45', y='15')
left_b_entry = tk.Entry(font='15', width='10')
left_b_entry.place(x='150', y='15')

right_b_label = tk.Label(text='Right border', font='15')
right_b_label.place(x='290', y='15')
right_b_entry = tk.Entry(font='15', width='10')
right_b_entry.place(x='400', y='15')

step_label = tk.Label(text='Step', font='15')
step_label.place(x='505', y='15')
step_entry = tk.Entry(font='15', width='10')
step_entry.place(x='550', y='15')

eps_label = tk.Label(text='Epsilon', font='15')
eps_label.place(x='690', y='15')
eps_entry = tk.Entry(font='15', width='10')
eps_entry.place(x='780', y='15')

opt = tk.IntVar()

first_checkbutton = tk.Radiobutton(font='15', text="First\noption", value=1,
                                   variable=opt, padx=15, pady=10)
first_checkbutton.place(x='900', y='5')

second_checkbutton = tk.Radiobutton(font='15', text="Second\noption", value=2,
                                    variable=opt, padx=15, pady=10)
second_checkbutton.place(x='900', y='60')

submit_button = tk.Button(text='Submit', font='15', command=submit_func)
submit_button.place(x='1040', y='15')

tree = ttk.Treeview(main, columns=('1', '2', '3', '4', '5'))
tree.insert(parent='', index='end', iid=-1, text='Number of root',
            values=('[ x[i] ; x[i + 1] ]', 'x', 'f(x)', 'Iterations',
                    'Exit code'))
tree.place(x='15', y='130')

tk.mainloop()
