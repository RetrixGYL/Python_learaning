my_string=input("Shalom my frendli, wat is yo name?: ")  # input() - функция ввода, просит пользователя самому ввести значение переменной
print("Hello, ",my_string)
print("Lenght your name: ", my_string.__len__())  # .__len__() - метод высчитывает длину
print("YOU: ",my_string.upper())
print("you: ",my_string.lower())
print("you ###: ",my_string.replace(" ","#"))  # .replace() - все через точку, это метод. Данный метод заменяет одно на другое
print("first word your name: ",my_string[0])  # [0] - индекс
print("Last word your name: ",my_string[-1])
