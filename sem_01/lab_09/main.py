def menu():
    print('1. Ввод строки')
    print('2. Настройка шифрующего алгоритма')
    print('3. Шифрование строки, используя шифр Виженера')
    print('4. Расшифровывание строки')
    print('5. Выйти')


menu()
while True:
    choice = input('Введите номер пункта меню: ')
    if choice == '1':
        sourceString = str(input('Введите исходную строку: '))
        print('Исходный текст: {}'.format(sourceString))
        nextChoice = True
    elif choice == '2':
        try:
            keyMain = ''
            i = 0
            keyStr = str(input('Введите ключевую строку: '))
            while i < len(sourceString):
                keyMain += keyStr[i % len(keyStr)]
                i += 1
            print('Ключ: {}'.format(keyMain))
        except NameError:
            print('Ошибка: не введен исходный текст')
    elif choice == '3':
        try:
            encryptedString = ''
            for i in range(len(sourceString)):
                x = (ord(sourceString[i]) + ord(keyMain[i])) % 128
                encryptedString += chr(x)
            print('Зашифрованный текст: {}'.format(encryptedString))
        except NameError:
            print('Ошибка: не настроен алгоритм шифрования')
    elif choice == '4':
        key = str(input('Введите ключ: '))
        if key != keyStr:
            print('Ошибка: ключ неверный')
        else:
            decryptedString = ''
            for j in range(len(encryptedString)):
                y = ((ord(encryptedString[j]) - ord(keyMain[j])) + 128) % 128
                decryptedString += chr(y)
            print('Расшифрованный текст: {}'.format(decryptedString))
    elif choice == '5':
        exit()
    else:
        print('Ошибка: данный пункт не существует')
