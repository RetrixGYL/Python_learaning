import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, name, _cords=None):
        if _cords is None:
            _cords = [0, 0, 0]

        self._cords = _cords
        self.speed = speed
        self.name  = name

    def info(self):
        print(f'Халло, я {self.name}')
        print(f'Мой уровень опасности: {self._DEGREE_OF_DANGER}')
        print(f'Я сейчас нахожусь по координатам {self._cords}') # аналог get_cords(self), который выводит координаты

    def move(self, dx, dy, dz):
        ground_ = self._cords[2]
        check_  = ground_ + dz
        if check_ >= 0:
            self._cords[0] = int(self._cords[0] + dx * self.speed)
            self._cords[1] = int(self._cords[1] + dy * self.speed)
            self._cords[2] = int(self._cords[2] + dz * self.speed)
            print(f'Я сдвинулся в координаты {self._cords}')
        else:
            print(f'Он кричал: -Нет, Мама! Я не хочу в "Затекстурие"... :((')

    def attack(self):
        if Animal._DEGREE_OF_DANGER < 5:
            print('Я мирный :)')
        else:
            print('Я не в опасности! Я и есть опасность >:]')

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random_ = random.randint(1, 4)
        if random_ > 1:
            print(f"Здесь целых {random_} egg's, специально for You! <3")
        else:
            print(f'Здесь {random_} egg, специально for You! <3')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= int(dz / 2 * self.speed)
        print(f'Я нырнул и переместился в координаты {self._cords}')


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    pass

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Click-clack'
    def speak(self):
        print(f'{self.name} говорит: -"{self.sound}".')



# goat = Animal(7, 'Карлик-Утконос')
# goat.info()
# goat.move(7, 5, 5)
# goat.info()
# goat.attack()
# voron = Bird(4, 'Черная Ворона')
# voron.lay_eggs()
# kit = AquaticAnimal(2, 'Кит')
# sneak = PoisonousAnimal(1, 'Гадюка')
# sneak.info()
# kit.info()
# kit.dive_in(5)
db = Duckbill(10, 'Гига-Утконос')
print(Duckbill.beak)
print(Duckbill.live)
db.speak()
db.move(1, 2, 3)
db.info()
db.dive_in(6)
db.lay_eggs()