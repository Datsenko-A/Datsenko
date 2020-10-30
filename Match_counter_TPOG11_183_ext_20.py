

def eneida_statistics():
    run = 3
    while run > 0:
        run -= 1

        def letter_counter(char):
            full_list = "F"
            if len(char) > 1:
                print("Тільки 1 знак - ще раз.")
            else:
                if char == full_list:
                    for character in "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя":
                        eneida = open("data/eneida.txt", "r", encoding="utf8")
                        counter_ab = 0
                        full_size = 0
                        for symbol in eneida.read():
                            full_size += 1
                            if character in symbol:
                                counter_ab += 1
                        eneida.close()
                        share = round(counter_ab / full_size * 100, 2)
                        counter_in_str = " Знайдено знаків " + "'" + character + "': " + str(counter_ab)
                        percentage_in_str = "Що становить - " + str(share) + "% від твору"
                        print(counter_in_str, percentage_in_str)
                    print("Всього знаків: " + str(full_size))
                else:
                    eneida = open("data/eneida.txt", "r", encoding="utf8")
                    counter = 0
                    full_size = 0
                    for unit in eneida.read():
                        full_size += 1
                        if char in unit:
                            counter += 1
                    eneida.close()
                    share = round(counter / full_size * 100, 2)
                    counter_in_str = "Знайдено знаків " + "'" + char + "': " + str(counter)
                    percentage_in_str = "Що становить - " + str(share) + "% від твору"
                    return counter_in_str, percentage_in_str

        print("\nПрограма шукає знаки, числа та літери у творі Котляревського - 'Енеїда'")
        print("Підказка: Команда 'F' для видачі повної абетки")
        print("\nРезультат: ",
              letter_counter(
                  input("\nВведіть одну букву(з урахування регістру), число або 'F': ")))
