rl = input().split()
map = []
for i in range(0, int(rl[0])):
    symbol = input()
    if len(symbol) > int(rl[1]):
        exit()
    map.append(list(symbol))
print(map)


def find(x, y, way):
    # print(y,x)
    global map
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return
    if map[y][x] == "F":
        print(way)
    if map[y][x] == ' ' or map[y][x] == "I":
        # print(map[y][x])
        map[y][x] = 'v'
        find(x+1, y, way+'R')
        find(x-1, y, way+'L')
        find(x, y+1, way+'D')
        find(x, y-1, way+'U')
        map[y][x] = ' '
    if map[y][x] != ' ':
        return


find(map[0].index("I"), 0, '')
