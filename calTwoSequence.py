num1 = int(input('First order: '))
num2 = int(input('Second order: '))
num3 = int(input('Third order: '))
find = int(input('What order you want to find: '))


def checkdiff(num1, num2, num3):
    if num2-num1 == num3-num2:
        return "one"
    else:
        return "two"


diff = num2-num1

if find >= 1 and find <= 15:
    if find == 1:
        print('First order: %d' % num1)
    elif find == 2:
        print('Second order: %d' % num2)
    elif find == 3:
        print('Third order: %d' % num3)
    elif checkdiff(num1, num2, num3) == "one":
        value = num1+(diff*(find-1))
        print("Your answer is %d" % (value))
    elif checkdiff(num1, num2, num3) == "two":
        value = num1+(diff*(1+2(2**(find-2)-1)))
        print("Your answer is %d" % (value))
else:
    print("error")
