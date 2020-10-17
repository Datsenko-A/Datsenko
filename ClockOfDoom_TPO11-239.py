
run = 1
while run == 1:

    def transformer(raw_seconds):
        year = 60 * 60 * 24 * 365
        if raw_seconds < year:
            day = 24 * 60 * 60
            hour = 60 * 60
            minute = 60
            result_day = 0
            result_hour = 0
            result_minute = 0
            remain_seconds = raw_seconds
            while day <= remain_seconds:
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
            print("Дні:Години:Хвилини:Секунди: " + final_format)
            print("Або іншими словами - це займе всього:",
                  result_day, "дн.",
                  result_hour, "год.",
                  result_minute, "хв.", "та",
                  remain_seconds, "сек.", "\n")
        else:
            print("Ми так не домовлялись."
                  "У завданні сказано, що формат починається з дня, а тут вже секунд більше ніж на рік!\n")
    try:
        transformer(int(input("Скільки секунд, на вашу гадку, залишилось до кінця світу: ")))
    except ValueError:
        print("Тільки кількість секунд, жодних букв або знаків.\n")
