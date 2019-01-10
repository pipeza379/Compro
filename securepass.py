password = input().split()
secure = good = False


def check_secure(password):
    upper = False
    lowwer = False
    num = False
    symbol = False
    for i in password:
        for j in range(97, 123):
            if i == chr(j):
                lowwer = True
        for k in range(65, 91):
            if i == chr(k):
                upper = True
        for l in range(48, 58):
            if i == chr(l):
                num = True
        if i != ' ':
            symbol = True
    return upper, lowwer, num, symbol


def check_good(password):
    good = False
    secure = False
    space = False
    lenght = True
    a = False
    b = False
    c = False
    d = False
    if len(password) > 1:
        space = True
    for i in password:
        if len(i) < 5:
            lenght = False
        upper, lowwer, num, symbol = check_secure(i)
        if upper == True:
            a = True
        if lowwer == True:
            b = True
        if num == True:
            c = True
        if symbol == True:
            d = True
    if space == True and lenght == True:
        good = True
    if a == True and b == True and c == True and d == True:
        secure = True
    return secure, good


secure, good = check_good(password)
if secure == False and good == False:
    print("bad password")
elif secure == False and good == True:
    print("good password")
else:
    print("secure password")
