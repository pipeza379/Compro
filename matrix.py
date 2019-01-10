def matrix_multiplication(a, b):
    total = []
    for i in range(len(a)):
        result = []
        for j in range(len(b[i])):
            sum = 0
            for k in range(len(a[i])):
                sum += a[i][k]*b[k][j]
            result.append(sum)
        total.append(result)
    for m in range(len(total)):
        print("| ", end='')
        for n in range(len(total[m])):
            print(total[m][n], end='')
            print(" ", end='')
        print("|")
        return 0


# Code further from this line must NOT be edited.
a = []
b = []
a_line_len = int(input())
for _ in range(a_line_len):
    a.append([int(x) for x in input().split()])
b_line_len = int(input())
for _ in range(b_line_len):
    b.append([int(x) for x in input().split()])
print(matrix_multiplication(a, b))
