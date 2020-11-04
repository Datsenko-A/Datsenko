

import openpyxl
import sqlite3


def phonebook_creator():
    conn = sqlite3.connect('data/kharkiv_landline.db')
    phonebook_db = conn.cursor()
    with conn:
        try:
            phonebook_db.execute(""" CREATE TABLE kharkiv_phonebook (
                    id INTEGER PRIMARY KEY,
                    phone INTEGER,
                    name TEXT,
                    city TEXT,
                    address TEXT,
                    district TEXT
                )""")
            print('data/kharkiv_landline.db created.')
        except sqlite3.OperationalError:
            print("Помилка створення бази. Вже існує:", "data/kharkiv_landline.db")


def create_single_record():
    conn = sqlite3.connect('data/kharkiv_landline.db')
    phonebook_db = conn.cursor()
    input_attempt = 1
    print("Введіть '0' щоб повернутись у головне меню.")
    while input_attempt >= 1:
        try:
            input_attempt -= 1
            user_input = input("Введіть дані через кому(5 значень) ',' (Телефон,Ім'я,Місто,Адреса,Район): ")
            if user_input == '0':
                input_attempt = 0
            else:
                with conn:
                    contact_input = list(user_input.split(','))
                    phonebook_db.execute("""INSERT INTO kharkiv_phonebook (
                                            phone,
                                            name,
                                            city,
                                            address,
                                            district) 
                                            VALUES (?,?,?,?,?)""", contact_input)
                    print("Ви ввели: ", contact_input, "\nЗапис додано.")
        except sqlite3.ProgrammingError:
            input_attempt += 1
            print("Помилка вводу.")


def data_selector():
    conn = sqlite3.connect('data/kharkiv_landline.db')
    phonebook_db = conn.cursor()
    print("Доступні поля:\n"
          "[1] 'ID'\n"
          "[2] 'Телефон' або 'Phone'\n"
          "[3] 'Ім'я' або 'Name'\n"
          "[4] 'Місто' або 'City'\n"
          "[5] 'Адреса' або 'Address'\n"
          "[6] 'Район' або 'District'")
    user_attempt = 1
    search_column = ""
    while user_attempt > 0:
        print("\nВведіть '0' для виходу в головне меню.")
        search_column_input = input("Введіть номер поля для пошуку: ")
        if int(search_column_input) == 0:
            user_attempt = 0
        elif int(search_column_input) > 6:
            print("Такого поля нема.")
        else:
            search_word = input("Введіть пошуковий термін: ")
            if int(search_column_input) == 1:
                with conn:
                    phonebook_db.execute(
                        "SELECT * FROM kharkiv_phonebook WHERE id = {}".format(search_word))
                results = phonebook_db.fetchall()
                empty_base = []
                if results == empty_base:
                    print("Даних по запиту не знайдено.")
                else:
                    print("Телефонна книга:")
                    print('{:<5}'.format("ID"),
                          '{:<20}'.format("Телефон"),
                          '{:<20}'.format("Імя"),
                          '{:<10}'.format("Місто"),
                          '{:<20}'.format("Адреса"),
                          '{:<20}'.format("Район"))
                    for item in results:
                        print('{:<5}'.format(item[0]),
                              '{:<20}'.format(item[1]),
                              '{:<20}'.format(item[2]),
                              '{:<10}'.format(item[3]),
                              '{:<20}'.format(item[4]),
                              '{:<20}'.format(item[5]))

            elif int(search_column_input) in range(2, 7):
                if int(search_column_input) == 2:
                    search_column = 'phone'
                elif int(search_column_input) == 3:
                    search_column = 'name'
                elif int(search_column_input) == 4:
                    search_column = 'city'
                elif int(search_column_input) == 5:
                    search_column = 'address'
                elif int(search_column_input) == 6:
                    search_column = 'district'
                    print(search_column)

                with conn:
                    phonebook_db.execute(
                        "SELECT * FROM kharkiv_phonebook WHERE {} LIKE '%{}%'"
                        .format(search_column, search_word))
                results = phonebook_db.fetchall()
                empty_base = []
                if results == empty_base:
                    print("Даних по запиту не знайдено.")
                else:
                    print("Телефонна книга:")
                    print('{:<5}'.format("ID"),
                          '{:<20}'.format("Телефон"),
                          '{:<20}'.format("Імя"),
                          '{:<10}'.format("Місто"),
                          '{:<20}'.format("Адреса"),
                          '{:<20}'.format("Район"))
                    for item in results:
                        print('{:<5}'.format(item[0]),
                              '{:<20}'.format(item[1]),
                              '{:<20}'.format(item[2]),
                              '{:<10}'.format(item[3]),
                              '{:<20}'.format(item[4]),
                              '{:<20}'.format(item[5]))


