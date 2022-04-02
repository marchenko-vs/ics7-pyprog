m = int(input('Введите размер M квадратной матрицы: '))
print('Построчно введите элементы матрицы:')
matrix = [[int(i) for i in input().split()] for j in range(m)]
print('Повернутая на 180 градусов матрица:')
for i in range(m - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        print(matrix[i][j], end=' ')
    print()

a = [int(i) for i in input('Введите элементы списка A: ').split()]
b = [int(j) for j in input('Введите элементы списка B: ').split()]
if len(a) <= len(b):
    f = [[int(i) for i in range(len(b))] for j in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            f[i][k] = a[i] * b[k]
    for i in range(len(a)):
        for k in range(len(b)):
            print(f[i][k], end=' ')
        print()
else:
    f = [[int(i) for i in range(len(b))] for j in range(len(a))]
    for k in range(len(a)):
        for i in range(len(b)):
            f[k][i] = a[k] * b[i]
    for i in range(len(a)):
        for k in range(len(b)):
            print(f[i][k], end=' ')
        print()

num = 0
summary = 0
count = 0
x = len(f[0])
for j in range(x):
    for i in range(len(f)):
        summary += f[i][j]
    average = summary / len(f)
    for k in range(len(f)):
        if f[k][j] > average:
            count += 1
    if count == 1:
        print('В {} столбце {:5.2f} - ср. арифметическое, и {} элемент больше ср. '
              'арифметического'.format(num + 1, average, count))
    elif 2 <= count <= 4:
        print('В {} столбце {:5.2f} - ср. арифметическое, и {} элемента больше ср. '
              'арифметического'.format(num + 1, average, count))
    else:
        print('В {} столбце {:5.2f} - ср. арифметическое, и {} элементов больше ср. '
              'арифметического'.format(num + 1, average, count))
    summary = 0
    count = 0
    num += 1
