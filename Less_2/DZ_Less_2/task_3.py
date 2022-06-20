"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
month_list = [['зима', ['12', '1', '2']],
              ['весна', ['3', '4', '5']],
              ['лето', ['6', '7', '8']],
              ['осень', ['9', '10', '11']]
              ]

month_dict = {"зима": ['12', '1', '2'],
              "весна": ['3', '4', '5'],
              "лето": ['6', '7', '8'],
              "осень": ['9', '10', '11']
              }
while True:
    month_num = input('Пожалуйста введите число номера месяца: ')
    if int(month_num) > 12 or int(month_num) == 0:
        print('В году 12 месяцев. Попробуйте еще раз')
        continue
    break

for season, months in month_list:
    if month_num in months:
        print(f'Месяц с номером {month_num} это {season}')

for season, months in month_dict.items():  # .items() - список пар ключ: значение
    if month_num in months:
        print(f'Месяц с номером {month_num} это {season}')
