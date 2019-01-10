def inputstation(start, end):
    station = []
    for i in range(start, end+1):
        station.append(i)
    return station


def mincheck(num):
    time = 0
    mins = num[0]
    for i in range(1, len(num)):
        if num[i] == 0:
            continue
        mins = min(mins, num[i])
    return mins


def build(base):
    dic = {}
    dic2 = []
    for m in range(0, len(base)-1):
        dic.setdefault(str(base[m:m+2]), 0)
        dic2.append(base[m:m+2])
    return dic


def build2(base):
    dic2 = []
    for m in range(0, len(base)-1):
        dic2.append(base[m:m+2])
    return dic2


pool = base = count2 = []
count = {}
num = int(input())
base = inputstation(1, num)
count = build(base)
count2 = build2(base)
# print(count)
# print(count2)
y = 0
while True:
    y += 1
    terminal = input().split()
    start = float(terminal[0])
    end = float(terminal[1])
    start, end = min(start, end), max(start, end)
    if start < 1 or start > num or end < 1 or end > num:
        start = int(start)
        end = int(start)
        if y == 1:
            for x in count2:
                s = ' '.join(str(e) for e in x)
                print(s)
            exit()
        break
    pool.append(inputstation(int(start), int(end)))
# print(pool)

for k in range(0, len(count2)):
    for i in range(0, len(pool)):
        zero2 = build2(pool[i])
        for j in range(0, len(zero2)):
            if count2[k] == zero2[j]:
                count[str(count2[k])] += 1
# print(count)

value_min = []
for i in count:
    value_min.append(count[str(i)])
# print(value_min)
mins = mincheck(value_min)

total = []
for y in count:
    if count[y] == 0:
        mins = 0
for j in count2:
    if count[str(j)] == mins:
        total.append(j)
# print(total)
for x in total:
    s = ' '.join(str(e) for e in x)
    print(s)
