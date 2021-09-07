import random

m = round(random.uniform(2, 6))
print('Количество строк - ', m)

n = round(random.uniform(2, 6))
print('Количество столобцов - ', n)

# создание нулевой  матрицы
a = [[0] * n for i in range(m)]

# заполнение рандомными числами

for i in range(m):
    for j in range(n):
        a[i][j] = round(random.uniform(0, 100))

# вывод матрицы

for i in range(m):
    for j in range(n):
        if j != (n - 1):
            print(a[i][j], ",", end='')
        else:
            print(a[i][j])

# сумма элементов с четной суммой индексов

sum = 0

for i in range(m):
    for j in range(n):
        if (i + j) % 2 == 0:
            sum += a[i][j]
print(sum)


