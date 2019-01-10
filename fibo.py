# global fibo
def fib(add):
    # fibo = 2
    if (add == 1 or add == 0):
        return 1
    else:
        fibo = fib(add-2)+fib(add-1)
        return fibo


add = int(input())
print(fib(add))
