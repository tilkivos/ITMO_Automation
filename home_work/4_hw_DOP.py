#Доп*
#4. В отдельном файле напишите программу с классом Car.
#a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
#b. Напишите пять методов.
#i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
#ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
#iii. Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
#iv. Пятый — присвоение автомобилю цвета.

class Car:


    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def start(self):
        print('Автомобиль заведен')


    def stop(self):
        print('Автомобиль заглушен')


    def car_year(self, year):
        self.year = year
        print(f'Год выпуска {self.year}')


    def car_type(self, type):
        self.type = type
        print(f'Тип автомобиля {self.type}')


    def car_color(self, color):
        self.color = color
        print(f'Цвет автомобиля {self.color}')


auto = Car('Зеленый', 'Volvo', '1976')
print('\n')
print('Первое значение: ' + auto.color, auto.type, auto.year)
print('\n')
auto.start()
auto.stop()
auto.car_year(1984)
auto.car_type('Opel')
auto.car_color('Синий')
print('Измененное значение: ' + auto.color, auto.type, auto.year)