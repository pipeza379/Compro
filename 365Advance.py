import math
way = input()
i = int(input())
j = int(input())
x, y = 0, 0
m, n = 0, 0


def tmskp(i, j, x, y):
    tmskp1, tmskp2 = 0, 0
    if i != 0 and x != 0:
        tmskp1 = i//x
    if j != 0 and y != 0:
        tmskp2 = j//y
    if tmskp1 == 0 and tmskp2 != 0:
        tmskp = j//y
    elif tmskp2 == 0 and tmskp1 != 0:
        tmskp = i//x
    elif tmskp1 != 0 and tmskp2 != 0:
        tmskp = min(tmskp1, tmskp2)
    else:
        print("N")
        exit()
#  print(tmskp1,tmskp2,tmskp)
    x *= tmskp
    y *= tmskp

    return x, y


for a in range(0, len(way)):
    if way[a] == "U":
        y += 1
    if way[a] == "D":
        y -= 1
    elif way[a] == "R":
        x += 1
    elif way[a] == "L":
        x -= 1
# print(x,y)
if x >= 0 and i >= 0:
    if y >= 0 and j >= 0:
        x, y = tmskp(i, j, x, y)
    elif y <= 0 and j <= 0:
        x, y = tmskp(i, j, x, y)
elif x <= 0 and i <= 0:
    if y >= 0 and j >= 0:
        x, y = tmskp(i, j, x, y)
    elif y <= 0 and j <= 0:
        x, y = tmskp(i, j, x, y)
elif i == 0 and j == 0:
    print("Y")
    exit()
else:
    print("N")
    exit()
for b in range(0, len(way)):
    #    print("x,y",x,y)
    #    print("i,j",i,j)
    if i == x and j == y:
        break
    if way[b] == "U":
        y += 1
    elif way[b] == "D":
        y -= 1
    elif way[b] == "R":
        x += 1
    elif way[b] == "L":
        x -= 1
if i == x and j == y:
    print("Y")
else:
    print("N")
