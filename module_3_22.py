def send_email(message=0, recipient=0, sender = "university.help@gmail.com"):
    message = message_1
    recipient = recipient_1
    check_1 = recipient.find(".ru")
    check_2 = recipient.find("@")
    if check_1 > 0:
        check_1 = True
    else:
        check_1 = False
    score_ = 1
    while score_ == 1:
        if check_1 and check_2:
            print(f"Вы успешно отправили сообщение '{message}', на почту '{recipient}'.")
            score_ += 1
        else:
            print('Ошибка!\nНеверно указан домен или нет знака "@"\n(.ru/.com/.ru)')
            recipient = input("Укажите получателя заново: ")
            continue

i = 1
while i > 0:
    print("Бобро пожаловать в почту, вы хотите написать кому-то сообщение?")
    answer_1 = input("y/n: ")
# print(answer_1)
    check_0 = answer_1.find("y")
# print(check_0)
    if check_0 >= 0:
        recipient_1 = input("Отлично, ваша почта по умолчанию: university.help@gmail.com\nВведите почту получателя: ")
        message_1 = input("Введите сообщение для отправки: ")
        break
    else:
        print("Ну и ладно...")
        continue
send_email()
print("кек")










# def send_email(message, recipient, sender = "university.help@gmail.com"):
#     print(f"Вы успешно отправили сообщение '{message}', на почту '{recipient}'.")

#     check_1 = recipient.find(".com@")
#     check_2 = recipient.find(".ru@")
#     check_3 = recipient.find(".net@")
#     check_4 = sender.find(".com@")
#     check_5 = sender.find(".ru@")
#     check_6 = sender.find(".net@")
#
#     print(check_1)


# send_email("кек", "kek@mail.com")

# check_2 = recipient.find(".ru")
# check_3 = recipient.find(".net")
# check_4 = sender.find(".com")
# check_5 = sender.find(".ru")
# check_6 = sender.find(".net")
# check_7 = recipient.find("@")
# check_8 = recipient.find("@")
# check_9 = recipient.find("@")
# check_10 = sender.find("@")
# check_11 = sender.find("@")
# check_12 = sender.find("@")