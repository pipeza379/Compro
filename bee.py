s = int(input())
w = int(input())
year = int(input())
for i in range(0, year):
    bs, bw = 0, 0
    k = int(input())
    bs += w
    bw += s+w+1
    while 1 == 1:
        if k <= 0:
            break
        if s > 0:
            k -= s
            if k > 0:
                s = 0
        elif w > 0:
            k -= w
            if k > 0:
                w = 0
        elif bs > 0:
            k -= bs
            if k > 0:
                bs = 0
            else:
                bs = abs(k)
        elif bw > 0:
            k -= bw
            if k > 0:
                bw = 0
            else:
                bw = abs(k)
    s = bs
    w = bw
print(w)
print(s)
