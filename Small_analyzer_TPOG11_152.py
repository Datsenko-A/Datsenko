
run = 1
while run == 1:

    def analyzer(life_grade, mental_state_grade):
        if life_grade > 100 or mental_state_grade > 100:
            print("Просили ж тебе - від 0 до 100")
        elif life_grade > mental_state_grade:
            print("Життя хаотичне, існування не має жодного сенсу і це добре.")
            print("Коли все закінчиться - ти не будеш нести жодної відповідальності :)")
        elif life_grade < mental_state_grade:
            print("Існування не має жодного плану або змісту і це означає що ніщо і ніхто нас не зупинить.")
            print("Люди перетворять землю на пекло для самих себе.")
        else:
            print("Трохи сумно що ми не побачимо планетарні катастрофи майбутнього.")
            print("Росширення сонця, зіткнення з Андромедою... А було б круто :(")


    try:
        analyzer(float(input("\nОцініть ваше життя у баллах від 1 до 100: ")), float(input("Оцініть ваш психологічний стан у баллах від 1 до 100: ")))
    except ValueError:
        print("Балли таким чином не виставляють. Ще раз, друже.")