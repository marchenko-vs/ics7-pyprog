from math import sqrt


print('Вычислитель корней квадратного уравнения')
a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

if a == 0:
    if b != 0:
        x = -c / b
        print('Корень уравнения равен {:5.2f}'.format(x))
    elif c == 0:
        print('X - любое число')
    else:
        print('Решений нет')
else:
    d = b ** 2 - 4 * a * c  # Нахождение дискриминанта
    if d < 0:
        print('Корни уравнения комплексные')
    elif d == 0:
        x = -b / (2 * a)
        print('Корень уравнения равен {:5.2f}'.format(x))
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        print('Корни уравнения равны {:5.2f} и {:5.2f}'.format(x1, x2))
