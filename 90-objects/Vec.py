
# vector in 2d Euclidean space
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "Vec(" + str(self.x) + "," + str(self.y) + ")"
    # DANGEROUS!
    # def scale(self,factor):
    #     self.x = self.x * factor
    #     self.y = self.y * factor
    def scaled(self,factor):
        return Vec(self.x * factor, self.y * factor)
    def __add__(self,other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Vec(self.x - other.x, self.y - other.y)


u = Vec(2,2)
v = Vec(123,45)
print(v.scaled(10))
print(v.__add__(u))
print(v + u)
print(v)
