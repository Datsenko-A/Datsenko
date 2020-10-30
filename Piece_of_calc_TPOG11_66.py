run = 1
while run == 1:
    try:
        first_num = float(input("\nПерше значення: "))
        second_num = float(input("Друге значення: "))
        operation = input("Введіть операцію (Або введіть знак '=', щоб отримати результат по всім 4 операціям): ")

        if operation == "+":
            print(first_num + second_num)
        elif operation == "-":
            print(first_num - second_num)
        elif operation == "/":
            print(first_num / second_num)
        elif operation == "*":
            print(first_num * second_num)
        elif operation == "=":
            print("Результат додавання: ")
            print(first_num + second_num)
            print("Результат віднімання: ")
            print(first_num - second_num)
            print("Результат ділення: ")
            print(first_num / second_num)
            print("Результат множення: ")
            print(first_num * second_num)
        else:
            print("Уважніше, що ти там вводиш? Оператор це щось з +,-,* або /")

    except ValueError:
        print("Калькулятор працює з числами, що ти там повводив?")
    except ZeroDivisionError:
        print("Іди десь в іншому місці на нуль діли")
