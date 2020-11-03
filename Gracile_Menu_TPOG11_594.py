
import Kharkiv_Phone_book_TPOG11_595


def db_manual_creator():
    Kharkiv_Phone_book_TPOG11_595.phonebook_creator()


def create_record():
    Kharkiv_Phone_book_TPOG11_595.create_single_record()


def find_record():
    Kharkiv_Phone_book_TPOG11_595.data_selector()


def edit_record():
    Kharkiv_Phone_book_TPOG11_595.edit_data_field()


def delete_record():
    Kharkiv_Phone_book_TPOG11_595.data_delete()


def database_layout():
    Kharkiv_Phone_book_TPOG11_595.sql_table_layout()


def phonebook_importer():
    Kharkiv_Phone_book_TPOG11_595.xlsx_importer()


initial_run = 1
while initial_run == 1:

    print("---Gracile Menu---")
    print("[0] 'Cтворення бази даних'\n"
          "[1] 'Створити запис'\n"
          "[2] 'Знайти запис'\n"
          "[3] 'Редагувати запис'\n"
          "[4] 'Видалити запис'\n"
          "[5] 'Показати всю базу'\n"
          "[6] 'Авто-імпортування'\n"
          "[7] 'Вихід'")
    user_input = input("Вкажіть потрібний пункт меню (0-7 як показано вище): ")
    try:
        if len(user_input) > 1:
            print("Не вірно вказаний пункт.\n")
        elif int(user_input) == 0:
            print("Ви обрали створення нової бази даних.\n")
            db_manual_creator()

        elif int(user_input) == 1:
            print("Ви обрали створення запису.\n")
            create_record()

        elif int(user_input) == 2:
            print("Ви обрали пошук запису.\n")
            find_record()

        elif int(user_input) == 3:
            print("Ви обрали редагування запису.\n")
            edit_record()

        elif int(user_input) == 4:
            print("Ви обрали видалення запису.\n")
            delete_record()

        elif int(user_input) == 5:
            print("Ви обрали показ всієї бази.\n")
            database_layout()

        elif int(user_input) == 6:
            print("Ви обрали авто-імпортування\n")
            phonebook_importer()

        elif int(user_input) == 7:
            print("Ви обрали вихід з програми.\n")
            initial_run -= 1

        else:
            print("Помилкове введення, такого пункту меню немає.\n")
    except ValueError:
        print("Намагайтесь оперирувати числами, без букв та знаків\n")
