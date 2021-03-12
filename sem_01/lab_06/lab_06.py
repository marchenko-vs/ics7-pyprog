# Автор программы - Марченко Владислав (ИУ7-13Б)
# Вариант 13
# Программа предлагает на выбор 7 вариантов работы со списком

def isfloat(index):
    try:
        float(index)
        return True
    except ValueError:
        return False

array = []
position = -5
print(' ' * 35 + 'Меню')
print('1. Проинициализировать список первыми N элементами заданного ряда')
print('2. Добавить элемент в произвольное место списка')
print('3. Удалить произвольный элемент из списка')
print('4. Очистить список')
print('5. Найти значение K-го экстремума в списке, если он является списком чисел')
print('6. Найти наиболее длинную последовательность чисел, в которой все,\nначиная '
      'с 3-го, являются суммой двух предыдущих')
print('7. Найти наиболее длинную последовательность, содержащую результат игры в слова')
print('8. Выйти из программы')
print()
while True:
    choice = int(input('Выберите вариант: '))
    if choice == 1:
        i = 0
        t = 0
        u = 1
        array = []
        n = int(input('Введите кол-во элементов N: '))
        x = int(input('Введите значение аргумента X: '))
        while i < n:
            array.append(str(u))
            t += 2
            u = u * x ** 2 * ((t - 1) / t)
            i += 1
        print(array)
    elif choice == 2:
        newElement = str(input('Введите новый элемент: '))
        placeToCreate = int(input('Введите индекс: '))
        array.insert(placeToCreate, newElement)
        print(array)
    elif choice == 3:
        placeToDel = int(input('Введите индекс элемента, который нужно удалить: '))
        if placeToDel >= len(array):
            print('Ошибка: элемент с таким индексом не существует')
        else:
            array.pop(placeToDel)
        print(array)
    elif choice == 4:
        array.clear()
        print(array)
    elif choice == 5:
        extremum = False
        if len(array) < 3:
            print('Экстремум в данном списке не существует')
            continue
        numOfExtremum = int(input('Введите порядковый номер K экстремума: '))
        if numOfExtremum <= 0:
            print('Ошибка: порядковый номер должен быть больше нуля')
        else:
            help = True
            for i in range(0, len(array)):
                boolean = isfloat(array[i])
                if not boolean:
                    print('Ошибка: список состоит не только из чисел')
                    help = False
                    break
                array[i] = float(array[i])
            if help:
                count = 0
                i = 1
                if array[1] > array[0]:
                    directionMain = 1
                else:
                    directionMain = 0
                while count < numOfExtremum and i < len(array)-1:
                    if array[i + 1] > array[i]:
                        dirSecondary = 1
                    else:
                        dirSecondary = 0
                    if array[i + 1] < array[i] and dirSecondary != directionMain:
                        extremum = array[i]
                        directionMain = 0
                        count += 1
                    elif array[i + 1] > array[i] and dirSecondary != directionMain:
                        extremum = array[i]
                        directionMain = 1
                        count += 1
                    i += 1
                if not extremum:
                    print('Экстремум в данном списке не существует')
                else:
                    print(extremum)
    elif choice == 6:
        if len(array) < 3:
            print('Ошибка: в списке менее трех элементов')
        else:
            help = True
            for i in range(0, len(array)):
                boolean = isfloat(array[i])
                if not boolean:
                    print('Ошибка: список состоит не только из чисел')
                    help = False
                    break
                array[i] = float(array[i])
            if help:
                maxLen = 0
                i = 0
                for j in range(2, len(array)):
                    if float(array[j]) == float(array[j - 1]) + float(array[j - 2]):
                        i += 1
                    else:
                        if maxLen < i:
                            maxLen = i
                            position = j - 1
                        i = 0
                else:
                    if maxLen < i:
                        maxLen = i
                        position = j
                    f = position - (maxLen + 1)
                    if position == -5:
                        print('В списке нет нужной последовательности')
                    else:
                        while f <= position and f < len(array):
                            print(array[f], end='  ')
                            f += 1
                        print()
    elif choice == 7:
        if len(array) < 2:
            print('Ошибка: в списке менее двух элементов')
        else:
            help = True
            for i in range(0, len(array)):
                boolean = isfloat(array[i])
                if boolean:
                    print('Ошибка: список состоит не только из строк')
                    help = False
                    break
                array[i] = str(array[i])
            if help:
                maxLen = 0
                i = 0
                for j in range(1, len(array)):
                    if str(array[j])[0].lower() == str(array[j - 1])[len(str(array[j - 1])) - 1].lower():
                        i += 1
                    else:
                        if maxLen < i:
                            maxLen = i
                            position = j - 1
                        i = 0
                if maxLen < i:
                    maxLen = i
                    position = j
                f = position - maxLen
                if position == -5:
                    print('В списке нет нужной последовательности')
                else:
                    while f <= position:
                        print(array[f], end=' ')
                        f += 1
                    print()
    elif choice == 8:
        exit()
    else:
        print('Ошибка: выберите вариант от 1 до 8')
