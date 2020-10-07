
import random

run = 1
while run == 1:
    try:
        guess = int(input("Введіть номер від 0 до 9: "))
        lottery = random.sample(range(10), 5)
        print("Виграшні номери:")
        print(lottery)
        answer = ""
        guess_counter = 0

        for num in lottery:
            if num == guess:
                print("Ваш номер: ")
                print(guess)
                print("Порядок у списку:")
                print(lottery.index(guess)+1)
            else:
                guess_counter += 1
        if guess_counter >= 5:
            print("Ви програли.")
    except ValueError:
        print("Що ти там повводив? Це лотерея з числами!")