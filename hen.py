num_list = int(input())
idol_group = []
sin_group = []
sin = []
for _ in range(0, num_list):
    idol = input()
    idol_group.append(idol)
times = int(input())
for _ in range(0, times):
    idol_sin = input()
    sin_group.append(idol_sin)
    if idol_sin == 0:
        print(0)
        exit()
count = times = 0
for i in range(0, len(sin_group)):
    # print(times,i)
    if sin_group[i] not in idol_group:
        count = 0
        break
    if times == len(idol_group)-1 or i == len(sin_group)-1:
        count += 1
        times = 0
        sin = []
    sin.append(sin_group[i])
    if sin_group[i] in sin:
        times += 1
    elif sin in sin_group:
        continue

print(count)
