class Vehicle:
    __COLOR_VARIANTS = ['black', 'silver', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        # self.__engine_power()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self):
        choice_ = input(f'Выберите в какой цвет прокрасить автомобиль {Vehicle.__COLOR_VARIANTS}: ')
        choice_low = choice_.lower()
        print(f'Вы выбрали: {choice_low}')
        if choice_low in Vehicle.__COLOR_VARIANTS:
            print(f'Цвет сменился на {choice_low}, с вас 110к')
            self.__color = choice_low
        else:
            print(f'Цвета "{choice_low}" в ассортименте нет, приходите позже')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


# mark = Vehicle('Gay', '2jz', 55, 'Black')
# #mark.get_model()
# #mark.get_horsepower()
# #mark.get_color()
# mark.print_info()
# mark.set_color()
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color()
vehicle1.set_color()
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
