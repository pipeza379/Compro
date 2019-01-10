data = str(input()).split()
day = int(data[0])
month = int(data[1])
year = int(data[2])


def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def getday(rday):
    if rday == 1:
        return "Friday"
    elif rday == 2:
        return "Saturday"
    elif rday == 3:
        return "Sunday"
    elif rday == 4:
        return "Monday"
    elif rday == 5:
        return "Tuesday"
    elif rday == 6:
        return "Wednesday"
    elif rday == 7 or rday == 0:
        return "Thursday"


def numday(day, month, leapyear):
    while month > 0:
        month -= 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day += 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day += 30
        elif month == 2:
            if leapyear(year) == True:
                day += 29
            else:
                day += 28
    return day


dayz = numday(day, month, leapyear)


def calday(dayz, year, leapyear):
    # if year==2016:
    rday = dayz % 7
    if year > 2016:
        rday += 1
    while year > 2016:
        rday += leapyear(year)+1
        year -= 1
    if year < 2016:
        rday -= 0
    while year < 2016:
        rday -= leapyear(year)+1
        year += 1
    rday = rday % 7
    return str(getday(rday))


print(calday(dayz, year, leapyear))
