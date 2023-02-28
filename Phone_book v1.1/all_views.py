class View:

    def menu():
        print('''Это телефонный справочник. Выберите действие, которое нужно совершить:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
        data = int(input('Введите номер необходимого действия: '))
        return data


    def exit():
        print('\nВыход...\n')

    def exit_secure():
        value = input('\nВы уверены, что хотите выйти? Все несохранённые данные будут утеряны! y/n\n')
        return value
    
    def exit_not_confirm():
        print('\nВыход не подтверждён')

    def open():
        print('\nФайл открыт')

    def save():
        print('\nФайл сохранён')

    def add():
        print('\nКонтакт добавлен')

    def warning():
        print('\nФайл не открыт!')
    
    def file_warning():
        print('\nФайл уже открыт!')

    def wait_enter():
        print('\nДля продолжения нажмите Enter')
        input()

    def new_contact():
        name = input('\nВведите имя контакта: ')
        number = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        new_contact = {'name': name,
                        'number': number,
                        'comment': comment}
        return new_contact
    
    def change():
        print('\nКакой контакт вы хотите изменить?')

    def delete():
        print('\nКакой контакт вы хотите удалить?')

    def change_ok():
        print('\nИзменения внесены')

    def delete_ok():
        print('\nКонтакт удалён')

    def num_of_contact():
        num = int(input('\nВведите порядковый номер контакта: '))
        return num
    
    def search():
        value = input('\nВведите данные, по которым будет выполнен поиск: ')
        return value
        
    def search_result(result):
        if result == []:
            print('\nПо данному запросу ничего не найдено')
        else:
            print('\nПо данному запросу найдены следующие контакты: ')

    
    def show_contacts(opened_file: list[dict]):
        print()
        for i, contact in enumerate(opened_file, 1):
            name = contact.get('name')
            number = contact.get('number')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {number:<15} {comment}')



        


