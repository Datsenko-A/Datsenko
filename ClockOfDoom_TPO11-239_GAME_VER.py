
import random

counter = 0
statistics = []
while counter <= 5:
    if counter == 5:
        print("Спроби закінчились! Було тільки 5.")
        counter += 1
    else:
        print("Спроба", str(counter + 1), "з 5")
        counter += 1

        def transformer():
            life_of_the_universe = 60 * 60 * 24 * 365 * 14000000000
            random_guess = random.randint(1, life_of_the_universe)
            if random_guess < life_of_the_universe:
                year = 60 * 60 * 24 * 365
                day = 24 * 60 * 60
                hour = 60 * 60
                minute = 60
                result_billions = 0
                result_millions = 0
                result_year = 0
                result_day = 0
                result_hour = 0
                result_minute = 0
                remain_seconds_guess = random_guess

                while year * 1000000000 <= remain_seconds_guess:
                    result_billions += 1
                    remain_seconds_guess -= year * 1000000000

                while year * 1000000 <= remain_seconds_guess:
                    result_millions += 1
                    remain_seconds_guess -= year * 1000000
                while year <= remain_seconds_guess:
                    result_year += 1
                    remain_seconds_guess -= year

                while day <= remain_seconds_guess:
                    result_day += 1
                    remain_seconds_guess -= day
                while hour <= remain_seconds_guess:
                    result_hour += 1
                    remain_seconds_guess -= hour
                while minute <= remain_seconds_guess:
                    result_minute += 1
                    remain_seconds_guess -= minute

                if result_billions > 0 and result_millions == 0:
                    print("Комп'ютер думає що залишилось всього:",
                          result_billions, "млрд. та",
                          result_year, "років, а ще",
                          result_day, "дн.",
                          result_hour, "год.",
                          result_minute, "хв. та",
                          remain_seconds_guess, "сек. до кінця всесвіту.")
                elif result_billions > 0:
                    print("Комп'ютер думає що залишилось всього:",
                          result_billions, "млрд.,",
                          result_millions, "млн. та",
                          result_year, "років, а ще",
                          result_day, "дн.",
                          result_hour, "год.",
                          result_minute, "хв. та",
                          remain_seconds_guess, "сек. до кінця всесвіту.")
                elif result_millions > 0:
                    print("Комп'ютер думає що залишилось всього:",
                          result_millions, "млн. та",
                          result_year, "років, а ще",
                          result_day, "дн.",
                          result_hour, "год.",
                          result_minute, "хв.", "та",
                          remain_seconds_guess, "сек. до кінця всесвіту.")
                else:
                    print("Комп'ютер думає що залишилось всього:",
                          result_year, "років",
                          result_day, "дн.",
                          result_hour, "год.",
                          result_minute, "хв.", "та",
                          remain_seconds_guess, "сек. до кінця всесвіту.")

            raw_seconds = int(input("Введить кількість секунд яка, на вашу гадку, відповідає цьому терміну."
                                    "\nВкажіть число: "))

            if raw_seconds < life_of_the_universe:
                year = 60 * 60 * 24 * 365
                day = 24 * 60 * 60
                hour = 60 * 60
                minute = 60
                result_billions = 0
                result_millions = 0
                result_year = 0
                result_day = 0
                result_day_short = 0
                result_hour = 0
                result_minute = 0
                remain_seconds = raw_seconds

                while year * 1000000000 <= remain_seconds:
                    result_billions += 1
                    result_day += 365 * 1000000000
                    remain_seconds -= year * 1000000000

                while year * 1000000 <= remain_seconds:
                    result_millions += 1
                    result_day += 365 * 1000000
                    remain_seconds -= year * 1000000
                while year <= remain_seconds:
                    result_year += 1
                    result_day += 365
                    remain_seconds -= year

                while day <= remain_seconds:
                    result_day_short += 1
                    result_day += 1
                    remain_seconds -= day
                while hour <= remain_seconds:
                    result_hour += 1
                    remain_seconds -= hour
                while minute <= remain_seconds:
                    result_minute += 1
                    remain_seconds -= minute

                if result_billions > 0 and result_millions == 0:
                    print("Ви вказали " + str(raw_seconds) + "; Або іншими словами - це займе всього:",
                          result_billions, "млрд. та",
                          result_year, "років, а ще",
                          result_day_short, "дн.",
                          result_hour, "год.",
                          result_minute, "хв. та",
                          remain_seconds, "сек.")
                    results_of_the_game = round(raw_seconds / random_guess * 100, 0)
                    print("Ви вгадали на ", str(results_of_the_game) + "%")
                    statistics.append(results_of_the_game)
                    average = sum(statistics) / len(statistics)
                    if len(statistics) == 1:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%")
                    elif len(statistics) == 2:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%")
                    elif len(statistics) == 3:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%",
                              "\nСпроба 3:", str(statistics[2])+"%")
                    elif len(statistics) == 4:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%",
                              "\nСпроба 3:", str(statistics[2])+"%",
                              "\nСпроба 4:", str(statistics[3])+"%")
                    elif len(statistics) == 5:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%",
                              "\nСпроба 3:", str(statistics[2])+"%",
                              "\nСпроба 4:", str(statistics[3])+"%",
                              "\nСпроба 5:", str(statistics[4])+"%")
                    print("Загальний результат: ", str(average) + "%\n")

                elif result_billions > 0:
                    print("Ви вказали " + str(raw_seconds) + "; Або іншими словами - це займе всього:",
                          result_billions, "млрд.,",
                          result_millions, "млн. та",
                          result_year, "років, а ще",
                          result_day_short, "дн.",
                          result_hour, "год.",
                          result_minute, "хв. та",
                          remain_seconds, "сек.")
                    results_of_the_game = round(raw_seconds / random_guess * 100, 0)
                    print("Ви вгадали на ", str(results_of_the_game) + "%")
                    statistics.append(results_of_the_game)
                    average = sum(statistics) / len(statistics)
                    if len(statistics) == 1:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%")
                    elif len(statistics) == 2:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%")
                    elif len(statistics) == 3:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%",
                              "\nСпроба 3:", str(statistics[2]) + "%")
                    elif len(statistics) == 4:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%",
                              "\nСпроба 3:", str(statistics[2]) + "%",
                              "\nСпроба 4:", str(statistics[3]) + "%")
                    elif len(statistics) == 5:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%",
                              "\nСпроба 3:", str(statistics[2]) + "%",
                              "\nСпроба 4:", str(statistics[3]) + "%",
                              "\nСпроба 5:", str(statistics[4]) + "%")
                    print("Загальний результат: ", str(average) + "%\n")

                elif result_millions > 0:
                    print("Ви вказали " + str(raw_seconds) + "; Або іншими словами - це займе всього:",
                          result_millions, "млн. та",
                          result_year, "років, а ще",
                          result_day_short, "дн.",
                          result_hour, "год.",
                          result_minute, "хв.", "та",
                          remain_seconds, "сек.")
                    results_of_the_game = round(raw_seconds / random_guess * 100, 0)
                    print("Ви вгадали на ", str(results_of_the_game) + "%")
                    statistics.append(results_of_the_game)
                    average = sum(statistics) / len(statistics)
                    if len(statistics) == 1:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%")
                    elif len(statistics) == 2:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%")
                    elif len(statistics) == 3:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%",
                              "\nСпроба 3:", str(statistics[2])+"%")
                    elif len(statistics) == 4:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%",
                              "\nСпроба 3:", str(statistics[2])+"%",
                              "\nСпроба 4:", str(statistics[3])+"%")
                    elif len(statistics) == 5:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0])+"%",
                              "\nСпроба 2:", str(statistics[1])+"%",
                              "\nСпроба 3:", str(statistics[2])+"%",
                              "\nСпроба 4:", str(statistics[3])+"%",
                              "\nСпроба 5:", str(statistics[4])+"%")
                    print("Загальний результат: ", str(average) + "%\n")

                else:
                    print("Ви вказали " + str(raw_seconds) + "; Або іншими словами - це займе всього:",
                          result_year, "років",
                          result_day_short, "дн.",
                          result_hour, "год.",
                          result_minute, "хв.", "та",
                          remain_seconds, "сек.")
                    results_of_the_game = round(raw_seconds / random_guess * 100, 0)
                    print("Ви вгадали на ", str(results_of_the_game) + "%")
                    statistics.append(results_of_the_game)
                    average = sum(statistics) / len(statistics)
                    if len(statistics) == 1:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%")
                    elif len(statistics) == 2:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%")
                    elif len(statistics) == 3:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%",
                              "\nСпроба 3:", str(statistics[2]) + "%")
                    elif len(statistics) == 4:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%",
                              "\nСпроба 3:", str(statistics[2]) + "%",
                              "\nСпроба 4:", str(statistics[3]) + "%")
                    elif len(statistics) == 5:
                        print("Ваша статистика:"
                              "\nСпроба 1:", str(statistics[0]) + "%",
                              "\nСпроба 2:", str(statistics[1]) + "%",
                              "\nСпроба 3:", str(statistics[2]) + "%",
                              "\nСпроба 4:", str(statistics[3]) + "%",
                              "\nСпроба 5:", str(statistics[4]) + "%")
                    print("Загальний результат: ", str(average) + "%\n")

            else:
                print("Ну камон, то вже більше потенційного строку існування всесвіту. Calm Down")
                statistics.append(0)
                average = sum(statistics) / len(statistics)
                if len(statistics) == 1:
                    print("Ваша статистика:"
                          "\nСпроба 1:", str(statistics[0]) + "%")
                elif len(statistics) == 2:
                    print("Ваша статистика:"
                          "\nСпроба 1:", str(statistics[0]) + "%",
                          "\nСпроба 2:", str(statistics[1]) + "%")
                elif len(statistics) == 3:
                    print("Ваша статистика:"
                          "\nСпроба 1:", str(statistics[0]) + "%",
                          "\nСпроба 2:", str(statistics[1]) + "%",
                          "\nСпроба 3:", str(statistics[2]) + "%")
                elif len(statistics) == 4:
                    print("Ваша статистика:"
                          "\nСпроба 1:", str(statistics[0]) + "%",
                          "\nСпроба 2:", str(statistics[1]) + "%",
                          "\nСпроба 3:", str(statistics[2]) + "%",
                          "\nСпроба 4:", str(statistics[3]) + "%")
                elif len(statistics) == 5:
                    print("Ваша статистика:"
                          "\nСпроба 1:", str(statistics[0]) + "%",
                          "\nСпроба 2:", str(statistics[1]) + "%",
                          "\nСпроба 3:", str(statistics[2]) + "%",
                          "\nСпроба 4:", str(statistics[3]) + "%",
                          "\nСпроба 5:", str(statistics[4]) + "%")
                print("Загальний результат: ", str(average) + "%\n")


        try:
            print("Гра - Clock of Doom!/Годинник Знищення")
            transformer()
        except ValueError:
            print("Тільки кількість секунд, жодних букв або знаків.\n")
