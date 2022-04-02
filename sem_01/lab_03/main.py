from math import sqrt


x1 = int(input('Введите x-координату первой вершины треугольника: '))
y1 = int(input('Введите y-координату первой вершины треугольника: '))
x2 = int(input('Введите x-координату второй вершины треугольника: '))
y2 = int(input('Введите y-координату второй вершины треугольника: '))
x3 = int(input('Введите x-координату третьей вершины треугольника: '))
y3 = int(input('Введите y-координату третьей вершины треугольника: '))

ABx = x2 - x1  # Находим координаты векторов-сторон треугольника
ABy = y2 - y1
BCx = x3 - x2
BCy = y3 - y2
ACx = x3 - x1
ACy = y3 - y1

# Пусть a = AB, b = BC, c = AC

a = sqrt(ABx * ABx + ABy * ABy)  # Находим длины сторон треугольника
b = sqrt(BCx * BCx + BCy * BCy)
c = sqrt(ACx * ACx + ACy * ACy)

if abs(a - b - c) >= 0.01 or abs(b - a - c) >= 0.01 or abs(c - a - b) >= 0.01:
    print()
    print('Такого треугольника не существует')
else:
    p = (a + b + c) / 2  # Полупериметр треугольника
    s = sqrt(p * (p - a) * (p - b) * (p - c))  # Площадь треугольника

    if a > b and a > c:  # Поиск наибольшей стороны
        h = (2 * s) / a  # Находим длину высоты
    elif b > a and b > c:
        h = (2 * s) / b
    elif c > a and c > b:
        h = (2 * s) / c

    x4 = float(input('Введите x-координату точки: '))
    y4 = float(input('Введите y-координату точки: '))

    AOx = x4 - x1  # Находим координаты векторов AO, BO, CO, где O -
    AOy = y4 - y1  # точка с координатами (x4; y4)
    BOx = x4 - x2
    BOy = y4 - y2
    COx = x4 - x3
    COy = y4 - y3

    AO_length = sqrt(AOx * AOx + AOy * AOy)  # Длины отрезков, соединяющих точку O с вершинами
    BO_length = sqrt(BOx * BOx + BOy * BOy)
    CO_length = sqrt(COx * COx + COy * COy)

    p1 = (a + AO_length + BO_length) / 2
    s1 = sqrt(p1 * (p1 - a) * (p1 - AO_length) * (p1 - BO_length))
    p2 = (b + BO_length + CO_length) / 2
    s2 = sqrt(p2 * (p2 - b) * (p2 - CO_length) * (p2 - BO_length))
    p3 = (c + AO_length + CO_length) / 2
    s3 = sqrt(p3 * (p3 - c) * (p3 - CO_length) * (p3 - AO_length))

    print()
    print('Длина стороны a: {:3.2f}, длина стороны b: {:3.2f}, '
          'длина стороны c: {:3.2f}'.format(a, b, c))
    print('Длина высоты, проведенной из наибольшего угла: {:3.2f}'.format(h))
    if abs(s - (s1 + s2 + s3)) <= 0.01:
        l1 = (2 * s1) / a
        l2 = (2 * s2) / b
        l3 = (2 * s3) / c
        if l1 <= l2 and l1 <= l3:
            l = l1
        elif l2 <= l1 and l2 <= l3:
            l = l2
        else:
            l = l3
        print('Точка O({};{}) принадлежит треугольнику'.format(x4, y4))
        print('Расстояние от точки O до ближайшей стороны: {:3.2f}'.format(l))
    else:
        print('Точка O({};{}) не принадлежит треугольнику'.format(x4, y4))
    if a > b and a > c:
        if a * a > c * c + b * b + 0.01:
            print('Треугольник тупоугольный')
        else:
            print('Треугольник не тупоугольный')
    elif b > a and b > c:
        if b * b > c * c + a * a + 0.01:
            print('Треугольник тупоугольный')
        else:
            print('Треугольник не тупоугольный')
    else:
        if c * c > b * b + a * a + 0.01:
            print('Треугольник тупоугольный')
        else:
            print('Треугольник не тупоугольный')
