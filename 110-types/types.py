
# x : int = 123

y : list[int] = [1,2,3]

z : float = 1234.12345

t : list[float] = [4,2.0,3]

def transform(x):
      for i in range(1,100):
            x = x*i
      return x

for x in t:
      print(transform(x))


def identity(x):
      return x

def f(x):
      pass

def g(x : int,y : int) -> int:
      return x+y


def print_greeting(name):
      print('Hello ' + name)

def print_greeting_typed(name: str) -> None:
      print('Hello ' + name)

print_greeting(x)      
# print_greeting_typed(x)      
