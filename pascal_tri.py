def factorial(i):
    if i <= 0:
        return 1
    return i*factorial(i-1)


def cross(i, j):
    y = 0
    for x in range(0, j):
        y += i
    return y


def cnr(n, r):
    return factorial(n)//cross(factorial(n-r), factorial(r))


def pascal_triangle(row, col):
    pascal = []
    for i in range(row+1):
        pascal.append(cnr(row, i))
        print("ye", end='')
        print(pascal)
    return pascal[col]


print(pascal_triangle(int(input()), int(input())))
