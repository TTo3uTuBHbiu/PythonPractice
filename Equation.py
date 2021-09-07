# Квадратное уравненеи вида a*x^2 + b*x + c = 0,с возможными комплексными коэфициентами

# импорт math модуля
import cmath

print("В уравнение есть комплексные коэффициенты?")
Ans = input("Ваш ответ(yes/no) = ")

if Ans == 'yes':

    ar = float(input("a(действительная часть) = "))
    ai = float(input("a(мнимая часть) = "))
    br = float(input("b(действительная часть) = "))
    bi = float(input("b(мнимая часть) = "))
    cr = float(input("c(действительная часть) = "))
    ci = float(input("c(мнимая часть) = "))

    a = complex(ar, ai)
    b = complex(br, bi)
    c = complex(cr, ci)

    print(a, b, c)

    # формула дискриминанта
    d = (b ** 2) - (4 * a * c)

    # два решения

    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    # если дискременант ноль,корни совпадают возращаем одно решение

    if d == 0:
        print('Ответ: {0}'.format(sol1))
    else:
        print('Ответы: {0} and {1}'.format(sol1, sol2))

if Ans == 'no':

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # формула дискриминанта
    d = (b ** 2) - (4 * a * c)

    # два решения

    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    # если дискременант ноль,корни совпадают возращаем одно решение

    if d == 0:
        print('Ответ: {0}'.format(sol1))
    else:
        print('Ответы: {0} and {1}'.format(sol1, sol2))