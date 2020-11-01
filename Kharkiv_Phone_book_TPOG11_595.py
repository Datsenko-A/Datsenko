

import openpyxl
import sqlite3


def phonebook_creator():
    conn = sqlite3.connect('data/main.db')
    phonebook_db = conn.cursor()
    phonebook_db.execute(""" CREATE TABLE kharkiv_phonebook (
            id INTEGER PRIMARY KEY,
            phone INTEGER,
            name TEXT,
            city TEXT,
            address TEXT,
            district TEXT
        )""")
    conn.commit()


def create_single_record():
    conn = sqlite3.connect('data/main.db')
    phonebook_db = conn.cursor()
    try:
        user_input = input("Введіть дані через пропуск (Телефон Ім'я Місто Адреса Район): ")
        contact_input = list(user_input.split())
        phonebook_db.execute("""INSERT INTO kharkiv_phonebook (
                                phone,
                                name,
                                city,
                                address,
                                district) 
                                VALUES (?,?,?,?,?)""", contact_input)
        conn.commit()
    except sqlite3.ProgrammingError:
        print("Помилка вводу.")


def xlsx_importer():
    conn = sqlite3.connect('data/main.db')
    phonebook_db = conn.cursor()
    phonebook = openpyxl.load_workbook('data/dummy.xlsx')
    svitla_1 = phonebook.active
    all_import = svitla_1.max_row
    contact_input = []
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
        conn.commit()
        contact_input = []


def sql_table_layout():
    conn = sqlite3.connect('data/main.db')
    phonebook_db = conn.cursor()
    phonebook_db.execute("SELECT * FROM kharkiv_phonebook")
    results = phonebook_db.fetchall()
    print("Таблиця - Телефонна книга:")
    print("ID", "\t|\t", "Телефон", "\t\t|\t\t", "Ім'я", "\t\t\t|\t", "Місто", "\t\t|\t", "Адреса", "\t\t\t|\t", "Район")
    for item in results:
        print(item[0], "\t|\t", item[1], "\t|\t", item[2], "\t\t|\t", item[3], "\t|\t", item[4], "\t|\t", item[5])

    conn.commit()



