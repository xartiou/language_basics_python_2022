from functools import reduce
from functools import partial


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


print(reduce(my_func, [10, 20, 30]))


def my_func1(param_1, param_2):
    return param_1 ** param_2


new_my_func = partial(my_func1, 2)
print(new_my_func)
print(new_my_func(4))
