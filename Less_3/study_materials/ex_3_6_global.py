def full_s_calc():
    global r_val, h_val, s_side, s_circle
    r_val = float(input("Укажите радиус: "))
    h_val = float(input("Укажите высоту: "))
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full


s_val = full_s_calc()
print(s_val)
print(s_circle)


# nolocal
def ext_func():
    my_var = 0

    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var

    return int_func


func_obj = ext_func()
print(func_obj)
print(func_obj())
print(func_obj())
print(func_obj())
