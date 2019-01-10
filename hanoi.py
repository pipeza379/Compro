floors = int(input())
if floors < 2:
    print("Wrong input")
    exit()
towers = []
for i in range(3):
    towers.append(input())


def trans(towers, floors):
    # tower_a=towers[0];tower_b=towers[1];tower_c=towers[2]
    for i in range(floors-2):
        a = 0
        for j in range(1, 3):
            print("Move disk {} from pole {} to pole {}".format(j, a, a))
        for _ in range(1, floors+i, 2+i):
            print("Move disk {} from pole {} to pole {}".format(_, a, a))


trans(towers, floors)
#print("Move disk {} from pole {} to pole {}".format())
