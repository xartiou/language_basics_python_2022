# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил path_first_day километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее max_path километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

path_first_day = int(input('Введите начальный километраж пробежки : '))
print('Каждый день увеличивайте ваш километраж на 10%')
max_path = int(input('Введите максимальный километраж пробежки : '))
day_run = 1
while path_first_day < max_path:
    path_first_day += (path_first_day / 100) * 10
    day_run += 1
print(f'Вы достигните результата на {day_run} день')
