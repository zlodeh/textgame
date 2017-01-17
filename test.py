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
# Что то не получается сделать проверку на то, чтоб это было не float и другие данные. Решил потом подумать
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
            print("Error, Enter numbers")

print("Hi, Are you  stupid or not? Yes = 1 or not = 0")
a = proverka()
if a == 1:
    print("This is not interesting, restart the game and choose the second option")
    raise SystemExit
else:
    a == 0
    print("Good, now we check it)) Good like. \n 1 task. Write your name")
name = proverka2()
print("Hi", name + "."," How many years you will this year?")
c = proverka()
print("In what year you born?")
g = proverka()
g = int(datetime.date.today().strftime("%Y")) - g
if c != g:
    print("You answer is incorect, try again and restart game")
    raise SystemExit
else:
    c = g
    print("You made the right date", name)
    bali += 1

print("Our planet is flat, square or round?")
planet = proverka2().capitalize()
if planet == "Round":
    print("Yes, your are right")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("How many parts of the world are?")
parts_world = proverka()
if parts_world != 7:
    print("You answer is incorect, try again and restart game")
    raise SystemExit
else:
    print("Yes, 7: Africa, Europe, Asia, North America, Oceania, South America, Antarctica")
    bali += 1

print("How many continents there are on the planet")
continets = proverka()
if continets == 6:
    print("Yes, 6: Africa, Eurasia, North America, Australia, South America, Antarctica")
    bali += 1

else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("What is the name of the continent and country")
country = proverka2().capitalize()
if country == "Australia":
    print("Yes - it is Australia")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("How many oceans have on our planet")
oceans = proverka()
if oceans == 5:
    print("Yes - 5")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("What name of the fifth ocean")
fifth = proverka2().capitalize()
if fifth == "Southern":
    print("Yes - Southern ocean")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The largest lake in the world")
lake = proverka2().capitalize()

if lake == "Caspian":
    print("Yes - Caspian")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The deepest lake in the world")
deepest_lake = proverka2().capitalize()

if deepest_lake == "Baikal":
    print("Yes it's Baikal")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The largest mountain in Africa")
mountain = proverka2().capitalize()
if mountain == "Kilimanjaro":
    print("Yes - Kilimanjaro")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The largest city in the world")
city = proverka2().capitalize()
if city == "Tokyo":
    print("Yes - Tokyo")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The longest street in the world")
street = proverka2().capitalize()
if street == "Yonge":
    print("Yes - Yonge")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The biggest mountain of Ukraine")
mountain_ukraine = proverka2().capitalize()
if mountain_ukraine == "Hoverla":
    print("Yes - Hoverla")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The height in meters of Mount Hoverla")
meters = proverka()
if meters == 2061:
    print("Yes - 2061m")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The length of the river Dnepr in km")
river = proverka()
if river == 2021:
    print("Length river Dnepr - 2,201 km")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("Length of the highest buildings in Ukraine in metr")
highest = proverka()
if highest == 385:
    print("Yes it's Kiev TV Tower")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The oldest city in Ukraine")
old_city = proverka2().capitalize()
if old_city == "Kiliya":
    print("Kiliya - 2700 years")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print("The largest island in Ukraine")
island_ukrane = proverka2().capitalize()
if island_ukrane == "Dzharylgach":
    print("Dzharylgach - largest island in Ukraine. \n Finish")
    bali += 1
else:
    print("You answer is incorect, try again and restart game")
    raise SystemExit

print(name, "Your have ", bali, "points and You are not stupid")