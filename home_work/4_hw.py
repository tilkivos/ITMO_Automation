#1. создайте класс прямоугольника.
#a. атрибуты - прямоугольнику можно задать ширину и высоту
#b. методы - реализуйте 2 метода:
#i. расчет площади прямоугольника
#ii. расчет периметра прямоугольника
#c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.
print('\n')
print('Задача №1')


class Rectangle:


    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)


rec_1 = Rectangle(2, 4)
rec_2 = Rectangle(5, 5)
rec_3 = Rectangle(2.5, 10)

print(f'Площадь прямоугольника равна {rec_1.area()}, периметр прямоугольника равен {rec_1.perimeter()}')
print(f'Площадь прямоугольника равна {rec_2.area()}, периметр прямоугольника равен {rec_2.perimeter()}')
print(f'Площадь прямоугольника равна {rec_3.area()}, периметр прямоугольника равен {rec_3.perimeter()}')


#2.Cоздайте класс Math.
#a. Создайте два атрибута — a и b.
#b. Напишите методы
#i. addition — сложение,
#ii. multiplication — умножение,
#iii. division — деление,
#iv. subtraction — вычитание.
#При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

print('\n')
print('Задача №2')

class Math:


    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            print ('Нельзя делить на ноль!')
        else:
            return self.a / self.b


    def subtraction(self):
        return self.a - self.b


parameter = Math(10, 3)
print(f'Результат сложения {parameter.a} и {parameter.b} равен {parameter.addition()}')
print(f'Результат умножения {parameter.a} и {parameter.b} равен {parameter.multiplication()}')
print(f'Результат деления {parameter.a} и {parameter.b} равен {parameter.division()}')
print(f'Результат вычитания {parameter.a} и {parameter.b} равен {parameter.subtraction()}')


