
# assume x is an int
def binary_digits(x):
    while x > 0:
        print(x % 2)
        x = x // 2

binary_digits(30)
