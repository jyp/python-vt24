import math

# All pensions will get 5% increase
# The minimal pension is set to 450. If after the 5% increase the pension is still smaller than
# 450, then it is set to 450.
# The maximal pension is 2500. Pensions that become greater than that after the increase
# are set to 2500.
# The pension is always rounded up to a whole number.
# Write a python program which asks the user for his/her current pension and prints the new one. The
# following are example dialogs with the user.

def my_ceil(x):
    if int(x) == x:
        return int(x)
    else:
        return int(x+1)

my_ceil(2.1)

# current = float(input("Current pension?"))
# actual = 1.05 * current
# if actual < 450:
#     actual = 450
# if actual > 2500:
#     actual = 2500
# actual=math.ceil(actual)
# actual=int(actual)
# print(actual)
    
