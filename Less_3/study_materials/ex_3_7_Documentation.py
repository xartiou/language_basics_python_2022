# Однострочники
def get_path():
    """Возвращает путь до директории."""
    global my_path
    if my_path: return my_path


def my_func(param_1, param_2):
    """Выполняет обработку параметров и возвращает кортеж."""


# Многострочники
def my_func_1(p_1=0, p_2=1):
    """Возвращает частное от деления.

    Именованные параметры:
    p_1 -- делимое (по умолчанию 0.0)
    p_2 -- делитель (по умолчанию 1.0)

    """
    return p_1/p_2