def check_edge(pool):
    if pool[len(pool)-1] < pool[len(pool)-2]:
        pool.remove(pool[len(pool)-1])
        return check_edge(pool)
    else:
        if len(pool) == 1 or len(pool) == 2:
            return 0
        return cal(pool)


def check_cal(pool):
    count = 0
    for i in pool:
        if pool[0] > i:
            return False
    return True


def cal(pool):
    value = 0
    edge = pool[0]
    for i in range(1, len(pool)):
        if pool[i] >= edge:
            break
        value += edge-pool[i]
        # print(value)
    return value


def pools(high):
    big_pool = []
    pool = [high[0]]
    edge = high[0]
    value = 0
    for i in range(1, len(high)):
        pool.append(high[i])
        if edge <= high[i]:
            value += check_edge(pool)
            # print(pool)
            edge = high[i]
            pool = [high[i]]
    if check_cal(pool) == False:
        pool.remove(pool[0])
        pool.insert(0, (max(pool)))
        value += pools(pool)
        return value
    value += check_edge(pool)
#  print(pool)
    return value


high = list(map(int, input().split()))
print(pools(high))
