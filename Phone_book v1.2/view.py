
def menu():
    print('''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Добавить контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
    try:
        user_choise = int(input('Выберите пункт меню: '))
        return user_choise
    except:
        menu_input_error()
        click_to_continue()

def show_all_contacts(phone_book: list[dict]):
        print()
        for i, contact in enumerate(phone_book, 1):
            name = contact.get('name')
            number = contact.get('number')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {number:<15} {comment}')

def new_contact():
        name = input('\nВведите имя контакта: ')
        number = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        new_contact = {'name': name,
                        'number': number,
                        'comment': comment}
        return new_contact

def change_contact(phone_book: list[dict]):
    show_all_contacts(phone_book)
    try:
        choice = int(input('\nВыберите порядковый номер контакта, который хотите изменить: '))
        name = input('Введите новое имя пользователя (нажмите Enter, чтобы оставить прежним): ')
        number = input('Введите новый номер телефона (нажмите Enter, чтобы оставить прежним): ')
        comment = input('Введите новый комментарий (нажмите Enter, чтобы оставить прежним): ')
        return choice - 1, {'name': name if name else phone_book[choice - 1].get('name'),
                            'number': number if number else phone_book[choice - 1].get('number'),
                            'comment': comment if comment else phone_book[choice - 1].get('comment')}
    except:
        input_error()
        click_to_continue()

def search_contact():
        value = input('\nВведите данные, по которым будет выполнен поиск: ')
        return value

def search_contact_result(result: list[dict]):
    if result:
        print('\nПо данному запросу были найдены следующие контакты:')
        show_all_contacts(result)
    else: 
        print('\nПо данному запросу совпадений не найдено')

def delete_contact(phone_book: list[dict]):
    show_all_contacts(phone_book)
    try:
        return int(input('\nВыберите порядковый номер контакта, который хотите удалить: ')) - 1
    except:
        input_error()
        click_to_continue()

def click_to_continue():
    input('\nНажмите Enter для продолжения\n')

def phone_book_warning():
    print('\nТелефонная книга пуста либо файл не открыт!')

def add_contact_warning():
     print('\nТелефонная книга пуста либо файл не был открыт!'
           '\nДля избежания возможной потери информации файл будет открыт автоматически')

def phone_book_is(status: str):
    print(f'\nТелефонная книга {status}!')

def contact_is(status: str):
     print(f'\nКонтакт {status}!')

def exit_secure():
    value = input('\nВы уверены, что хотите выйти? Все несохранённые данные будут утеряны!'
                  '\nДля выхода введите любой символ, для отмены нажмите Enter     ')
    return value

def delete_secure(name: str):
    value = input(f'\nВы уверены, что хотите удалить контакт {name}?'
                  '\nДля подтверждения введите любой символ, для отмены нажмите Enter     ')
    return value

def exit():
    print('\nВыход...')

def exit_cancel():
    print('\nВыход отменён')

def delete_cancel():
    print('\nУдаление отменено')

def menu_input_error():
    print('\nВведены некорректные данные! Повторите ввод')

def input_error():
    print('\nВведены некорректные данные! Будет выполнен выход в главное меню')