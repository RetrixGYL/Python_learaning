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

    def __eq__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors

    def __le__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors

    def __it__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors = self.numbers_of_floors + value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)


house_1 = House('ЖК-Темнолесье', 10)
house_2 = House('ЖК-Холм_гномов', 20)
house_3 = House('ЖК-Чайный_Гриб', 9)
# print(f'Это дом "{house_1.name}", в нём {house_1.numbers_of_floors} этажей.')
# house_1.go_to(1)

print(str(house_1))
print(str(house_2))
# print(str(house_3))

print(house_1 == house_2) # __eq__

house_1 = house_1 + 10 # __add__
print(house_1)
print(house_1 == house_2)

house_1 += 10 # __iadd__
print(house_1)

house_2 = 10 + house_2 # __radd__
print(house_2)
print(house_1 > house_2) # __gt__
print(house_1 >= house_2) # __ge__
print(house_1 < house_2) # __lt__
print(house_1 <= house_2) # __le__
print(house_1 != house_2) # __ne__