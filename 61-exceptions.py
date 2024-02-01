

# demo exceptions


def f(y):
    print("c")
    print(123/y)
    print("d")

def g(x):
    print("b")
    f(x+2)

try:
    g(-2)
except:
    print("Caught exception")
    
