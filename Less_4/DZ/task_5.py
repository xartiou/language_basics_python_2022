"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы).
    Необходимо получить результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce().

"""

from functools import reduce
# reduce(function, iterable[, initializer])


def mul_list(el_1, el_2):
    return el_1 * el_2


uniq_list = [el for el in range(2, 60, 2)]
print(f"List:\n{uniq_list}\nMultiplication of numbers:\n{reduce(mul_list, uniq_list)}")


# вариант с lambda
print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))

# вариант с mul()
# operator.mul(a, b) - Функция возвращает a * b, для чисел a и b.

from operator import mul

print(reduce(mul, [x for x in range(100, 1001, 2)]))
