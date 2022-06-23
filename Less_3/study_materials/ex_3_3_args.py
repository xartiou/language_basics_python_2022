# Аргументы функций
# Функция может принимать любое количество параметров или не принимать их вообще. Параметры
# могут быть позиционные и именованные, обязательные и необязательные.

# позиционные параметры
def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))


# именованные параметры
def second_func(var_2, var_1, var_3):
    print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")


second_func(var_1=10, var_2=20, var_3=30)


# обязательные параметры
def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))


# var_2 и var_3 - необязательные параметры
def second_func(var_1, var_2=20, var_3=30):
    return var_1 + var_2 + var_3


print(second_func(10))


# Функция может принимать неопределённое число позиционных параметров. В этом случае при
# описании функции используется конструкция *args.
def my_func(*args):
    return args


print(my_func(10, "text_1", 20, "text_2"))


# Функция может принимать и неопределённое число именованных параметров. Тогда используется
# конструкция **kwargs.
def my_func(**kwargs):
    return kwargs


print(my_func(el_1=10, el_2=20, el_3="text"))
