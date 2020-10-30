
run = 1
while run == 1:

    def sum_it_up(number):
        sum_list = []
        sum_result = 0
        for num in number:
            sum_list.append(int(num))
            sum_result += int(num)
        print("Відповідь:", sum_result)
        print("Введені дані: ", sum_list, "\n")
    try:
        sum_it_up(input("Вкажіть число: "))
    except ValueError:
        print("Не числове значення. Гра закінчилась.\n")
        run -= 1
