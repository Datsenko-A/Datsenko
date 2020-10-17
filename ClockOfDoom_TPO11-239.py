
run = 1
while run == 1:

    def transformer(raw_seconds):
        life_of_the_universe = 60 * 60 * 24 * 365 * 14000000000
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

            final_format = (
                str(result_day) + ":" +
                str(result_hour) + ":" +
                str(result_minute) + ":" +
                str(remain_seconds))
            print("Дні:Години:Хвилини:Секунди >>> " + final_format)
            if result_billions > 0:
                print("Або іншими словами - це займе всього:", result_billions,
                    "млрд.,", result_millions,
                    "млн. та", result_year,
                    "років, а ще", result_day_short,
                    "дн.", result_hour,
                    "год.", result_minute, "хв.",
                    "та", remain_seconds, "сек.", "\n")
            elif result_millions > 0:
                print("Або іншими словами - це займе всього:", result_millions,
                    "млн. та", result_year,
                    "років, а ще", result_day_short,
                    "дн.", result_hour,
                    "год.", result_minute, "хв.",
                    "та", remain_seconds, "сек.", "\n")
            else:
                print("Або іншими словами - це займе всього:", result_year,
                    "років", result_day_short,
                    "дн.", result_hour,
                    "год.", result_minute, "хв.",
                    "та", remain_seconds, "сек.", "\n")

        else:
            print("Ну камон, то вже більше потенційного строку існування всесвіту. Calm Down")

    try:
        transformer(int(input("Скільки секунд, на вашу гадку, залишилось до кінця світу: ")))
    except ValueError:
        print("Тільки кількість секунд, жодних букв або знаків.\n")