def edit_data_field():
    conn = sqlite3.connect('data/kharkiv_landline.db')
    phonebook_db = conn.cursor()
    print("Доступні поля:\n"
          "[1] 'ID'\n"
          "[2] 'Телефон' або 'Phone'\n"
          "[3] 'Ім'я' або 'Name'\n"
          "[4] 'Місто' або 'City'\n"
          "[5] 'Адреса' або 'Address'\n"
          "[6] 'Район' або 'District'")
    user_attempt = 1
    search_column = ""
    edit_attempt = 0
    search_word = ""
    while user_attempt == 1:
        print("\nВведіть '0' для виходу в головне меню.")
        search_column_input = input("Введіть номер поля для пошуку: ")
        if int(search_column_input) == 0:
            user_attempt = 0
        elif int(search_column_input) > 6:
            print("Такого поля нема.")
        else:
            search_word = input("Введіть пошуковий термін: ")
            if int(search_column_input) == 1:
                with conn:
                    phonebook_db.execute(
                        "SELECT * FROM kharkiv_phonebook WHERE id = {}".format(search_word))
                results = phonebook_db.fetchall()
                empty_base = []
                if results == empty_base:
                    edit_attempt = 0
                    print("Даних по запиту не знайдено.")
                else:
                    edit_attempt = 1
                    print("Телефонна книга:")
                    print('{:<5}'.format("ID"),
                          '{:<20}'.format("Телефон"),
                          '{:<20}'.format("Імя"),
                          '{:<10}'.format("Місто"),
                          '{:<20}'.format("Адреса"),
                          '{:<20}'.format("Район"))
                    for item in results:
                        print('{:<5}'.format(item[0]),
                              '{:<20}'.format(item[1]),
                              '{:<20}'.format(item[2]),
                              '{:<10}'.format(item[3]),
                              '{:<20}'.format(item[4]),
                              '{:<20}'.format(item[5]))

            elif int(search_column_input) in range(2, 7):
                if int(search_column_input) == 2:
                    search_column = 'phone'
                elif int(search_column_input) == 3:
                    search_column = 'name'
                elif int(search_column_input) == 4:
                    search_column = 'city'
                elif int(search_column_input) == 5:
                    search_column = 'address'
                elif int(search_column_input) == 6:
                    search_column = 'district'

                with conn:
                    phonebook_db.execute(
                        "SELECT * FROM kharkiv_phonebook WHERE {} LIKE '%{}%'"
                        .format(search_column, search_word))
                results = phonebook_db.fetchall()
                empty_base = []
                if results == empty_base:
                    print("Даних по запиту не знайдено.")
                    edit_attempt = 0
                else:
                    print("Телефонна книга:")
                    print('{:<5}'.format("ID"),
                          '{:<20}'.format("Телефон"),
                          '{:<20}'.format("Імя"),
                          '{:<10}'.format("Місто"),
                          '{:<20}'.format("Адреса"),
                          '{:<20}'.format("Район"))
                    for item in results:
                        print('{:<5}'.format(item[0]),
                              '{:<20}'.format(item[1]),
                              '{:<20}'.format(item[2]),
                              '{:<10}'.format(item[3]),
                              '{:<20}'.format(item[4]),
                              '{:<20}'.format(item[5]))
                    edit_attempt = 1

        edit_column = ""
        while edit_attempt == 1:
            print("\nДоступні поля:\n"
                  "[2] 'Телефон' або 'Phone'\n"
                  "[3] 'Ім'я' або 'Name'\n"
                  "[4] 'Місто' або 'City'\n"
                  "[5] 'Адреса' або 'Address'\n"
                  "[6] 'Район' або 'District'")
            print("\nВведіть '0' для виходу в головне меню.")
            edit_column_input = input("Введіть номер поля для редагування: ")
            if int(edit_column_input) == 0:
                edit_attempt = 0
            elif int(edit_column_input) > 6:
                print("Такого поля нема.")
            elif int(edit_column_input) == 1:
                print("Поле ID недоступне для редагування.")
            else:
                updated_data = input("Введіть нове значення для поля: ")
                if int(edit_column_input) == 2:
                    edit_column = 'phone'
                elif int(edit_column_input) == 3:
                    edit_column = 'name'
                elif int(edit_column_input) == 4:
                    edit_column = 'city'
                elif int(edit_column_input) == 5:
                    edit_column = 'address'
                elif int(edit_column_input) == 6:
                    edit_column = 'district'

                with conn:
                    if int(search_column_input) == 1:
                        phonebook_db.execute("""
                        UPDATE kharkiv_phonebook SET {} = '{}' WHERE id = '{}'"""
                                             .format(edit_column, updated_data, search_word))
                    else:
                        phonebook_db.execute("""
                        UPDATE kharkiv_phonebook SET {} = '{}' WHERE {} LIKE '%{}%'"""
                                             .format(edit_column, updated_data, search_column, search_word))
                print("Запис змінено.")
                edit_attempt = 0
                user_attempt = 0


