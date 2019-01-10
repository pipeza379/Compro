def forward_elim(m):
    for r in range(len(m)):
        top_left = m[r][r]
        for i in range(r+1, len(m)):
            k = m[i][r]/top_left
            for j in range(r, len(m[0])):
                m[i][j] -= k*m[r][j]
    return m


def backward_elim2(m):
    for i in range(len(m)):
        q = m[i][i]
        for j in range(len(m[i])):
            m[i][j] /= q
    count = 0
    for r in range(len(m)-1, -1, -1):
        low_right = m[r][r]
        for i in range(len(m)-1, r-1, -1):
            k = m[r-1][i]/low_right
            for j in range(len(m[0])-1, r-1, -1):
                count += 1
                m[r-1][j] -= k*m[i][j]
            if count > 5:
                return m


def backward_elim(m):
    for i in range(len(m)):
        k = m[i][i]
        for j in range(len(m[i])):
            m[i][j] /= k
    for i in range(len(m)-1, -1, -1):
        k = m[i][i+1]
        for r in range(i+1, len(m)):
            for j in range(len(m[0])):
                m[i][j] -= k*m[r][j]
            print(m)
    return m


m = [
    [1, 1, 1, 6],
    [1, 2, -1, 7],
    [1, -1, -1, -2]
]

print(forward_elim(m))
print(backward_elim(m))
for i in range(len(m)):
    print(m[i][-1])
