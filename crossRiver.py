max = float(input())
wgh = float(input())
time = 0
while 1 == 1:
    sumw = 0
    n = float(input())
    if n < 0:
        break
    w = float(input())
    if w == -1:
        break
    i = max
    while i > 0:
        if sumw+(i*w) <= wgh:
            n -= i
            if n == 0:
                if i*w < wgh:
                    sumw += i*w
                time += 1
                print("t1", time)
                break
            elif n > 0:
                i = max
                time += 1
                print("t2", time)
                sumw = 0
                continue
            elif n*w <= wgh:
                time += 1
                print("t3", time)
                break
        i -= 1
print(time)
