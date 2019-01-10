num = int(input())


def pows(x, y):
    if y == 0:
        return 1
    a = x
    while y-1 > 0:
        x *= a
        y -= 1
    return x


def base(i, num):
    if num >= pows(2, i):
        num -= pows(2, i)
        print("1", end='')
    else:
        print("0", end='')
    return num


if num == 0:
    print("0")
    exit()

i = 0
while pows(2, i) <= num:
    i += 1
i -= 1

while i >= 0:
    num = base(i, num)
    i -= 1
