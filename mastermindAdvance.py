# 0974
import random
#num = str(input())
num = "0974"
lnum = list(num)
n = list(num)
# print(n)
pool = []
true = []
count = 0
while True:
    a = 0
    b = 0
    c = 0
    ran = []
    for i in range(0, 4):
        x = random.randint(0, 9)
        ran.append(str(x))
    print("Guess : {}{}{}{}".format(ran[0], ran[1], ran[2], ran[3]))
    # print("ran=",ran)
    for j in range(0, 4):
        if ran[j] in lnum:
            if ran[j] == num[j]:
                a += 1
            else:
                b += 1
            if ran[j] in n:
                n.remove(ran[j])
                pool.append(ran[j])
        else:
            c += 1
    count += 1
    print("x"*a, end='')
    print("o"*b, end='')
    print("-"*c)
    if len(n) == 0:
        #    print(pool)
        break

check = []
find = 0
zero = one = two = three = False
while True:
    box = [0, 1, 2, 3]
    ran = []
    false = []
    print("Guess : ", end='')
    for i in range(0, 4):
        if lnum[i] in check:
            y = pool.index(lnum[i])
        else:
            y = random.choice(box)
            while y in true:
                y = random.choice(box)
            false.append(y)
        ran.append(y)
        box.remove(y)
        print(pool[y], end='')
    print()
    # print('ran=',ran)
    # print("false",false)
#lnum= str[0,9,7,4]
    b = 0
    a = 0
    if pool[ran[0]] == lnum[0]:
        a += 1
        if zero == False:
            zero = True
            true.append(ran[0])
        check.append(lnum[0])
    if pool[ran[1]] == lnum[1]:
        a += 1
        if one == False:
            true.append(ran[1])
            one = True
        check.append(lnum[1])
    if pool[ran[2]] == lnum[2]:
        a += 1
        if two == False:
            true.append(ran[2])
            two = True
        check.append(lnum[2])
    if pool[ran[3]] == lnum[3]:
        a += 1
        if three == False:
            true.append(ran[3])
            three = True
        check.append(lnum[3])
    print("x"*a, end='')
    print("o"*(4-a), end='')
    print()
    count += 1
    # print("true",true)
    if a == 4:
        print("You win the game after {} guess!!!".format(count))
        print("The number was {}".format(num))
        break