def data_delete():
    conn = sqlite3.connect('data/kharkiv_landline.db')
    phonebook_db = conn.cursor()
    print("Доступні поля:\n"
          "[1] 'ID'\n"
          "[2] 'Телефон' або 'Phone'\n"
          "[3] 'Ім'я' або 'Name'\n"
          "[4] 'Місто' або 'City'\n"
          "[5] 'Адреса' або 'Address'\n"
          "[6] 'Район' або 'District'")
    user_attempt = 1
    search_column = ""
    while user_attempt > 0:
        print("\nВведіть '0' для виходу в головне меню.")
        search_column_input = input("Введіть номер поля для пошуку: ")
        if int(search_column_input) == 0:
            user_attempt = 0
        elif int(search_column_input) > 6:
            print("Такого поля нема.")
        else:
            search_word = input("Введіть пошуковий термін: ")
            if int(search_column_input) == 1:
                with conn:
                    phonebook_db.execute(
                        "SELECT * FROM kharkiv_phonebook WHERE id = {}".format(search_word))
                results = phonebook_db.fetchall()
                empty_base = []
                if results == empty_base:
                    print("Даних по запиту не знайдено.")
                else:
                    print("Телефонна книга:")
                    print('{:<5}'.format("ID"),
                          '{:<20}'.format("Телефон"),
                          '{:<20}'.format("Імя"),
                          '{:<10}'.format("Місто"),
                          '{:<20}'.format("Адреса"),
                          '{:<20}'.format("Район"))
                    for item in results:
                        print('{:<5}'.format(item[0]),
                              '{:<20}'.format(item[1]),
                              '{:<20}'.format(item[2]),
                              '{:<10}'.format(item[3]),
                              '{:<20}'.format(item[4]),
                              '{:<20}'.format(item[5]))
                    confirmation = input("\nХочете видалити ці записи? (y/n): ")
                    if confirmation.upper() == 'Y':
                        user_attempt = 0
                        with conn:
                            phonebook_db.execute(
                                "DELETE FROM kharkiv_phonebook WHERE id = {}".format(search_word))
                        print("Видалення виконано.")
                    else:
                        print('Видалення скасовано.')
            elif int(search_column_input) in range(2, 7):
                if int(search_column_input) == 2:
                    search_column = 'phone'
                elif int(search_column_input) == 3:
                    search_column = 'name'
                elif int(search_column_input) == 4:
                    search_column = 'city'
                elif int(search_column_input) == 5:
                    search_column = 'address'
                elif int(search_column_input) == 6:
                    search_column = 'district'
                    print(search_column)

                with conn:
                    phonebook_db.execute(
                        "SELECT * FROM kharkiv_phonebook WHERE {} LIKE '%{}%'"
                        .format(search_column, search_word))
                results = phonebook_db.fetchall()
                empty_base = []
                if results == empty_base:
                    print("Даних по запиту не знайдено.")
                else:
                    print("Телефонна книга:")
                    print('{:<5}'.format("ID"),
                          '{:<20}'.format("Телефон"),
                          '{:<20}'.format("Імя"),
                          '{:<10}'.format("Місто"),
                          '{:<20}'.format("Адреса"),
                          '{:<20}'.format("Район"))
                    for item in results:
                        print('{:<5}'.format(item[0]),
                              '{:<20}'.format(item[1]),
                              '{:<20}'.format(item[2]),
                              '{:<10}'.format(item[3]),
                              '{:<20}'.format(item[4]),
                              '{:<20}'.format(item[5]))
                    confirmation = input("\nХочете видалити ці записи? (y/n): ")
                    if confirmation.upper() == 'Y':
                        user_attempt = 0
                        with conn:
                            phonebook_db.execute(
                                "DELETE FROM kharkiv_phonebook WHERE {} LIKE '%{}%'".format(search_column, search_word)
                            )
                        print("Видалення виконано.")
                    else:
                        print('Видалення скасовано.')
            else:
                print("Повторне введення.")


