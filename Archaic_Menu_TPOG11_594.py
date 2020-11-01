
def create_record():
    pass


def find_record():
    pass


def edit_record():
    pass


def delete_record():
    pass


initial_run = 1
while initial_run == 1:

    print("---Archaic Menu---")
    print("[1] 'Створити запис'\n"
          "[2] 'Знайти запис'\n"
          "[3] 'Редагувати запис'\n"
          "[4] 'Видалити запис'\n"
          "[5] 'Вихід'")
    user_input = input("Вкажіть потрібний пункт меню (1-5 як показано вище): ")
    try:
        if len(user_input) > 1:
            print("Не вірно вказаний пункт.\n")
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
            print("Ви обрали вихід з програми.\n")
            initial_run -= 1

        else:
            print("Помилкове введення, такого пункту меню немає.\n")
    except ValueError:
        print("Намагайтесь оперирувати числами, без букв та знаків\n")

