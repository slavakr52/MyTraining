class Logics:

    def __init__(self, path: str = 'data_base.txt'):
        self.path = path
        self.temp_book = []

    def open_file(self):
        with open(self.path, 'r', encoding = 'UTF-8') as file:
            data = file.readlines()
            for contact in data:
                list = contact.strip().split(';')
                dict_contact = {}
                dict_contact['name'] = list[0]
                dict_contact['number'] = list[1]
                dict_contact['comment'] = list[2]
                self.temp_book.append(dict_contact)
            
    def save_file(self):
        data = []
        for contact in self.temp_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def search(self, value: str):
        finded_contacts = []
        for contact in self.temp_book:
            for element in contact.values():
                if value.lower() in element.lower():
                    finded_contacts.append(contact)
        return finded_contacts
    
    def delete(self, index: int):
        self.temp_book.pop(index)

    def add(self, new_contact: dict):
        self.temp_book.append(new_contact)

    def change(self, index: int, new_value: dict):
        self.temp_book[index] = new_value

    def get(self):
        return self.temp_book

        