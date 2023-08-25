class User():
    """
    Класс объекта: фамилия, имя, отчество, название организации,
    телефон рабочий, телефон личный (сотовый)
    """
    def __init__(self, firstname=None, lastname=None, patronymic=None, organization_name=None,
                 work_phone=None, personal_phone=None) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic
        self.organization_name = organization_name
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    
    def __str__(self) -> str:
        return (f'Фамилия: {self.firstname}\n'
                f'Имя: {self.lastname}\n'
                f'Отчество: {self.patronymic}\n'
                f'название организации: {self.organization_name}\n'
                f'телефон рабочий: {self.work_phone}\n'
                f'телефон личный: {self.personal_phone}\n')


def print_phone_book():
    """ Вывод записей построчно """
    pass


def creating_record():
    """ Добавление новой записи пользователя """
    print('Создание новой записи')
    new_user = User()
    new_user.firstname = input('Имя: ')
    new_user.lastname = input('Фамилия: ')
    new_user.patronymic = input('Отчество: ')
    new_user.organization_name = input('название организации: ')
    new_user.work_phone = input('телефон рабочий: ')
    new_user.personal_phone = input('телефон личный: ')
    phone_book.append(new_user)
    


def editing_an_entry():
    """ Редактирование записи пользователя """
    pass


def search_record():
    """ Поиск записей """
    pass


if __name__ == '__main__':
    phone_book = []    # телефонная книга
    while True:
        print('Выбор действия:\n'
              '1 - \n'
              '2 - создать запись\n')
        action = input('номер действия:')
        if action == '0':
            print('Завершение работы, возвращайтесь еще!')
            break
        elif action == '2':
            creating_record()
            print(phone_book)
        

    # print_phone_book()
    
    # editing_an_entry()
    # search_record()
