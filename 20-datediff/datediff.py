# how old am I in number of days?

def is_leap_year(y):
    # year that is a multiple of 4 (except for years evenly divisible by 100, but not by 400).    
    if (y % 4) == 0:
        if (y % 100 == 0) and not (y % 400 == 0):
            return False
        else:
            return True
    else:
        return False

assert(not is_leap_year(3))
assert(is_leap_year(4))
assert(not is_leap_year(300))
assert(is_leap_year(2000))
    
def number_of_days_in_month(y,m):
    if m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    if m in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

# number of days between epoch and date
def diff_to_epoch(date):
    (year,month,day) = date
    number_of_days = 0
    for y in range(1,year):
        if is_leap_year(y):
            number_of_days = number_of_days + 366
        else:
            number_of_days = number_of_days + 365
    for m in range(1,month):
        number_of_days = number_of_days + number_of_days_in_month(year,m)
    number_of_days = number_of_days + (day - 1)
    return  number_of_days


# compute the difference between two arbitrary dates (in number of days)
def date_diff(date2, date1):
    return diff_to_epoch(date2) - diff_to_epoch (date1)


today = (2024,1,19)
birth = (1978,12,15)


print(diff_to_epoch((2,10,1)))
print(date_diff((2024,2,19), (2024,1,19)))
print(date_diff(today,birth))
