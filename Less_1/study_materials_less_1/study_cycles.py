# num = input("Enter a number 0-9: ")
# print(type(num))
# # input - тип str, перевести в число - int
# num = int(num)
# print(type(num))
#  или
num = int(input("Enter a number 0-9: "))
print()
# цикл
# while num <= 10:
#     print(num)
#     num = num + 1

# бесконечный цикл
# распечатывем нечётные числа меньше 10
i = 0
while True:
    i += 1
    if i >= 10:
        break
    if i % 2 == 0:
        continue
    print(i)
