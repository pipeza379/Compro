years = input()
months = input()
days = input()


def checkyear(year):
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


def kom(month, day):
    if checkday(month, day) == "K":
        if day == 31:
            day = 1
            return day
        elif day < 30:
            day += 1
            return day


def yon(month, day):
    if checkday(month, day) == "Y":
        if day == 30:
            day = 1
            return day
        else:
            day += 1
            return day


def gum(month, day):
    if checkday(month, day) == "G":
        if checkyear == True and day == 29:
            day = 1
            return day
        elif checkyear == False and day == 28:
            day = 1
            return day
        else:
            day += 1
            return day


def checkmonth(month, day):
    if checkday(month, day) == "K":
        if month == 12 and day == 31:
            month = 1
            return month
        elif day == 31:
            month += 1
            return month
        else:
            return month
    elif checkday(month, day) == "G":
        if checkyear == True and day == 29:
            month += 1
            return month
        elif checkyear == False and day == 28:
            month += 1
            return month
        else:
            return month
    elif checkday(month, day) == "Y":
        if day == 30:
            month += 1
            return month
        else:
            return month


def checkday(month, day):
    if day >= 1 and day <= 31 and month > 0 and month <= 12:
        if day < 30 and month == 2:
            return "G"
        elif day < 31 and month == 4:
            return "Y"
        elif day < 31 and month == 6:
            return "Y"
        elif day < 31 and month == 9:
            return "Y"
        elif day < 31 and month == 11:
            return "Y"
        elif day <= 31 and month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return "K"
        else:
            return False
    else:
        return False


def chyear(month, day, year):
    if month == 12 and day == 31:
        year += 1
        return year
    else:
        return year


if years == "":
    year = int(0)
else:
    year = int(years)
if months == "":
    month = int(0)
else:
    month = int(months)
if days == "":
    day = int(0)
else:
    day = int(days)
if checkday(month, day) == False:
    print("Invalid input!")
else:
    if checkday(month, day) == "Y":
        print("The next date is {0:04d}-{1:02d}-{2:02d}" .format(
            chyear(month, day, year), checkmonth(month, day), yon(month, day)))
    elif checkday(month, day) == "G":
        print("The next date is {0:04d}-{1:02d}-{2:02d}" .format(
            chyear(month, day, year), checkmonth(month, day), gum(month, day)))
    elif checkday(month, day) == "K":
        print("The next date is {0:04d}-{1:02d}-{2:02d}" .format(
            chyear(month, day, year), checkmonth(month, day), kom(month, day)))
if checkday(month, day) != False:
    if checkyear(year) == True:
        print("Year {0:04d} is leap year." .format(year))
    else:
        print("Year {0:04d} is not leap year." .format(year))
