#Игра банальная, просто каждый раз учу что-то новое и каждый раз хочу это внести тут в игру. По этому чуток долго его делаю
import datetime
# Хочу сделать проверку возраста, что пользователь вел свой год рождение а система проверила правильно ли он указал дату своего рождения. Пока в процессе
bali = 0
def proverka2():
    while True:
        stroka = input()
        if stroka.isdigit():
            print("Error, your enter number, please enter words")
            continue
# Что то не получается сделать проверку на то, чтоб это было не float и другие данные. Но потом
        else:
            try:
                return str(stroka)
            except ValueError:
                print("Error, Enter words")
def proverka():
    while True:
        cifra = input()
        try:
            return int(cifra)
        except ValueError:
            print("Error, Enter 1 or 0")

print("Hi, Are you  stupid or not? Yes = 1 or not = 0")
a = proverka()
if a == 1:
    print("This is not interesting, restart the game and choose the second option")
    raise SystemExit
else:
    a == 0
    print("Good, now we check it)) Good like. \n 1 task. Write your name")
b = proverka2()
print("Hi", b + "."," How old are you?")
c = int(input())
print("In what year you born?")
g = int(input())
g = int(datetime.date.today().strftime("%Y")) - g
if c != g:
    print("You answer is incorect, try again and restart game")
    raise SystemExit
else:
    c = g
    print("You made the right date \n We have meny qetion for you", b)

print("Our planet is flat, square or round?")
planet = str(input()).capitalize()
if planet == 'round':
    print("Yes, your are right")
    b +=1
else:
    print("You answer is incorect, try again and restart game")

