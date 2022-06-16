# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_sec = int(input("Введите время в секундах "))
hours = time_sec // 3600
minutes = (time_sec - hours * 3600) // 60
seconds = time_sec - (hours * 3600 + minutes * 60)
print(f'{time_sec} cекунд в формате чч:мм:сс   {hours:02} : {minutes:02} : {seconds:02}')
