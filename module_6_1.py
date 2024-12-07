from time import sleep


class Animal:

    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def info(self):
        print(f'Привет, я {self.name}')
        if self.fed:
            print('Я не голоден')
        else:
            print('Я голодный')
            if self.alive:
                print('И пока что жив')
            else:
                print('И я уже мертв')

    def eat(self, food):
        if food.edible:
            print('Кушает')
            sleep(1)
            print('...')
            sleep(1)
            print('...')
            print(f'{self.name} говорит: Спасибо, я поел')
            self.fed = True
        else:
            print('Кушает')
            sleep(1)
            print('...')
            sleep(1)
            print('...')
            print(f'{self.name} говорит: Спасибо, я умер')
            self.alive = False


class Plant:
    edible = False
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible
#
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# animal_1 = Mammal('Кролик')
# eat_1 = Flower('Сено')
# eat_2 = Plant('Каша')
# animal_1.info()
# animal_1.eat(eat_1)
# animal_1.info()

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)