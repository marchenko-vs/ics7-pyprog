from math import pi, cos, trunc


xMin = float(input('Введите минимальное значение аргумента: '))
xMax = float(input('Введите максимальное значение аргумента: '))
xStep = float(input('Введите шаг изменения аргумента: '))

xCurrent = xMin
eps = 0.00001  # Погрешность
sumNegP1 = 0
sumNegP2 = 0

if xMax < xMin or xStep <= 0:
    print('Ошибка ввода данных')
else:
    # Поиск min и max значений функции
    minFunc = 5 * xCurrent ** 3 + 2 * xCurrent ** 2 - 15 * xCurrent - 6
    maxFunc = 5 * (xCurrent+xStep) ** 3 + 2 * (xCurrent+xStep) ** 2 - 15 * (xCurrent+xStep) - 6

    print('|---------|---------|---------|')
    print('|    t    |    p1   |    p2   |')
    print('|---------|---------|---------|')
    while xCurrent <= xMax + eps:
        p1 = xCurrent - cos(pi * xCurrent) ** 2
        p2 = 5 * xCurrent ** 3 + 2 * xCurrent ** 2 - 15 * xCurrent - 6
        if p2 < minFunc:
            minFunc = p2
        elif p2 > maxFunc:
            maxFunc = p2
        if p1 < 0:
            sumNegP1 += p1
        if p2 < 0:
            sumNegP2 += p2
        print('|{:^9.3g}|{:^9.3g}|{:^9.3g}|'.format(xCurrent, p1, p2))
        xCurrent += xStep
    print('|---------|---------|---------|')
    print()
    print(minFunc, maxFunc)
    numOfSer = int(input('Введите кол-во засечек от 4 до 8: '))
    i = 0
    if numOfSer < 4 or numOfSer > 8:
        print('Ошибка ввода данных')
    else:
        print('------------------------------ График p2(t) ------------------------------------')
        print()
        currFunc = minFunc
        lenOfSer = (maxFunc - minFunc) / (numOfSer-1)
        space = trunc((85 / (numOfSer + 6)))
        znach = (maxFunc - minFunc) / (numOfSer - 1)
        print()
        while i < numOfSer:
            print('{:<6.3g}'.format(currFunc) + ' ' * (trunc(((currFunc - (currFunc - znach)))/(maxFunc-minFunc)*80) - 6), end='')
            znach = (maxFunc - minFunc) / (numOfSer - 1)
            currFunc = currFunc + znach
            i += 1
        currFunc = minFunc
        print()
        print('|', end='')
        while currFunc < maxFunc - eps:
            posOfSer = currFunc + lenOfSer
            print('-' * (trunc((posOfSer-currFunc)/(maxFunc-minFunc)*80) - 1) + '|', end='')
            currFunc += lenOfSer
        print('------>Y')
        posOfZero = trunc((-minFunc/(maxFunc-minFunc))*80)
        xCurrent = xMin
        while xCurrent <= xMax + eps:
            p2 = 5 * xCurrent ** 3 + 2 * xCurrent ** 2 - 15 * xCurrent - 6
            posOfDot = trunc(((p2 - minFunc)/(maxFunc-minFunc) * 80))
            if p2 < 0:
                print(' ' * posOfDot + '*' + ' ' * (posOfZero-posOfDot) + '|{:<4.1f}'.format(xCurrent))
            else:
                print(' ' * (posOfZero - 3) + '{:>4.1f}|'.format(xCurrent) + ' ' * (posOfDot - posOfZero - 4) + '*'  )
            xCurrent += xStep
        print(' ' * (posOfZero + 1) + '|')
        print(' ' * (posOfZero + 1) + 'X')
    print()
    print('Сумма отрицательных значений функции p1: {:4.2g}'.format(sumNegP1))
    print('Сумма отрицательных значений функции p2: {:4.2g}'.format(sumNegP2))


