
orig_password = "12345"
password = input("Enter password: ")

# 1 вариант ветвления
# if password == orig_password:
#     print("OK")
#
# if password != orig_password:
#     print("No OK")

# 2 вариант ветвления
# if password == orig_password:
#     print("OK")
# else:
#     print("No OK")

# # 3 вариант ветвления
# if password == orig_password:
#     print("OK")
#     name = input()
#     if name == "admin":
#         print("Hello, admin")
#     else:
#         print("Hello, hacker")
# else:
#     print("No OK")

# 4 вариант ветвления
color = "red"

if color == "white":
    print(123)
elif color == "black":
    print(124)
elif color == "blue":
    print(125)
else:
    print("I don't know this color")
