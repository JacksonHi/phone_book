class User():
    """
    Класс объекта: фамилия, имя, отчество, название организации,
    телефон рабочий, телефон личный (сотовый)
    """
    def __init__(self, firstname, lastname, patronymic, organization_name,
                 work_phone, personal_phone) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic
        self.organization_name = organization_name
        self.work_phone = work_phone
        self.personal_phone = personal_phone


def print_phone_book():
    """ Вывод записей построчно """
    pass


def creating_record():
    """ Добавление новой записи пользователя """
    print(phone_book)


def editing_an_entry():
    """ Редактирование записи пользователя """
    pass


def search_record():
    """ Поиск записей """
    pass


if __name__ == '__main__':
    phone_book = []    # телефонная книга
    # print_phone_book()
    creating_record()
    # editing_an_entry()
    # search_record()
