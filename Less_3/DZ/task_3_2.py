"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.

"""


def user_data(**kwargs):
    """Функция принимающая данные пользователя"""
    return ' '.join(kwargs.values())  # выводим значения через пробел


print(user_data(name=input('Enter your name: '), surname=input('Enter your surname: '),
                year_birth=input('Enter you year of birth: '),
                city=input('Enter your city: '), email=input('Enter your email: '),
                phone=input('Enter your phone number:')))
