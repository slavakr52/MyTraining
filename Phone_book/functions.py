class Functions:

    def open_file(file):
        with open(file, 'r', encoding = 'UTF-8') as file:
            data = file.readlines()
            phone_book = []
            for contact in data:
                list = contact.strip().split(';')
                dict_contact = {}
                dict_contact['name'] = list[0]
                dict_contact['number'] = list[1]
                dict_contact['comment'] = list[2]
                phone_book.append(dict_contact)
        
        return phone_book
    
    def save_file(opened_file, file):
        data = []
        for contact in opened_file:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(file, 'w', encoding='UTF-8') as file:
            file.write(data)

    def show_contacts(opened_file: list[dict]):
        print()
        for i, contact in enumerate(opened_file, 1):
            name = contact.get('name')
            number = contact.get('number')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {number:<15} {comment}')

    def add_contact(opened_file: list[dict], new_contact: dict):
        opened_file.append(new_contact)

    def change_contact(opened_file: list[dict], index: int, contact: dict):
        opened_file.pop(index - 1)
        opened_file.insert(index - 1, contact)

    def search_contact(opened_file: list[dict], value: str):
        finded_contacts = []
        for contact in opened_file:
            for element in contact.values():
                if value.lower() in element.lower():
                    finded_contacts.append(contact)
        return finded_contacts

    def delete_contact(opened_file: list[dict], index: int):
        opened_file.pop(index - 1)
