from random import randint
from random import randrange
from random import random

# можно импортировать и напрямую из модуля
# from random import randint

# Генерация целых случайных чисел
print(randint(5, 10))

# from random import randrange
# randrange(start, stop, step)
print(randrange(10, 20, 5))


# Самый простой способ
# получить вещественное число — применить функцию random() без параметров.
print(random())
print(random() * 10)

"""
.random() -Возвращает псевдослучайное число от 0.0 до 1.0
.uniform(<Начало>, <Конец>) -Возвращает псевдослучайное вещественное число в указанныхпределах
.randint(<Начало>, <Конец>) -Возвращает псевдослучайное целое число в указанных пределах
.choice(<Последовательность>) -Возвращает случайный элемент из любой последовательности(строки, списка, кортежа)
.randrange(<Начало>, <Конец>,<Шаг>) -Возвращает случайно выбранное число из последовательности
.shuffle(<Список>) -Перемешивает последовательность элементов
"""