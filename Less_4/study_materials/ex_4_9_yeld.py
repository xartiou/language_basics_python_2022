generator = (param * param for param in range(5))

for el in generator:
    print(el)

# print(next(generator))


# yeld
def generator():
    """
    Такой механизм может быть полезен в том случае, когда функция возвращает большой объём
    данных. Но использовать их нужно только единожды. При вызове функции с оператором yield
    функция не выполняется. Она возвращает объект-генератор, с которым далее можно выполнять
    нужные действия.

    """
    for el in (10, 20, 30):
        yield el


g = generator()
print(g)
for el in g:
    print(el)
