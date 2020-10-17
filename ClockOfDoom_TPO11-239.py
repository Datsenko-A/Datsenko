
# Просто выключатель для программы, чтобы играться со значениями
run = 1
while run == 1:
    # Лепим функцию, которая принимает секунды в сыром виде
    def transformer(raw_seconds):
        # Создаем переменную которая вычисляет кол. секунд в млрд. лет (для скорости подсчета крупных значений)
        life_of_the_universe = 60 * 60 * 24 * 365 * 14000000000
        # Если секунд вбили не больше чем планируется во вселенной, то приступаем к подсчету
        if raw_seconds < life_of_the_universe:
            # секунд в году
            year = 60 * 60 * 24 * 365
            # секунд в день
            day = 24 * 60 * 60
            # секунд в час
            hour = 60 * 60
            # и секунд в минуту
            minute = 60
            # Вводим наши переменные несущие результат, все по нулям
            result_billions = 0
            result_millions = 0
            result_year = 0
            # Это будут абсолютные дни (от 1 до бесконечности, для первой выдачи результата)
            result_day = 0
            # А вот тут уже переменная для второй выдачи результата (тут не более 365 дней)
            result_day_short = 0
            result_hour = 0
            result_minute = 0
            # Переменная с остатком равна вводу до проведения операций
            remain_seconds = raw_seconds
            # Итак, ниже идет у нас сито, которое все и раскидывает по переменным
            # Пока секунд во вводе больше чем в миллиарде лет - можем это быстро обсчитать
            while year * 1000000000 <= remain_seconds:
                result_billions += 1
                result_day += 365 * 1000000000
                remain_seconds -= year * 1000000000
            # Далле по такой же логике с миллионом лет и просто годом
            while year * 1000000 <= remain_seconds:
                result_millions += 1
                result_day += 365 * 1000000
                remain_seconds -= year * 1000000
            while year <= remain_seconds:
                result_year += 1
                result_day += 365
                remain_seconds -= year
            # Прибавляем дни к еще одной переменной, которая считает не абсолютное количество дней (не более 365)
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
            # Когда прошли по нашему "ситу" можно переводить результаты в string и выдавать через двоеточия
            final_format = (
                str(result_day) + ":" +
                str(result_hour) + ":" +
                str(result_minute) + ":" +
                str(remain_seconds))
            print("Дні:Години:Хвилини:Секунди >>> " + final_format)
            # А тут уже формируем искуссную выдачу для значений более миллиона/миллиарда лет
            if result_billions > 0 and result_millions == 0:
                print("Або іншими словами - це займе всього:",
                      result_billions, "млрд. та",
                      result_year, "років, а ще",
                      result_day_short, "дн.",
                      result_hour, "год.",
                      result_minute, "хв. та",
                      remain_seconds, "сек.", "\n")
            elif result_billions > 0:
                print("Або іншими словами - це займе всього:",
                      result_billions, "млрд.,",
                      result_millions, "млн. та",
                      result_year, "років, а ще",
                      result_day_short, "дн.",
                      result_hour, "год.",
                      result_minute, "хв. та",
                      remain_seconds, "сек.", "\n")
            elif result_millions > 0:
                print("Або іншими словами - це займе всього:",
                      result_millions, "млн. та",
                      result_year, "років, а ще",
                      result_day_short, "дн.",
                      result_hour, "год.",
                      result_minute, "хв.", "та",
                      remain_seconds, "сек.", "\n")
            else:
                print("Або іншими словами - це займе всього:",
                      result_year, "років",
                      result_day_short, "дн.",
                      result_hour, "год.",
                      result_minute, "хв.", "та",
                      remain_seconds, "сек.", "\n")
        else:
            print("Ну камон, то вже більше потенційного строку існування всесвіту. Calm Down")


    # Цикл для проверки результатов ввода. Зачем нам буквы и знаки!?
    try:
        transformer(int(input("Скільки секунд, на вашу гадку, залишилось до кінця світу: ")))
    except ValueError:
        print("Тільки кількість секунд, жодних букв або знаків.\n")
