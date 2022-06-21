# Анонимные функции (lambda)

my_func = lambda p_1, p_2: p_1 + p_2
print(my_func(2, 5))
print(my_func("abra", "kadabra"))

print((lambda p_1, p_2: p_1 + p_2)(2, 5))
print((lambda p_1, p_2: p_1 + p_2)("abra", "kadabra"))

new_func = lambda *args: args
print(new_func(10, 20, 30, 40))


# *************
def named_func(param):
    return param ** 0.5


print(named_func(100))


square_rt = lambda param: param ** 0.5
print(square_rt(100))
