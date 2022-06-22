"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""


def division_function(num_1, num_2):
    """Функция выполняющая деление"""
    try:
        return f"Результат функции деления : {int(num_1) / int(num_2)}"
    except ZeroDivisionError:  # проверка на ноль делить нельзя
        print('Division by zero is forbidden')
    except ValueError:   # проверка на число
        print('You should enter integers')


print(division_function(input("Введите первое число: "), input("Введите второе число: ")))
