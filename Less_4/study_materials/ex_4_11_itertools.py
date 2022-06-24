from itertools import count
from itertools import cycle

# стартовый параметр
for el in count(7):
    if el > 15:
        break
    else:
        print(el)

# итератор для формирования бесконечного цикла набора значения
с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1

# Для выполнения операций перемещения по итератору применяется функция next.

progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

"""
.count (<Начало>, <Шаг>) Возвращает равномерно распределённые переменные, начиная
                            с числа — стартового параметра. Можно указать параметр шага.
.cycle (<Итерируемый объект>) Итератор, создающий бесконечный цикл поочерёдного вывода
                                неких символов или чисел.
.repeat (<Объект>, <Количество повторений>) Итератор, осуществляющий повторение объекта, переданного в
                                            качестве первого параметра в функцию.
.combinations (<Объект>, <Количество значений>) Функция комбинирования элементов последовательности.
                                                Принимает два аргумента: объект и количество значений,
                                                которые должны присутствовать в каждой комбинации.
.combinations_with_replacement(<Объект>, <Количество значений>) Модифицированный вариант предыдущей функции.
                                                                Предоставляет программе возможность делать выборку из
                                                                отдельных элементов с учётом их порядка. Комбинации могут
                                                                состоять из повторяющихся элементов.
.permutations (<Объект>, <Количество значений>) Сходна с предыдущей функцией, но в текущей не допускается
                                                размещение идентичных элементов в одной комбинации.
.product (<Массив данных>) Принимает в качестве параметра массив данных, объединяющий
                           несколько групп значений. Позволяет получить из введённого
                           набора чисел и символов новую совокупность групп во всех возможных вариациях.
                           
"""