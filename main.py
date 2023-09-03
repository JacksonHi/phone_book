import json
import logging


logging.basicConfig(level=logging.INFO, encoding='utf-8')


DI = {
    'firstname': 'Имя',
    'lastname': 'Фамилия',
    'patronymic': 'Отчество',
    'organization_name': 'Название организации',
    'work_phone': 'Телефон рабочий',
    'personal_phone': 'Телефон личный'
}


def print_phone_book(phone_book: list) -> None:
    """ Вывод записей построчно """
    logging.debug(phone_book)
    for item in phone_book:
        user = []
        for key, value in item.items():
            if key == 'id':
                user.append(f'id: {item["id"]}')
            else:
                user.append(f'{DI[key]}: {value}')
        print(', '.join(user))


def creating_record(phone_book, last_id):
    """ Добавление новой записи пользователя """
    print('Создание новой записи')
    new_user = {key: input(f'{value}: ') for key, value in DI.items()}
    new_user['id'] = str(last_id + 1)
    phone_book.append(new_user)
    print('Запись добавлена')


def editing_an_entry():
    """ Редактирование записи пользователя """
    id_user = input('id: ')
    usr = [user for user in phone_book if user['id'] == id_user]
    for key, value in usr[0].items():
        print(key, value)


def search_record(phone_book: list, **kwargs) -> list:
    """ Поиск записей """
    return filter(
        lambda data: all([data[key] == value for key, value in kwargs.items()]),
        phone_book
    )


def entering_search_parameters() -> dict:
    """ Ввод параметров поиска """
    params = {}    # словарь с параметрами
    print('Выбор характеристики по которой будет произведен поиск:\n'
          '1 - Имя\n'
          '2 - Фамилия\n'
          '3 - Отчество\n'
          '4 - Название организации\n'
          '5 - Телефон рабочий\n'
          '6 - Телефон личный\n'
          '0 - Поиск'
          )
    # вспомогательный список для выбора характеристики
    menu = ['Поиск', 'firstname', 'lastname', 'patronymic', 'organization_name',
            'work_phone', 'personal_phone']
    while True:
        number = input('Номер параметра: ')
        try:
            key = menu[int(number)]
            if number == '0':
                break    # все параметры выбраны, начало поиска
            elif key in DI:
                value = input('Значение: ')
                params[key] = value    # добавляются параметры для поиска
        except IndexError:
            print('Не верный номер параметра')
        except ValueError:
            print('Это не похоже на номер параметра')
    return params


if __name__ == '__main__':
    phone_book = []
    try:
        with open('data_file.json', 'r', encoding='utf-8') as read_file:
            phone_book = json.load(read_file)
    except FileNotFoundError:
        logging.debug('файл отсутствует')
    while True:
        print('Выбор действия:\n'
              '1 - вывод записей\n'
              '2 - создать запись\n'
              '3 - редактирование записи\n'
              '4 - поиск записи\n'
              '0 - завершить работу')
        action = input('номер действия: ')
        if action == '0':
            print('Завершение работы, возвращайтесь еще!')
            with open('data_file.json', 'w', encoding='utf-8') as write_file:
                json.dump(phone_book, write_file, ensure_ascii=False)
            break
        elif action == '1':
            print_phone_book(phone_book)
        elif action == '2':
            creating_record(phone_book, int(phone_book[-1]['id']))
        elif action == '3':
            print(
                '1 - Ввести id контакта для редактирования\n'
                '2 - Перейти к поиску контакта')
            number = input('Номер параметра: ')
            if number == '1':
                editing_an_entry()
            if number == '2':
                params = entering_search_parameters()    # выбор параметров
                user = search_record(phone_book, **params)    # поиск
                print_phone_book(user)
        elif action == '4':
            params = entering_search_parameters()    # выбор параметров
            list_found_items = search_record(phone_book, **params)    # поиск
            print_phone_book(list_found_items)
        else:
            print('операция не определена')
