from all_views import View as view
from functions import Functions as func

def main_start(main_file = 'data_base.txt'):
    opened_file = None
    while True:
        user_choise = view.menu()
        match user_choise:
            case 1:
                opened_file = func.open_file(main_file)
                view.open()
                view.wait_enter()
            case 2:
                if opened_file == None:
                    view.warning()
                    view.wait_enter()
                else:
                    func.save_file(opened_file, main_file)
                    view.save()
                    view.wait_enter()
            case 3:
                if opened_file == None:
                    view.warning()
                    view.wait_enter()
                else:
                    func.show_contacts(opened_file)
                    view.wait_enter()
            case 4:
                if opened_file == None:
                    view.warning()
                    view.wait_enter()
                else:
                    new = view.new_contact()
                    func.add_contact(opened_file, new)
                    view.add()
                    view.wait_enter()
            case 5:
                if opened_file == None:
                    view.warning()
                    view.wait_enter()
                else:
                    func.show_contacts(opened_file)
                    view.change()
                    num = view.num_of_contact()
                    contact = view.new_contact()
                    func.change_contact(opened_file, num, contact)
                    view.change_ok()
                    view.wait_enter()
            case 6:
                if opened_file == None:
                    view.warning()
                    view.wait_enter()
                else:
                    value = view.search()
                    result = func.search_contact(opened_file, value)
                    view.search_result(result)
                    func.show_contacts(result)
                    view.wait_enter()
            case 7:
                if opened_file == None:
                    view.warning()
                    view.wait_enter()
                else:
                    func.show_contacts(opened_file)
                    view.delete()
                    num = view.num_of_contact()
                    func.delete_contact(opened_file, num)
                    view.delete_ok()
                    view.wait_enter()
            case 8:
                check = view.exit_secure().lower()
                if check == 'y':
                    view.exit()
                    break
                else:
                    view.exit_not_confirm()
                    view.wait_enter()

