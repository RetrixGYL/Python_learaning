first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second == third:
    print("Все числа равны, 3")
elif first == second != third or first != second == third or first == third != second:
    print('Два из трех чисел равны, 2')
elif first != second != third:
    print('Все числа разные, 0')
else:
    print("Если вы увидели данное сообщение, то программа дала сбой, обратитесь в тех.поддержку")
