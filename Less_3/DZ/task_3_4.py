"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
    Необходимо выполнить возведение числа x в степень y.
    Задание необходимо реализовать в виде функции my_func(x, y).
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

"""


def my_func(x, y):
    """Функция возводит в степень отрицательного числа"""
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает только с действительными x и целыми y')
        return
    if x <= 0 or y >= 0:
        print('Программа работает только с положительными x и отрицательными y')
        return
    return x ** y


print(my_func(2, -5))
print(round(my_func(2, -5), 4))


# ***********************


# Ещё вариант решения
def pow_negative(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает только с действительными x и целыми y')
        return
    if x <= 0 or y >= 0:
        print('Программа работает только с положительными x и отрицательными y')
        return
    result = 1
    for _ in range(abs(y)):
        result /= x
    return f'Результат возведения x в степень y: {round(result, 6)}'


print(pow_negative(input('Введите действительный положительный х: '), input('Введите целый отрицательный у: ')))


# ********************************

# Вариант решения с рекурсией
def my_func(x, y):
    return 1 if y == 0 else my_func(x, y + 1) * 1 / x


print(round(my_func(int(input('Введите действительный положительный х: ')),
                    int(input('Введите целый отрицательный у: '))), 10))
