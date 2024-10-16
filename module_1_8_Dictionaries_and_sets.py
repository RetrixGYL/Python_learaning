my_dict = {"Rex": 2344, "Shmeks": 1455, "Geks": 31311}
print(my_dict)
print(my_dict["Rex"])
print(my_dict.get("Kio"))
my_dict["Meh"] = 666
my_dict["Keh"] = 669  # Или метод update, чтобы добавить сразу несколько пар ключ-значение
print(my_dict)
kek = my_dict.pop("Meh")
print(my_dict)
# Множества
my_set = {1, 3, 3, 3, 1, 1}
print(my_set)
(my_set.add(7))
(my_set.add(9))
print(my_set)
(my_set.remove(3))
print(my_set)
print(kek)

#  Дополнение: в функции get() у словаря можно передать вторым аргументом сообщение, которое будет выводиться при отсутствии указанного ключа вместо None
#  Например:
#  my_dict.get("Kio", "Указанный ключ не найден")
