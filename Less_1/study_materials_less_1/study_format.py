# %s - строка
# %d - число
age = 29
name = "Name"

print("Your name %s, your age %d " % (name, age))
print("Your name {}, your age {} " .format(name, age))
print("Your name {}, your age {} " .format(age, name))  # форматирует по порядку не основываясь на тип

print(f"Your name {name}, your age {age} ")

print(f"{10 / 3:.2}")  # 3.3
print(f"{10 / 3:.2f}")  # 3.33
