"""
Функция argv модуля sys возвращает список аргументов командной строки, передаваемых скрипту Python.
Выражение argv[0] - это имя скрипта и зависит от операционной системы, является ли это полный путь или нет.

"""
from sys import argv


script_name, first_param, second_param, third_param = argv
print("Имя скрипта: ", script_name)
print("Параметр 1: ", first_param)
print("Параметр 2: ", second_param)
print("Параметр 3: ", third_param)

