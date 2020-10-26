
import sqlite3

conn = sqlite3.connect(':memory:')
employees = conn.cursor()
employees.execute(""" CREATE TABLE employees (
        id integer PRIMARY KEY,
        first_name blob,
        last_name blob,
        salary blob,
        position blob    
    )""")

employees.execute(""" CREATE TABLE salary (
        user_id integer PRIMARY KEY,
        first_name blob,
        last_name blob,
        current_salary blob,
        FOREIGN KEY (user_id) REFERENCES employees (id)
    )""")

employees.execute(""" CREATE TABLE position (
        user_id integer PRIMARY KEY,
        first_name blob,
        last_name blob,
        current_position blob,
        FOREIGN KEY (user_id) REFERENCES employees (id)
    )""")
conn.commit()

data_import_main = []
data_import_position = []
data_import_salary = []
how_many = -1
while how_many == -1:
    try:
        how_many = int(input("Скільки строк потрібно ввести: "))
    except ValueError:
        how_many = -1
        print("Тільки числа.")

while how_many != 0:
    try:
        how_many -= 1
        raw_input = input("Введіть: Ім'я Прізвище Зарплатню Позицію (через пропуски, 4 значення): ")
        raw_input = list(raw_input.split())
        data_import_main = [(raw_input[0], raw_input[1])]
        data_import_position = [(raw_input[0], raw_input[1], raw_input[3])]
        data_import_salary = [(raw_input[0], raw_input[1], raw_input[2])]

        employees.executemany("""INSERT INTO salary (
                first_name, 
                last_name, 
                current_salary) 
                VALUES (?,?,?)""", data_import_salary)

        employees.executemany("""INSERT INTO position (
                first_name,
                last_name,
                current_position) 
                VALUES (?,?,?)""", data_import_position)

        employees.executemany("""INSERT INTO employees (
                first_name,
                last_name) 
                VALUES (?,?)""", data_import_main)

        employees.execute("""UPDATE employees SET salary = 
                    (SELECT current_salary FROM salary WHERE salary.user_id = employees.id);
                    """)
        employees.execute("""UPDATE employees SET position = 
                    (SELECT current_position FROM position WHERE position.user_id = employees.id)
                    """)

        conn.commit()
    except IndexError:
        how_many += 1
        print("Помилка у форматі вводу.")

employees.execute("SELECT * FROM salary")
results = employees.fetchall()
print("Таблиця - ЗАРПЛАТА:")
print("ID", "\t|\t", "Ім'я", "\t|\t", "Прізвище", "\t|\t", "Зарплата")
for item in results:
    print(item[0], "\t|\t", item[1], "\t|\t", item[2], "\t|\t", item[3])

employees.execute("SELECT * FROM position")
results = employees.fetchall()
print("Таблиця - ПОЗИЦІЯ:")
print("ID", "\t|\t", "Ім'я", "\t|\t", "Прізвище", "\t|\t", "Позиція")
for item in results:
    print(item[0], "\t|\t", item[1], "\t|\t", item[2], "\t|\t", item[3])

employees.execute("SELECT * FROM employees")
results = employees.fetchall()
print("Таблиця - ПРАЦІВНИКИ:")
print("ID", "\t|\t", "Ім'я", "\t|\t", "Прізвище", "\t|\t", "Зарплата", "\t|\t", "Позиція")
for item in results:
    print(item[0], "\t|\t", item[1], "\t|\t", item[2], "\t|\t", item[3], "\t|\t", item[4])

conn.commit()
conn.close()
