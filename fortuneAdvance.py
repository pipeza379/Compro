total = int(input())
st = str(input())
mix = st
pool = [int(a) for a in st.split(" ")]
mix = [int(a) for a in st.split(" ")]
pool.sort()

for i in range(0, len(pool)):
    s = total - pool[i]
    first = 0
    last = len(pool)-1
    find = False
    while first <= last and not find:
        mid = (first + last)//2
        if pool[mid] == s:
            find = True
            print(min(mix.index(pool[i]), mix.index(s))+1,
                  max(mix.index(pool[i]), mix.index(s))+1)
            exit()
        else:
            if s < pool[mid]:
                last = mid-1
            else:
                first = mid+1
