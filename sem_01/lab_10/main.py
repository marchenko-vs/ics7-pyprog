def menu():
    print(' ' * 25 + 'Меню\n1. Выравнивание текста по левому краю.\n'
          '2. Выравнивание текста по правому краю.\n'
          '3. Выравнивание текста по ширине.\n'
          '4. Удаление заданного слова.\n'
          '5. Замена одного слова другим во всем тексте.\n'
          '6. Вычисление арифметического выражения.\n'
          '7. Найти предложение с максимальным количеством слов,\n'
          'начинающихся на заданную букву.\n'
          '8. Выйти')


def lengthOfStr():
    biggestLength = len(text[0])
    for i in range(len(text)):
        if len(text[i]) > biggestLength:
            biggestLength = len(text[i])
    return biggestLength


def justifiedAlignment(text):
    textCopy = text.copy()
    maxLength = len(textCopy[0])
    for i in range(len(textCopy)):
        if len(textCopy[i]) > maxLength:
            maxLength = len(textCopy[i])
    lengthOfStr = 0
    numOfWords = 0
    j = 0
    for i in range(len(textCopy)):
        addArray = textCopy[i].split(' ')
        for j in range(len(addArray)):
            numOfWords += 1
            for k in range(len(addArray[j])):
                lengthOfStr += 1
        if numOfWords == 0 or numOfWords == 1:
            spaces = 0
            additional = 0
        else:
            spaces = (maxLength - lengthOfStr) // (numOfWords - 1)
            additional = (maxLength - lengthOfStr) % (numOfWords - 1)
        for j in range(len(addArray)):
            if additional == 0:
                if j < len(addArray) - 1:
                    print(addArray[j] + ' ' * spaces, end='')
                else:
                    print(addArray[j])
            else:
                if j < len(addArray) - 1:
                    if additional > 0:
                        print(addArray[j] + ' ' * (spaces + 1), end='')
                        additional -= 1
                    else:
                        print(addArray[j] + ' ' * spaces, end='')
                else:
                    print(' ' * additional + addArray[j])
        lengthOfStr = 0
        numOfWords = 0


def deleteWord(mainText, wordToDelete):
    j = 0
    for i in range(len(mainText)):
        helpArray = mainText[i].split()
        while j < len(helpArray):
            if helpArray[j] == wordToDelete or helpArray[j] == wordToDelete + ',' or helpArray[j] == wordToDelete + '.':
                helpArray.remove(helpArray[j])
                j += 1
            j += 1
        mainText[i] = ' '.join(helpArray)
        j = 0
        print(mainText[i])


def replaceWords(text, wordToReplace, newWord):
    j = 0
    for i in range(len(text)):
        helpArray = text[i].split()
        while j < len(helpArray):
            if helpArray[j] == wordToReplace or helpArray[j] == wordToReplace + ',':
                helpArray[j] = newWord
            j += 1
        text[i] = ' '.join(helpArray)
        j = 0
        print(text[i])


def plusOrMinus(expression):
    i = 0
    while i < len(expression):
        if expression[i] == "+":
            expression[i] = float(expression[i - 1]) + float(expression[i + 1])
            expression.pop(i - 1)
            expression.pop(i)
            i -= 1
        elif expression[i] == "-":
            expression[i] = float(expression[i - 1]) - float(expression[i + 1])
            expression.pop(i - 1)
            expression.pop(i)
            i -= 1
        i += 1
    return expression


def multOrDiv(expression):
    i = 0
    while i < len(expression):
        if expression[i] == "/":
            expression[i] = float(expression[i - 1]) / float(expression[i + 1])
            expression.pop(i - 1)
            expression.pop(i)
            i -= 1
        elif expression[i] == "*":
            expression[i] = float(expression[i - 1]) * float(expression[i + 1])
            expression.pop(i - 1)
            expression.pop(i)
            i -= 1
        elif expression[i] == "%":
            expression[i] = float(expression[i - 1]) % float(expression[i + 1])
            expression.pop(i - 1)
            expression.pop(i)
            i -= 1
        elif expression[i] == "//":
            expression[i] = float(expression[i - 1]) // float(expression[i + 1])
            expression.pop(i - 1)
            expression.pop(i)
            i -= 1
        i += 1
    return plusOrMinus(expression)


def powerOrBrackets(expression):
    expression = expression.split()
    i = 0
    while i < len(expression):
        if expression[i] == "**":
            expression[i] = float(expression[i - 1]) ** float(expression[i + 1])
            expression.pop(i - 1)
            expression.pop(i)
            i -= 1
        i += 1
    return multOrDiv(expression)


def solveExpression(expression):
    flag = False
    new_string = ""
    for i in expression:
        if i == ")":
            flag = False
        if flag:
            new_string += i
        if i == "(":
            flag = True
    if new_string != "":
        a = powerOrBrackets(new_string)[0]
        expression = expression.replace("(" + new_string + ")", str(a))
    return powerOrBrackets(expression)[0]


def findSolution(mainText):
    for i in range(len(mainText)):
        addArray = mainText[i].split(' ')
        count = 0
        solution = ''
        j = 0
        element = 0
        while j < len(addArray):
            for k in range(len(addArray[j])):
                if 47 < ord(addArray[j][k]) < 58 or addArray[j][k] == '-' or \
                        addArray[j][k] == '+' or 
                        addArray[j][k] == '*' or addArray[j][k] \
                        == '/' or addArray[j][k] == '%' or \
                        addArray[j][k] == '(' or addArray[j][k] == ')':
                    count += 1
                if count == len(addArray[j]):
                    solution += addArray[j]
                    solution += ' '
                    addArray.pop(j)
                    j -= 1
            count = 0
            j += 1
            if solution == '':
                element += 1
        if solution != '':
            answer = float(solveExpression(solution))
            if answer % 1 != 0:
                addArray.insert(element, str(answer))
            else:
                addArray.insert(element, str(int(answer)))
        mainText[i] = ' '.join(addArray)
        element = 0
    for i in range(len(mainText)):
        print(mainText[i])


def maxNumOfWords(mainText):
    firstLetter = str(input('Введите букву: '))
    j = 0
    count = 0
    maxNum = 0
    for i in range(len(mainText)):
        helpArray = mainText[i].split()
        while j < len(helpArray):
            if helpArray[j][0].lower() == firstLetter.lower():
                count += 1
            j += 1
        if count > maxNum:
            maxNum = count
            numOfSentence = i + 1
        count = 0
        j = 0
    if maxNum == 0:
        print('В тексте нет подходящих слов'.format(firstLetter))
    else:
        print('В {} предложении слова, начинающиеся на букву "{}" '
              'встречаются {} раз'.format(numOfSentence, firstLetter, maxNum))


text = ['Окидываю']
menu()
while True:
    choice = input('Введите номер пункта меню: ')
    if choice == '1':
        for i in range(len(text)):
            print(text[i])
    elif choice == '2':
        maxLength = lengthOfStr()
        for i in range(len(text)):
            spaceLength = maxLength - len(text[i])
            print(' ' * spaceLength + text[i])
    elif choice == '3':
        justifiedAlignment(text)
    elif choice == '4':
        wordToDel = str(input('Введите слово, которое нужно удалить: '))
        deleteWord(text, wordToDel)
    elif choice == '5':
        wordToReplace = str(input('Заменить слово: '))
        newWord = str(input('Новое слово: '))
        replaceWords(text, wordToReplace, newWord)
    elif choice == '6':
        findSolution(text)
    elif choice == '7':
        maxNumOfWords(text)
    elif choice == '8':
        exit()
    else:
        print('Ошибка: введите номер от 1 до 8')
