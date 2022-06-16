# итерация
print("итерация")
for i in "2316":
    print(i)

print("итерация list")

my_list = [1, 2, 3, 4]
print(my_list)
for j in my_list:
    print(j + 4)

print("итерация dict")
my_dict = {"a": 1, "b": 2, "c": 3}
for k in my_dict:
    print(k)

print("итерация dict по ключу и значению")
my_dict = {"a": 1, "b": 2, "c": 3}
for k, v in my_dict.items():
    print(k, v)

print("итерация range")
for i in range(0, 5, 2):
    print(i)
