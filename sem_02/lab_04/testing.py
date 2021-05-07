import tkinter as tk
from tkinter import messagebox
import math


def count_square(a, b, c):
    ab_x = b[0] - a[0]
    ab_y = b[1] - a[1]
    ab = math.sqrt(ab_x * ab_x + ab_y * ab_y)

    bc_x = c[0] - b[0]
    bc_y = c[1] - b[1]
    bc = math.sqrt(bc_x * bc_x + bc_y * bc_y)

    ac_x = c[0] - a[0]
    ac_y = c[1] - a[1]
    ac = math.sqrt(ac_x * ac_x + ac_y * ac_y)

    half_p = (ab + bc + ac) / 2
    triangle_s = math.sqrt(
        half_p * (half_p - ab) * (half_p - bc) * (half_p - ac))

    circle_r = (ab * bc * ac) / (4 * triangle_s)
    circle_s = circle_r ** 2 * math.pi

    return circle_s - triangle_s

def brute_force(matrix):
    min_result = 1e9
    i = 0
    j = 1
    k = 2
    length = len(matrix)
    answer_array = [0, 0, 0, 0, 0, 0]

    while i < length - 2:
        while j < length - 1:
            while k < length:
                if (matrix[i][0] != matrix[j][0] or matrix[j][0] != matrix[k][
                    0] or matrix[i][0] != matrix[k][0]) and (
                        matrix[i][1] != matrix[j][1] or matrix[j][1] !=
                        matrix[k][1] or matrix[i][1] != matrix[k][1]):
                    result = count_square(matrix[i], matrix[j], matrix[k])
                    if result < min_result:
                        min_result = result
                        answer_array[0] = matrix[i][0]
                        answer_array[1] = matrix[i][1]
                        answer_array[2] = matrix[j][0]
                        answer_array[3] = matrix[j][1]
                        answer_array[4] = matrix[k][0]
                        answer_array[5] = matrix[k][1]
                k += 1
            j += 1
            k = j + 1
        i += 1
        j = i + 1
        k = j + 1

    return answer_array

def submit_func():
    coords = input_entry.get()
    coords_array = list(map(int, coords.split()))
    coords_matrix = []
    pair = []
    answer_coords = list()

    if len(coords_array) < 6:
        messagebox.showinfo("Error", "Less than three points")
        return None

    if len(coords_array) % 2 != 0:
        size = len(coords_array) - 2
    else:
        size = len(coords_array) - 1

    for i in range(0, size, 2):
        canvas.create_oval(coords_array[i], coords_array[i + 1],
                           coords_array[i],
                           coords_array[i + 1], width=5)
        pair = [coords_array[i], coords_array[i + 1]]
        coords_matrix.append(pair)

    answer_coords = brute_force(coords_matrix)

    canvas.create_polygon((answer_coords[0], answer_coords[1]),
                          (answer_coords[2],
                           answer_coords[3]),
                          (answer_coords[4], answer_coords[5]), fill='white',
                          outline='red', width=2)


root = tk.Tk()
root.title("Laboratory work 4")
root.geometry("700x400+500+200")
root.resizable(False, False)

input_label = tk.Label(text='Enter coordinates:')
input_label.place(x=10, y=20)

input_label = tk.Label(text='You must enter coordinates separated by a space:\n'
                            'x1 y1 x2 y2 x3 y3 x4 y4')
input_label.place(x=10, y=50)

input_entry = tk.Entry()
input_entry.place(x=120, y=20, width=165)

input_button = tk.Button(text='Submit', command=submit_func)
input_button.place(x=15, y=100, width=270)

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.place(x=300)

root.mainloop()
