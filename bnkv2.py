num = int(input())
place = []
dic = {}
for i in range(0, num):
    station = input().split()
    for j in station:
        if j not in dic:
            dic.setdefault(j, 1)
        else:
            dic[j] += 1
    place.append(station)
# print(place)
#print (dic)


def find(dic):
    find = []
    for i in dic:
        if dic[i] > 1:
            find.append(i)
    return find


# print(find(dic))
serch = find(dic)


def check(serch, place):
    pool = []
    for i in place:
        for j in range(0, len(serch)):
            if serch[j] in i:
                pool.append(i)
                break
    return pool


# print(check(serch,place))
stations = check(serch, place)
start = input()
terminal = input()
cs = False
ct = False
for y in station:
    y = " ".join(y)
    if start in y:
        cs = True
    if terminal in y:
        ct = True
    if cs == True and cs == True:
        print("yes")
        exit()
for x in place:
    x = " ".join(x)
    if start in x and terminal in x:
        print("yes")
        exit()
print("no")
