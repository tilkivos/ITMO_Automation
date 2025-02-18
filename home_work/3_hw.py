#2. Функция на вход получает два произвольных числа.
# Вывести в консоль наибольшее из чисел.

def fun_1(a: float, b: float):
    print(max(a, b))

fun_1(5,187.8)


#3. Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135,
# иначе вывести на экран “No”

def fun_2(a: float, b: float):
    if abs(a - b) == 135:
        print('Yes')
    else:
        print('No')

fun_2(100, -35)


#4. Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)

def fun_3(a: int):
    if a == 1 or a == 2 or a == 12:
        print('Зима')
    elif a in [3, 4, 5]:
        print('Весна')
    elif 6 <= a <=8:
        print('Лето')
    elif a in [9, 10, 11]:
        print('Осень')
    else:
        print('Введите число от 1 до 12')

fun_3(12)


#5. Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”;

def fun_4(a: float, b: float, c: float):
    if a > 10 and b > 10 and c >10:
        print('yes')
    else:
        print('no')

fun_4(11, 9, 156.9)

#Доп *
#6. Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.

def fun_5(a_list: list):
    n = 0
    for elem in a_list:
        if elem > 0:
            n = n+1
        else:
            n = n
    print('Количество положительных чисел = ', n)

fun_5((-1, 2, 3, 4, -5))




#7. Функция на вход получает 2 переменные.
#а. Кол-во лет (int)
#b. Кол-во месяцев (int)
#Вывести в консоль количество дней за это время.
#Считать, что в каждом месяце 29 дней.

def fun_6(y: int, m: int):
    if y >= 0 and 0 <= m <= 12:
        print(29 * m + 29 * 12 * y)
    else:
        print('Введите год больше равен 0, месяц от 0 до 12')

fun_6(0,4)