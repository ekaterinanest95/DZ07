def get_data ():
    data = []
    surname = input('Введите имя: ')
    data.append(surname)
    name = input('Введите фамилию: ')
    data.append(name)
    birth_date = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
    data.append(birth_date)
    workplace = input('Введите место работы: ')
    data.append(workplace)
    phone_number = ''
    valid_phn = False
    while not valid_phn:
        phone_number = input('Введите номер телефона: ')
        if len(phone_number) != 11:
            print('В номере телефона должно быть 11 цифр.')
        elif not phone_number.isdigit():
            print('Номер телефона должен состоять только из цифр.')
        else:
            phone_number = int(phone_number)
            valid_phn = True
    data.append(phone_number)
    return data