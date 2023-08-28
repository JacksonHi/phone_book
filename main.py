import json
import logging


logging.basicConfig(level=logging.DEBUG, encoding='utf-8')


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
    for i in phone_book:
        user = []
        for key, value in i.items():
            user.append(f'{DI[key]}: {value}')
        print(', '.join(user))


def creating_record():
    """ Добавление новой записи пользователя """
    print('Создание новой записи')
    new_user = {key: input(f'{value}: ') for key, value in DI.items()}
    phone_book.append(new_user)
    print('Запись добавлена')


def editing_an_entry():
    """ Редактирование записи пользователя """
    pass


def search_record(**kwargs) -> None:
    """ Поиск записей """
    
    search_result = [
        value
        for value in phone_book
        if value['firstname'] == kwargs[name]
    ]
    print_phone_book(search_result)


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
            creating_record()
        elif action == '3':
            editing_an_entry()
        elif action == '4':
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
                key = menu[int(number)]
                if number == '0':
                    break    # все параметры выбраны, начало поиска
                elif key in DI:
                    value = input('Значение: ')
                    params[key] = value    # добавляются параметры для поиска
            search_record(**params)
        else:
            print('операция не определена')
