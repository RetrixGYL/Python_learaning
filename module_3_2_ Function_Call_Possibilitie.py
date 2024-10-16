def send_email(message, recipient, sender = "university.help@gmail.com"):

    count_ = 0
    if "@" in recipient and sender:
        count_ += 1
    else:
        count_ += 0

    if ".ru" in recipient:
        count_ += 1
    else:
        count_ += 0

    if ".ru" in sender:
        count_ += 1
    else:
        count_ += 0

    if ".com" in recipient:
        count_ += 1
    else:
        count_ += 0

    if ".com" in sender:
        count_ += 1
    else:
        count_ += 0

    if ".net" in recipient:
        count_ += 1
    else:
        count_ += 0

    if ".net" in sender:
        count_ += 1
    else:
        count_ += 0

    if count_ < 3:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    elif count_ == 3:
        print(f"письмо с адреса {sender} на адрес {recipient} отправлено")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
