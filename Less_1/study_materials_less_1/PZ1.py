# 1.Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.
a = 'Hi,'
b = 'user'
print(a, b)
number1 = int(input('Enter a number: '))
number2 = int(input('Enter another number: '))
print(f'You entered {number1} and {number2}')
word = input('Enter a word: ')
print(f'{word} is nice')

# 2.Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time_in_seconds = int(input())
hours = time_in_seconds // 60 // 60
time_in_seconds = time_in_seconds - 60 * 60 * hours
minutes = time_in_seconds // 60
seconds = time_in_seconds - 60 * minutes
print(f'{hours:02}:{minutes:02}:{seconds:02}')

# Вариант решения
sec = int(input("Введите количество секунд для конвертации в формате чч.мм.сс.: "))
print(f"{sec // 3600:.0f}:{(sec // 60) % 60:.0f}:{sec % 60:.0f}")

# Вариант решения
while True:
    number_seconds = input("Введите количество секунд: ")
    if number_seconds.isdigit():
        number_seconds = int(number_seconds)
        break
    print("Необходимо ввести число")

print(f"{number_seconds // 3600:0{2}}:{(number_seconds % 3600) // 60:0{2}}:{(number_seconds % 3600) % 60:0{2}}")

# Вариант решения
sec = int(input('Введите время в секундах: '))
min = sec // 60
hr = min // 60
print('%02d:%02d:%02d' % (hr, min % 60, sec % 60))

# Вариант решения
import datetime

sec = int(input())
print(datetime.time(sec // 3600, (sec % 3600) // 60, (sec % 3600) % 60))

# Вариант решения
import time

sec_numb = int(input())
print(time.strftime('%H:%M:%S', time.gmtime(sec_numb)))

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = input('Enter a number: ')

while n < '0':
    print('The number should be greater than 0! Please try again.')
    n = input('Please enter a number greater than 0: ')

print(int(n) + int(n + n) + int(n + n + n))

# Вариант решения
n = input("Enter n ")
print(int(n) + int(n * 2) + int(n * 3))

# Вариант решения
n = input("Введите число: ")
print(int(n) + int(f"{n}{n}") + int(f"{n}{n}{n}"))

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
num = int(input('Введите целое положительное число'))
n = num  # переменная для хранения оставшейся части числа
max = n % 10  # текущий максимум
while n:  # выполняем цикл, пока отсечения цифр не обнулят число
    a = n % 10  # определяем последнюю цифру
    if a > max:  # сравниваем её с текущим максимумом
        max = a  # обновляем максимум
        if max == 9:  # необязательно, для экономии времени выполнения, нет цифр больше 9
            break
    n = n // 10  # отсекаем от числа последнюю цифру
print(f'Наибольшая цифра в {num} равна {max}')


# Вариант решения с рекурсией
def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > num % 10 else num % 10


print(f'The largest number is: {num_max(int(input("Enter a number: ")))}')

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
income = int(input('Введите выручку '))
expense = int(input('Введите издержки '))
net_income = income - expense
if net_income > 0:
    print('Фирма работает с прибылью')
    print(f'Рентабельность выручки: {net_income / income: .2f}')
    people = int(input('Введите численность сотрудников '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {net_income / people: .2f}')
elif net_income < 0:
    print('Фирма работает с убытком')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня. Например: a = 2, b = 3. Результат: 1-й день: 2 2-й день: 2,2 3-й день:
# 2,42 4-й день: 2,66 5-й день: 2,93 6-й день: 3,22 Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
a = int(input())
b = int(input())
days = 1
while a < b:
    a = a * 1.1
    days = days + 1
print(days)

# вариант решения
while True:
    a = float(input('Стартовый результат: '))
    b = float(input('Финальный результат: '))
    if a < 0 or b < 0:
        print('Введите положительные числа')
    else:
        days = 1
        while a < b:
            a += a * 0.1
            days += 1
        print(f'Спортсмен добьётся результата за {days} дней.')
        break
