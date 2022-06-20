"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
# quantity_goods = ""
# goods_dict = ""
# product_name = ""
# product_price = ""
# quantity = ""
# unit_counting = ""
from pprint import pprint

i = 1

# создаем структуру товаров
goods = []
quantity_goods = int(input('Сколько товаров хотите ввести? '))
for _ in range(quantity_goods):
    product_name = input('Введите название товара ')
    product_price = int(input('Введите цену '))
    quantity = int(input('Введите количество '))
    unit_counting = input('Введите единицы измерения ')
    goods.append((i, {'название': product_name, 'цена': product_price, 'количество': quantity, 'ед': unit_counting}))
    i += 1

pprint(goods)
# создаем словарь, в котором каждый ключ — характеристика товара,
goods_dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
for good in goods:
    goods_dict['название'].append(good[1]['название'])
    goods_dict['цена'].append(good[1]['цена'])
    goods_dict['количество'].append(good[1]['количество'])
    if good[1]['ед'] not in goods_dict['ед']:
        goods_dict['ед'].append(good[1]['ед'])
pprint(goods_dict)


# вариант решения 2

# goods = []
# features = {'название': '', 'цена': '', 'количество':'', 'единица измерения': ''}
# analytics = {'название': [], 'цена': [], 'количество':[], 'единица измерения': []}
# num = 0
# while True:
#     if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
#         break
#     num += 1
#     for f in features.keys():
#         pro = input(f'Введите значение свойства "{f}": ')
#         features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
#         analytics[f].append(features[f])
#     goods.append((num, features))
#     print(f'\nСтруктура товаров\n{goods}')
#     print(f'\nТекущая аналитика по товарам: \n {"*" * 30}')
#     for key, value in analytics.items():
#         print(f'{key[:25]:>30}: {value}')
#     print('*' * 30)