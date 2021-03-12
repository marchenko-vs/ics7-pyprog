import numpy as np

def adjVerticesMat(numberOfLines, numberOfWay):  # Матрица ребер между вершинами
    matrix = np.zeros((numberOfLines, 2))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = inputData[numberOfWay]
            numberOfWay += 1
    return matrix

def sumOfRoutes(numOfDepartment):  # Кол-во смежных вершин
    summary = 0
    for i in range(len(matrixOfVertices)):
        for j in range(len(matrixOfVertices[i])):
            if matrixOfVertices[i][j] == numOfDepartment:
                summary += 1
    return summary

def laplacianMatrix():  # Матрица Кирхгофа
    matrix = np.zeros((numberOfVertices, numberOfVertices))
    numOfEdges = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = sumOfRoutes(i + 1)
            else:
                for k in range(len(matrixOfVertices)):
                    if matrixOfVertices[k][0] == i + 1 and matrixOfVertices[k][1] == j + 1 \
                            or matrixOfVertices[k][0] == j + 1 and matrixOfVertices[k][1] == i + 1:
                        numOfEdges += 1
                matrix[i][j] = -numOfEdges
                numOfEdges = 0
    return matrix

def algComplement(addDet):  # Алгебраическое дополнение
    for i in range(1, len(lapMatrix)):
        for j in range(1, len(lapMatrix[i])):
            addDet[i - 1][j - 1] = lapMatrix[i][j]
    numOfWays = round((np.linalg.det(addMatrix)))
    return str(numOfWays)


with open('input.txt', 'r') as inputFile:
    inputData = list(map(int, inputFile.read().split()))
numberOfVertices = inputData[0]  # Кол-во вершин
numberOfLinks = inputData[1]  # Кол-во ребер
matrixOfVertices = adjVerticesMat(numberOfLinks, 2)
lapMatrix = laplacianMatrix()
addMatrix = np.zeros((numberOfVertices-1, numberOfVertices-1))  # Минор матрицы Кирхгофа
numberOfMethods = algComplement(addMatrix)  # Кол-во остовных деревьев
outputFile = open('output.txt', 'w')
outputFile.write(numberOfMethods)
outputFile.close()