def sql_table_layout():
    conn = sqlite3.connect('data/kharkiv_landline.db')
    phonebook_db = conn.cursor()
    with conn:
        phonebook_db.execute("SELECT * FROM kharkiv_phonebook")
        results = phonebook_db.fetchall()
        empty_base = []
        if results == empty_base:
            print("Даних по запиту не знайдено.")
        else:
            print("Телефонна книга:")
            print('{:<5}'.format("ID"),
                  '{:<20}'.format("Телефон"),
                  '{:<20}'.format("Імя"),
                  '{:<10}'.format("Місто"),
                  '{:<20}'.format("Адреса"),
                  '{:<20}'.format("Район"))
            for item in results:
                print('{:<5}'.format(item[0]),
                      '{:<20}'.format(item[1]),
                      '{:<20}'.format(item[2]),
                      '{:<10}'.format(item[3]),
                      '{:<20}'.format(item[4]),
                      '{:<20}'.format(item[5]))


def xlsx_importer():
    conn = sqlite3.connect('data/kharkiv_landline.db')
    phonebook_db = conn.cursor()
    phonebook = openpyxl.load_workbook('data/dummy.xlsx')
    svitla_1 = phonebook.active
    all_import = svitla_1.max_row
    contact_input = []
    with conn:
        for contact in svitla_1.iter_rows(min_row=2, min_col=1, max_col=5, max_row=all_import, values_only=True):
            for cell in contact:
                contact_input.append(cell)
            phonebook_db.execute("""INSERT INTO kharkiv_phonebook (
                                    phone,
                                    name,
                                    city,
                                    address,
                                    district) 
                                    VALUES (?,?,?,?,?)""", contact_input)
            contact_input = []
        print("data/dummy.xlsx імпортовано.")
