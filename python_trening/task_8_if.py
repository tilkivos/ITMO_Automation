num = 3
    if num >= 0:
     print('Число больше равно 0')
    else:
     print('Число отрицательное')

#
#
# str_1 = 'test'
# str_2 = 'test1'
#
# if str_1 in str_2:
#     print('ДА')
# else:
#     print('НЕТ')
#
#
# num_float = 0
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('Ноль')
# else:
#     print('Число отрицательное')



# def fun(crs: int):
#     if 1 <= crs <= 4:
#         print('Бакалавр')
#     elif 5 <= crs <=6:
#         print('Магистр')
#     elif 7 <= crs <=9:
#         print('Аспирант')
#     else:
#         print('Введите корректный год обучения')
#
# fun(10)


def num(a):
    if a > abs(100):
        print('-')
    else:
        print ('+')

num(-300)