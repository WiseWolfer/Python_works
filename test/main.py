



matrix = []
columns = int(input("Число столбцов: "))
rows = int(input("Число строк: "))
for i in range(rows):
    elem = []
    for j in range(columns):
        elem.append(int(input("Числа в матрице: ")))
    matrix.append(elem)
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()
