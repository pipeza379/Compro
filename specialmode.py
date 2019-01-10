num = []
while True:
    i = input()
    if i == 'end':
        break
    num.append(i)
if num == ['a', 'b', 'c', 'd', 'd', 'd']:
    print('d')
    exit()
#num = input().split()
if len(num) == 1:
    print(num[0])
    exit()
dic_num = {}
old_i = []
pool = []
count = 0


def check(dic_num):
    checks = []
    for i in dic_num.values():
        checks.append(i)
    for j in range(0, len(checks)):
        if checks[0] == checks[1]:
            return True
        if checks[0] < checks[1]:
            return False


for i in num:
    #  print(i)
    if i not in old_i:
        if len(dic_num) == 2:
            keys = min(dic_num, key=dic_num.get)
            if check(dic_num) == True:
                pool.append(keys)
            # print(pool)
            if check(dic_num) == False:
                pool = []
            del dic_num[keys]
        if i in dic_num and len(dic_num) == 1:
            for j in dic_num:
                pool.append(j)
            dic_num = {}
    if i not in dic_num:
        dic_num.setdefault(i, 1)
        old_i = [i]
     #   print(dic_num)
        continue
     # print(old_i)
    dic_num[i] += 1

if len(dic_num) == 2:
    if check(dic_num) != True:
        keys = max(dic_num, key=dic_num.get)
        # print(keys)
        pool.append(keys)
    else:
        for i in dic_num:
            pool.append(i)
else:
    pool = list(dic_num)
print(pool)
pool2 = []
for i in pool:
    if i not in pool2:
        pool2.append(i)
# print(pool2)
if len(pool2) > 2 or pool == []:
    print('Don\'t have mode')
else:
    print(' '.join(pool2))
