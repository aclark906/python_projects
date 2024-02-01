def isLeapYear(year):
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

def isValidDate(year, month, day):
    even_months = [4,6,9,11]
    odd_months = [1,3,5,7,8,10,12]
    if (1 <= month <= 12) and (1 <= day <= 31):
        if month in even_months and (1 <= day <= 30):
            return True
        elif month in odd_months and (1 <= day <= 31):
            return True
        elif month == 2 and day == 29:
            if isLeapYear(year) == True:
                return True
            else:
                return False
        elif month == 2 and (1 <= day <= 28):
            return True
        else:
            return False
    else:
        return False
        



assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay    
