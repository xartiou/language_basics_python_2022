"""
7. Продолжить работу над заданием task_3_6. В программу должна попадать строка из слов, разделенных пробелом.
    Каждое слово состоит из латинских букв в нижнем регистре.
    Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
    Используйте написанную ранее функцию int_func().

"""


def int_func(word):
    return word[0].upper() + word[1:].lower()


s = input().split()

for i, word in enumerate(s):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('error!')
    else:
        s[i] = int_func(word)
print(' '.join(s))

# ******************


# Ещё вариант решения
def int_func():
    for word in input('Enter words with a space (lower latin script):\n').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - only small latin letters!")


int_func()

# ******************


# Вариант решения
def int_func(word):
    latin_char = 'abcdefghijklmnopqrstuvwxyz'
    return word.title() if not set(word).difference(latin_char) else False


words = input('Введите строку на латинице строчными буквами: ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')

# ********************

# Вариант решения
int_func = lambda word: word.title() if word and ascii(word)[1:-1].isalpha() else ''
print(' _ '.join(map(int_func, input('Enter a phrase: ').split())))
