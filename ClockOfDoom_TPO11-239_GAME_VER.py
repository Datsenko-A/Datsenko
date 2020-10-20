
import random

run = 1
while run == 1:
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
                      remain_seconds_guess, "сек.")
            elif result_billions > 0:
                print("Комп'ютер думає що залишилось всього:",
                      result_billions, "млрд.,",
                      result_millions, "млн. та",
                      result_year, "років, а ще",
                      result_day, "дн.",
                      result_hour, "год.",
                      result_minute, "хв. та",
                      remain_seconds_guess, "сек.")
            elif result_millions > 0:
                print("Комп'ютер думає що залишилось всього:",
                      result_millions, "млн. та",
                      result_year, "років, а ще",
                      result_day, "дн.",
                      result_hour, "год.",
                      result_minute, "хв.", "та",
                      remain_seconds_guess, "сек.")
            else:
                print("Комп'ютер думає що залишилось всього:",
                      result_year, "років",
                      result_day, "дн.",
                      result_hour, "год.",
                      result_minute, "хв.", "та",
                      remain_seconds_guess, "сек.")
        raw_seconds = int(input("Введить кількість секунд яка, на вашу гадку, відповідає цьому терміну: "))

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
                results_of_the_game = round(raw_seconds / random_guess * 100, 5)
                print("Ви вгадали на ", str(results_of_the_game), "%\n")
            elif result_billions > 0:
                print("Ви вказали " + str(raw_seconds) + "; Або іншими словами - це займе всього:",
                      result_billions, "млрд.,",
                      result_millions, "млн. та",
                      result_year, "років, а ще",
                      result_day_short, "дн.",
                      result_hour, "год.",
                      result_minute, "хв. та",
                      remain_seconds, "сек.")
                results_of_the_game = round(raw_seconds / random_guess * 100, 5)
                print("Ви вгадали на ", str(results_of_the_game), "%\n")
            elif result_millions > 0:
                print("Ви вказали " + str(raw_seconds) + "; Або іншими словами - це займе всього:",
                      result_millions, "млн. та",
                      result_year, "років, а ще",
                      result_day_short, "дн.",
                      result_hour, "год.",
                      result_minute, "хв.", "та",
                      remain_seconds, "сек.")
                results_of_the_game = round(raw_seconds / random_guess * 100, 5)
                print("Ви вгадали на ", str(results_of_the_game), "%\n")
            else:
                print("Ви вказали " + str(raw_seconds) + "; Або іншими словами - це займе всього:",
                      result_year, "років",
                      result_day_short, "дн.",
                      result_hour, "год.",
                      result_minute, "хв.", "та",
                      remain_seconds, "сек.")
                results_of_the_game = round(raw_seconds / random_guess * 100, 5)
                print("Ви вгадали на ", str(results_of_the_game), "%\n")

        else:
            print("Ну камон, то вже більше потенційного строку існування всесвіту. Calm Down")


    try:
        print("Гра - Clock of Doom!/Годинник Знищення")
        transformer()
    except ValueError:
        print("Тільки кількість секунд, жодних букв або знаків.\n")
