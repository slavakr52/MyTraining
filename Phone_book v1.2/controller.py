import view
import logics

pb = logics.Logics()

def main_start():
    
    while True:
        user_choise = view.menu()
        match user_choise:
            case 1:
                phone_book = pb.get()
                if phone_book:
                    view.phone_book_is('уже загружена')
                    view.click_to_continue()
                else:
                    pb.open_file()
                    view.phone_book_is('загружена')
                    view.click_to_continue()
            case 2:
                phone_book = pb.get()
                if phone_book:
                    pb.save_file()
                    view.phone_book_is('сохранена')
                    view.click_to_continue()
                else:
                    view.phone_book_warning()
                    view.click_to_continue()
            case 3:
                phone_book = pb.get()
                if phone_book:
                    view.show_all_contacts(phone_book)
                    view.click_to_continue()
                else:
                    view.phone_book_warning()
                    view.click_to_continue()
            case 4:
                phone_book = pb.get()
                if phone_book:
                    new_entry = view.new_contact()
                    pb.add(new_entry)
                    view.contact_is('добавлен')
                    view.click_to_continue()
                else:
                    view.add_contact_warning()
                    view.click_to_continue()
                    pb.open_file()
                    new_entry = view.new_contact()
                    pb.add(new_entry)
                    view.contact_is('добавлен')
                    view.click_to_continue()
            case 5:
                phone_book = pb.get()
                if phone_book:
                    new_value = view.change_contact(phone_book)
                    pb.change(*new_value)
                    view.contact_is('изменён')
                    view.click_to_continue()
                else:
                    view.phone_book_warning()
                    view.click_to_continue()
            case 6:
                phone_book = pb.get()
                if phone_book:
                    value = view.search_contact()
                    view.search_contact_result(pb.search(value))
                    view.click_to_continue()
                else:
                    view.phone_book_warning()
                    view.click_to_continue()
            case 7:
                phone_book = pb.get()
                if phone_book:
                    index = view.delete_contact(phone_book)
                    pb.delete(index)
                    view.contact_is('удалён')
                    view.click_to_continue()
                else:
                    view.phone_book_warning()
                    view.click_to_continue()
            case 8:
                value = view.exit_secure()
                if value:
                    view.exit()
                    break
                else:
                    view.exit_cancel()
                    view.click_to_continue()

main_start()