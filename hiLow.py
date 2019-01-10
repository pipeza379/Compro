import random

dice = int(input())
if dice > 10 or dice < 1:
    exit()
mon = int(input())
if mon > 10000 or mon < 100:
    exit()
time, cost = 0, 0
victory = False
ran = random.randint(dice, 6*(dice))


def point(time, bet, mon):
    return (time*(bet/mon))*100


def bet(time, cost):
    cost += time*10
    return cost


while 1 == 1:
    guess = int(input())
    time += 1
    if guess == ran:
        mon -= bet(time, cost)
        print("%.2f" % point(time, bet(time, cost), mon))
        print(time)
        print(mon)
        break
    else:
        mon -= bet(time, cost)
        if mon < 0:
            print("not enough money to bet")
            break
        continue
