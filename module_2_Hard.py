import time
def wait_():
    time.sleep(2.5)
    print('...')
n = int(input('Введите число, которое вы видите на первой вставке(3..20): '))
print('...')
wait_()
wait_()
num1 = list(range(1, n))
num2 = list(range(1, n))
pairs = []
result = ''
for i in num1:
    for j in num2:
        n1 = i
        n2 = j
        if n1 >= n2:
            continue
        else:
            multiple = n % (n1 + n2)
            if multiple == 0:
                pairs.append([n1, n2])
                result = result + str(n1) + str(n2)
print('Пары чисел', *pairs)
print('Пароль найден: ', result,'\nДля открытия ворот, вам необходимо вписать его во вторую вставку')

#Можно переделать под import random, за место input, но мне кажется так логичнее