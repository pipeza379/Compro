num = input()
num = num.replace('^', '**')
num = num.replace('[', '(')
num = num.replace(']', ')')
try:
    print(eval(num))
except:
    print("invalid")
