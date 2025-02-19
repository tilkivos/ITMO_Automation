class Soda:


    def __init__(self, add = None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(f'Газировка и {self.add}')
        else:
            print('Обычная газировка')

borjomi = Soda()
fanta = Soda ('orange')

borjomi.show_my_drink()
fanta.show_my_drink()