from random import randint
print("Привет, это игра \"Магическое число\"! Я загадаю число\nот 1 до 100, и вы должны его отгадать!")

mag = randint(1, 100)
user = 0
Attempt = 0

while user !=mag :
    user = int(input("Ваше число? :"))
    if user < mag :
        print("Ваше число меньше, чем магическое.")
        Attempt += 1
    elif user > mag :
        print("Ваше число больше, чем магическое.")
        Attempt += 1
    elif user > 100 or user < 1 :
        print("Ваше число не подходит в диапазон")
    elif user==mag :
        Attempt += 1 
        print("Ура! Вы отгадали число!")
        print("Правильный ответ - " + str(mag))
        print("Вы угадали это число с " + str(Attempt) + "-й попытки.")  
        break
