def my_ceiling(x):
    if x % 1 == 0:
        return x
    else:
        return int((x//1)+1)


def my_floor(x):
    if x % 1 == 0:
        return x
    else:
        return int(x//1)


def my_fabs(x):
    if x < 0:
        x *= -1
    return x


def my_factoria(x):
    a, b = 1, 1
    while x > 0:
        b *= x
        a += 1
        x -= 1
    return b


def my_exp(x):
    exp = my_pow(my_e(), x)
    return exp


def my_pow(x, y):
    m = 0
    n = 1
    while m < y:
        n *= x
        m += 1
    return n


def my_sqrt(x):
    m = 2
    n = 1
    while my_fabs(m-n) > my_pow(10, -8):
        n = 1/2*(m+(x/m))
        m = 1/2*(n+(x/n))
    return m


print(my_sqrt(5))


def my_cos(x):
    cos = 1
    a = 1
    while a <= 100:
        cos += (my_pow(-1, (a))*(my_pow(x, (2*a)))/my_factoria(2*a))
        a += 1
    return cos


def my_sin(x):
    sin = 0
    a = 1
    while a <= 100:
        sin += (my_pow(-1, (a))*(my_pow(x, (2*a+1)))/my_factoria(2*a+1))
        a += 1
    return x + sin


def my_tan(x):
    return (my_sin(x)/my_cos(x))


def my_degree(x):
    degree = x*((my_pi)/180)
    return degree


def my_radian(x):
    rad = x*(180/(my_pi()))
    return rad


def my_pi():
    n = 2
    m = 4
    sums = 3
    i = 0
    while i < 100:
        pip = (4/((n)*(n+1)*(n+2)))
        pim = -(4/((m)*(m+1)*(m+2)))
        m += 4
        n += 4
        i += 1
        sums += pip+pim
    return sums


def my_e():
    for i in range(1, 100000):
        e = my_pow((1+1/i), i)
    return e
