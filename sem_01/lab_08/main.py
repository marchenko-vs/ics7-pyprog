def antiDerivative(x):
    return x ** 3 / 3  # Здесь можно менять первообразную


def newtonLeibniz(a, b):
    return antiDerivative(b) - antiDerivative(a)


def f(x):
    return x ** 2  # Здесь можно менять функцию


def rectangleMethod(a, b, n):
    result = 0
    h = (b - a) / n
    for j in range(n):
        result += f(a + h * (j + 0.5))
    result *= h
    return result


def boolesRule(a, b, n):
    h = (b - a) / n
    y1 = 0
    y2 = 0
    y3 = 0
    result = 7 * (f(a) + f(b))
    for i in range(1, n):
        x = a + h * i
        if i % 2 != 0:
            y1 += f(x)
        elif i % 4 == 0:
            y2 += f(x)
        else:
            y3 += f(x)
    result = result + 32 * y1 + 12 * y3 + 14 * y2
    return 2 / 45 * h * result


a = float(input('Введите нижнюю границу интегрирования A: '))
b = float(input('Введите верхнюю границу интегрирования B: '))
n1 = int(input('Введите кол-во разбиений N1: '))
n2 = int(input('Введите кол-во разбиений N2: '))
print('|----------------------------|------------|------------|')
print('|           Метод            |     N1     |     N2     |')
print('|----------------------------|------------|------------|')
print('|   Средних прямоугольников  |', end='')
res1 = rectangleMethod(a, b, n1)
res2 = rectangleMethod(a, b, n2)
print('{:^12.5f}|'.format(res1), end='')
print('{:^12.5f}|'.format(res2))
print('|----------------------------|------------|------------|')
print('|        Правило Буля        |', end='')
res3 = boolesRule(a, b, n1)
res4 = boolesRule(a, b, n2)
print('{:^12.5f}|'.format(res3), end='')
print('{:^12.5f}|'.format(res4))
print('|----------------------------|------------|------------|')
print()

# Вторая часть

print('Правило Буля - менее точный способ вычисления интегралов')
eps = float(input('Введите значение погрешности: '))
n = 1
while abs(boolesRule(a, b, n) - boolesRule(a, b, 2 * n)) > eps:
    n += 1
res5 = boolesRule(a, b, n)
print('При N = {} интеграл равен {:10.7f} с погрешностью {}'.format(n, res5, eps))
print()
absError = abs(newtonLeibniz(a, b) - res4)
relError = abs((newtonLeibniz(a, b) - res4) / newtonLeibniz(a, b))
print('При N = {}'.format(n2))
print('Абсолютная погрешность равна {:10.7g}'.format(absError))
print('Относительная погрешность равна {:10.7g}'.format(relError))
