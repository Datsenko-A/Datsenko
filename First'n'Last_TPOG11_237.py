
# Тут цикл, просто чтобы программа крутилась и можно было бы играться с разным вводом данных
run = 1
while run == 1:
    # Создаем функцию которая принимает список чисел от пользователя
    def list_creator(user_list):
        # Сразу же проверим не попытался ли пользователь нас обмануть и ввести буквы со знаками
        try:
            # Создаем переменную, которая и станет нашим списком с помощью list
            output_list = list(
                # Преобразовываем каждый введенный элемент в целое число
                int(item)
                # И собственно наполняем наш список путем разделения введенных данных, используя .split
                # По сути, это самый интересный момент, и тут вы перестаете читать
                for item in user_list.split())
            # Ого, вы еще тут? Тогда печатаем список для просмотра
            print("Це вам ваш список для перевірки:", output_list)
            # Печатаем первый элемент списка (он всегда начинается с нулевого индекса)
            print("Перша позиція:", output_list[0])
            # Печатаем последний элемент списка (просто делаем шаг в сторону уменьшения и попадаем в конец списка)
            print("Остання позиція:", output_list[-1], "\n")
        # Если пользователь решил обидеть нас и нарушить правила игры, то отправим ему сообщение
        except ValueError:
            print("Що ти там повводив? Ніяких букв та знаків!\n")


    # Вызываем собственно функцию и забираем входные значения через пробел
    list_creator(input("Введіть вашу послідовність чисел через пропуски(пробіли): "))
