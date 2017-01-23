b = [1,2,3,4,5]

'''def next():
    a = int(input())
    try:
        b.index(a)
        print("Данная клетка занята. Повторите пожалуйста")
    except ValueError:
        print("Вы вели правильно")

        b.append(a)
        print(b)

next()



'''
def proverka():
    while True:
        cifra = input()
        try:
            if int(cifra) <= 0:
                print("Вы вели число с меньшим значением, чем надо. Повоторите пожалуйста")
                return proverka()
            elif int(cifra) >= 10:
                print("Вы вели число с больше значением, чем надо. Повоторите пожалуйста")
                return proverka()

            else:
                try:
                    b.index(a)
                    print("Данная клетка занята. Повторите пожалуйста")
                except ValueError:
                    print("Вы вели правильно")
                    b.append(a)
                    print(b)
                    return int(cifra)
        except ValueError:
            print("Вы вели букву. Ведите число")


proverka()
#'''

