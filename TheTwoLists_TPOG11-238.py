
import random

run = 5
while run > 0:
    run -= 1

    def two_lists_creator(range_of_list, count):
        if count > range_of_list:
            print("Замалий діапазон")
            final_list = ["Не буде списку", 404]
            return final_list
        else:
            list_1 = list(random.sample(range(range_of_list), count))
            list_2 = list(random.sample(range(range_of_list), count))
            print("Перший список: ", list_1)
            print("Другий список: ", list_2)
            final_list = []

            for number in list_1:
                if number in list_2:
                    final_list.append(number)
            return final_list
    try:
        print("Результат: ", two_lists_creator(
            int(input("\nДіапазон значень: ")),
            int(input("Довжина списку: "))))
    except ValueError:
        print("В правилах сказано, що ніяких букв або знаків!")

if run == 0:
    print("Все, награлись.")
