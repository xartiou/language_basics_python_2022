"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
number_of_elements = int(input("Введите число элементов списка : "))
completed_list = []
for n in range(number_of_elements):
    completed_list.append(input("Введите элемент списка : "))
print(completed_list)
for i in range(1, len(completed_list), 2):
    completed_list[i - 1], completed_list[i] = completed_list[i], completed_list[i - 1]
print(completed_list)


