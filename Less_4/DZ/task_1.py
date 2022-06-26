"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv


def salary():
    try:
        time, rate, bonus = map(int, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        time = int(input("Введите рабочее время:"))
        rate = int(input("Введите ставку:"))
        bonus = int(input("Введите сумму премии:"))
        print(f"Salary - {time * rate + bonus}")


salary()
