# Функция
# def my_func - объявление функции
# (arg1, arg2, arg3)  - аргументы функции
# return - показывает что функция должна вернуть

def my_sum(arg_1, arg_2):
    return arg_1 + arg_2


print(my_sum(20, 30))
print(my_sum("abra", "kadabra"))


# Функция может содержать вложенные функции и возвращать объекты различных типов (списки,
# словари, функции).

def ext_func(var_1):
    def int_func(var_2):
        return var_1 + var_2

    return int_func


f_obj = ext_func(200)  # f_obj - функция

print(f_obj(300))


# Оператор return не используется, если
# функция выполняет некоторые действия, но не возвращает значения. В этом случае возвращаемое
# значение — None.

def my_func():
    pass


print(my_func())
