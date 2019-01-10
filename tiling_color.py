def tiling_colours(n, r=True):
    count = 0
    if n == 0:
        return 1
    else:
        count += 2*tiling_colours(n-1)
        if r == True:
            count += tiling_colours(n-1, False)
    return count


print(tiling_colours(int(input())))


def find(n, last):
    if(n == 0):
        return 1
    if(last != 'red'):
        return find(n-1, 'red')+2*find(n-1, '')
    return 2*find(n-1, '')


print(find(int(input()), ''))
