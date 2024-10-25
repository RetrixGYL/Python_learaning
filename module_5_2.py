import time
from time import sleep


class House:
    def __init__(self, name, floors):
        self.name = name
        self.numbers_of_floors = floors

    def go_to(self, new_floor):
        if isinstance(new_floor, int) and self.numbers_of_floors >= new_floor >= 2:
            i = 0
            while i < new_floor:
                i += 1
                print(i)
                sleep(2)
            print(f'Вы приехали на {new_floor}, этаж.')
        elif new_floor == 1:
            sleep(2)
            print('Вы и так на первом этаже...')
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'


house_1 = House('ЖК-Темнолесье', 5)
print(f'Это дом "{house_1.name}", в нём {house_1.numbers_of_floors} этажей.')
house_1.go_to(1)
print(len(house_1))
print(str(house_1))