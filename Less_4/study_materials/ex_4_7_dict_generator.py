"""
Если в конструкции, определяющей генератор, вместо квадратных скобок указать фигурные, то
результатом работы генератора будет словарь.

"""
print("Генератор словаря")
my_dict = {el: el*2 for el in range(10, 20)}
print(my_dict)
print()
print("Генератор множеств")
my_set = {el**3 for el in range(5, 10)}
print(my_set)
