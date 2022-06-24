import ex_4_3_my_function


ex_4_3_my_function.show_msg()
print(ex_4_3_my_function.simple_calc())

print("ещё вариант")

from ex_4_3_my_function import show_msg
from ex_4_3_my_function import simple_calc


show_msg()
print(simple_calc())
