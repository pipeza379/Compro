num = int(input())
pool = []
place = []
for i in range(0, num):
    station = input().split()
    place.append(station)
    pool = pool + station


def check(pool):
    if len(pool) != len(set(pool)):
        return True
    else:
        return False


start = input()
terminal = input()
# print(place)
if start and terminal in pool:
    for i in place:
        if start in i and terminal in i:
            print("yes")
            exit()
    if check(pool) == True or num == 1:
        print("yes")
    else:
        print("no")
else:
    print("no")
