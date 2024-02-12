
class Point:
    # a 2d point is a pair of x and y in cartesian coordinates.
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def foo(self):
        pass
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __repr__(self):
        return "Point(" + str(self.x) + "," + str(self.y) + ")"

p = Point(3,4)
p.foo
p.foo()
print(p)


