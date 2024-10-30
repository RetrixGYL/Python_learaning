from time import sleep

class House:

    houses_history = []

    def __new__(cls, *args):

        new_houses = args[0]
        cls.houses_history.append(new_houses)
        return super().__new__(cls)

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

    def __it__(self, other): # ПОЧЕМУ __it__, окрашен ГОЛУБЫМ, в отличие от всех остальных методов(p.s. все остальные филетовым, он особенно одарённый???)
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

    def __del__(self):
        print(f'Даже такая великая крепость, как {self.name} пала, под натиском свирепых драконов...\nНо мы сохраним память о нем в древних свитках.')


h_1 = House('ЖК-Темнолесье', 10)
h_2 = House('ЖК-Холм_гномов', 20)
h_3 = House('ЖК-Чайный_Гриб', 9)


print(f'Это крепость "{h_1.name}", в ней {h_1.numbers_of_floors} этажей.')
h_1.go_to(4)


print(House.houses_history)
del h_2
print(House.houses_history)
stop = input('Stooop!')

