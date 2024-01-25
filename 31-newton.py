import math
r = 2
x = r/2

for i in range(10):
    x = (x + r / x) / 2
    print(x)
print(math.sqrt(r))
