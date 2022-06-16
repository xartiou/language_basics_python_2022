# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = 'Masha'
print(name)
print()
surname = 'Vladimirova'
print(surname)
print()
quantity = 15
quantity_1 = quantity + 10.5
quantity_total = quantity + quantity_1
print(quantity_total)
print(type(quantity_total))
driver_1 = input('Введите имя: ')
mileage_l = int(input('Введите суточный пробег: '))
print(driver_1, 'проехал', mileage_l, 'км')
car_model = input('Введите марку Вашего авто: ')
liter_mil = (8 / 100) * mileage_l
print(driver_1, 'на', car_model, 'израсходовал', liter_mil, 'литров бензина.')

