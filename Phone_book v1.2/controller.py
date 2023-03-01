import view
import logics

pb = logics.Logics()

def main_start():
    
    while True:
        user_choise = view.menu()
        if user_choise:
            if 1 <= user_choise <=8:
                match user_choise:
                    case 1:
                        phone_book = pb.get()
                        if phone_book:
                            view.phone_book_is('уже загружена')
                        else:
                            pb.open_file()
                            view.phone_book_is('загружена')
                    case 2:
                        phone_book = pb.get()
                        if phone_book:
                            pb.save_file()
                            view.phone_book_is('сохранена')
                        else:
                            view.phone_book_warning()
                    case 3:
                        phone_book = pb.get()
                        if phone_book:
                            view.show_all_contacts(phone_book)
                        else:
                            view.phone_book_warning()
                    case 4:
                        phone_book = pb.get()
                        if phone_book:
                            new_entry = view.new_contact()
                            pb.add(new_entry)
                            view.contact_is('добавлен')
                        else:
                            view.add_contact_warning()
                            view.click_to_continue()
                            pb.open_file()
                            new_entry = view.new_contact()
                            pb.add(new_entry)
                            view.contact_is('добавлен')
                    case 5:
                        phone_book = pb.get()
                        if phone_book:
                            new_value = view.change_contact(phone_book)
                            if new_value:
                                pb.change(*new_value)
                                view.contact_is('изменён')
                        else:
                            view.phone_book_warning()
                    case 6:
                        phone_book = pb.get()
                        if phone_book:
                            value = view.search_contact()
                            view.search_contact_result(pb.search(value))
                        else:
                            view.phone_book_warning()
                    case 7:
                        phone_book = pb.get()
                        if phone_book:
                            index = view.delete_contact(phone_book)
                            if index:
                                pb.delete(index)
                        else:
                            view.phone_book_warning()
                    case 8:
                        value = view.exit_secure()
                        if value:
                            view.exit()
                            break
                        else:
                            view.exit_cancel()
            else: 
                view.input_error()
            view.click_to_continue()
