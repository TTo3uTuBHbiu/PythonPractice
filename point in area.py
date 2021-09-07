import math

x = float(input("введите x:"))
y = float(input("введите y:"))

if (((x - 17) ** 2) + ((y - 5) ** 2)) < 9:
    print('Дерево')
elif (((x - 11) ** 2) + ((y - 17) ** 2)) < 4:
    print('Дым 1')

elif (((x - 14) ** 2) + ((y - 20) ** 2)) < 4:
    print('Дым 2')

elif (9 < x < 10) and (29 - 2*x < y < 15):
    print('Труба')

elif (y < 3.5 + 1.5 * x) and (y < 24.5 - 1.5 * x) and (8 < y):
    if(((x - 7) ** 2) + ((y - 10) ** 2)) < 1:
        print('Окно')
    else:
        print('Крыша,которая едет')

elif (3 < x < 10) and (0 < y < 8):
    if (5 < x < 9) and (5 < y < 7):
        print('Квадратное окно')
    if (5 < x < 7) and (0 < y < 4):
        print('Дверь')
    else:
        print('Фундамент')

else:
    print('все остальное')
