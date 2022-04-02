import pickle


def menu():
    print(' ' * 32 + 'Меню\n' + '1. Создание БД.\n'
          '2. Добавление записи в БД.\n'
          '3. Вывод всей БД.\n'
          '4. Поиск записи по одному полю.\n'
          '5. Поиск записи по двум полям.\n'
          '6. Выйти.\nБаза данных имеет поля "Компания", "Модель", "Год выпуска" и "КПП"')


numOfDicts = 0  # Счетчик для кол-ва записей в БД
isBaseCreated = False  # Создана ли БД
elementExist = False  # Найден ли элемент по ключевому полю
menu()
while True:
    choice = str(input('Введите пункт меню: '))
    if choice == '1':
        filename = 'database.bin'
        database = open(filename, 'wb')
        base = {'Компания': '', 'Модель': '', 'Год выпуска': '', 'КПП': ''}
        database.close()
        isBaseCreated = True
        print('База данных создана')
    elif choice == '2':
        if not isBaseCreated:
            print('Ошибка: база данных не создана')
        else:
            try:
                numOfData = int(input('Кол-во записей: '))
                database = open(filename, 'ab')
                print('Введите через пробел название компании, модель, годы выпуска и тип КПП')
                for i in range(numOfData):
                    base['Компания'], base['Модель'], base['Год выпуска'], base['КПП'] = input().split()
                    numOfDicts += 1
                    pickle.dump(base, database)
                database.close()
            except ValueError:
                print('Ошибка: введите целое число')
    elif choice == '3':
        if not isBaseCreated:
            print('Ошибка: база данных не создана')
        else:
            i = 0
            try:
                database = open(filename, 'rb')
                print('      Компания      |       Модель       | Год выпуска |        КПП      ')
                print('--------------------|--------------------|-------------|-----------------')
                while i < numOfDicts:
                    base = pickle.load(database)
                    print('{:^20}'.format(base['Компания']) + '|' + '{:^20}'.format(base['Модель']) +
                          '|     ' + base['Год выпуска'] + '    |' + '{:^20}'.format(base['КПП']))
                    print('--------------------|--------------------|-------------|-----------------')
                    i += 1
                database.close()
            except:
                print('Ошибка работы с файлом')
            finally:
                database.close()
    elif choice == '4':
        if not isBaseCreated:
            print('Ошибка: база данных не создана')
        else:
            try:
                searchField = input('Введите ключевое поле: ')
                searchWord = input('Введите ключевое слово: ')
                database = open(filename, 'rb')
                print('      Компания      |       Модель       | Год выпуска |        КПП      ')
                print('--------------------|--------------------|-------------|-----------------')
                for i in range(numOfDicts):
                    base = pickle.load(database)
                    if base[searchField] == searchWord:
                        print('{:^20}'.format(base['Компания']) + '|' + '{:^20}'.format(base['Модель']) +
                              '|     ' + base['Год выпуска'] + '    |' + '{:^20}'.format(base['КПП']))
                        print('--------------------|--------------------|-------------|-----------------')
                        elementExist = True
                database.close()
                if not elementExist:
                    print('Записи с таким элементом в БД нет')
                elementExist = False
            except KeyError:
                print('Ошибка: такого ключевого поля не существует')
    elif choice == '5':
        if not isBaseCreated:
            print('Ошибка: БД не создана')
        else:
            twoElements = 0
            firstKeyField = input('Введите первое ключевое поле: ')
            firstSearchWord = input('Введите первое ключевое слово: ')
            secondKeyField = input('Введите второе ключевое поле: ')
            secondSearchWord = input('Введите второе ключевое слово: ')
            try:
                database = open(filename, 'rb')
                print('      Компания      |       Модель       | Год выпуска |        КПП      ')
                print('--------------------|--------------------|-------------|-----------------')
                for i in range(numOfDicts):
                    base = pickle.load(database)
                    if base[firstKeyField] == firstSearchWord:
                        twoElements += 1
                    if base[secondKeyField] == secondSearchWord:
                        twoElements += 1
                    if twoElements == 2:
                        print('{:^20}'.format(base['Компания']) + '|' + '{:^20}'.format(base['Модель']) +
                              '|     ' + base['Год выпуска'] + '    |' + '{:^20}'.format(base['КПП']))
                        print('--------------------|--------------------|-------------|-----------------')
                        elementExist = True
                    twoElements = 0
                database.close()
                if not elementExist:
                    print('Записи с такими элементами в БД нет')
                elementExist = False
            except KeyError:
                print('Ошибка: такого ключевого поля не существует')
    elif choice == '6':
        exit()
    else:
        print('Ошибка: введите число от 1 до 6')
