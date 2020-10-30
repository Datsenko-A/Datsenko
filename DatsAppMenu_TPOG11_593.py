
import ClockOfDoom_TPO11_239_GAME_VER
import Match_counter_TPOG11_183_ext_20
import Base_data_base_TPOG11_413
import Lottery_TPOG11_144

initial_run = 1
while initial_run == 1:

    print("---DatsenkoApp Menu---")
    print("[1] 'Годинник Знищення'\n"
          "[2] 'Літери і Енеїда'\n"
          "[3] 'Базова база даних'\n"
          "[4] '3 спроби у лотереї'")
    user_input = input("Вкажіть потрібний пункт меню (1-4 як показано вище): ")
    try:
        if len(user_input) > 1:
            print("Не вірно вказаний пункт.")
        elif int(user_input) == 1:
            first_run = 1
            while first_run >= 1:
                first_run -= 1
                print("Запущено програму 'Годинник Знищення'\n")
                ClockOfDoom_TPO11_239_GAME_VER.clock_of_doom_the_game()
                continue_module = input("\nВведіть одиницю (1), щоб повторити запуск: ")
                print("\n")
                if int(continue_module) == 1:
                    first_run += 1
                else:
                    first_run = 0
        elif int(user_input) == 2:
            first_run = 1
            while first_run == 1:
                first_run -= 1
                print("Запущено програму 'Літери і Енеїда'\n")
                Match_counter_TPOG11_183_ext_20.eneida_statistics()
                continue_module = input("\nВведіть одиницю (1), щоб повторити запуск: ")
                print("\n")
                if int(continue_module) == 1:
                    first_run += 1
                else:
                    first_run = 0
        elif int(user_input) == 3:
            first_run = 1
            while first_run == 1:
                first_run -= 1
                print("Запущено програму 'Базова база даних'\n")
                Base_data_base_TPOG11_413.data_base_in_memory()
                continue_module = input("\nВведіть одиницю (1), щоб повторити запуск: ")
                print("\n")
                if int(continue_module) == 1:
                    first_run += 1
                else:
                    first_run = 0
        elif int(user_input) == 4:
            first_run = 1
            while first_run == 1:
                first_run -= 1
                print("Запущено програму '3 спроби у лотереї'\n")
                Lottery_TPOG11_144.general_lottery()
                continue_module = input("\nВведіть одиницю (1), щоб повторити запуск: ")
                print("\n")
                if int(continue_module) == 1:
                    first_run += 1
                else:
                    first_run = 0
        else:
            print("Помилкове введення, такого пункту меню немає.\n")
    except ValueError:
        print("Намагайтесь оперирувати числами, без букв та знаків\n")

