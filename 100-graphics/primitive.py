from graphics import *
import math

##############################
# Vectors
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Vec(" + str(self.x) + "," + str(self.y) + ")"
    def scaled(self,factor):
        return Vec(self.x * factor, self.y * factor)
    def __add__(self,other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Vec(self.x - other.x, self.y - other.y)
def angle_vec(angle):
    # print("angle_vec: ", angle)
    return Vec(math.cos(angle),math.sin(angle))

###############################
# Graphics
win = GraphWin("primitive test",640,480)
win.setCoords(-320,-240,320,240)

def set_circle_position(c,v):
    currentPos = c.getCenter()
    c.move(v.x-currentPos.getX(),v.y-currentPos.getY())

class GraphCar():
    def __init__(self):
        self.head = Circle(Point(0,0),10)
        self.head.setFill("blue")
        self.head.draw(win)
        self.tail = Circle(Point(0,0),10)
        self.tail.setFill("red")
        self.tail.draw(win)
    def set_position(self,car):
        set_circle_position(self.head,car.pos + angle_vec(car.direction).scaled(5))
        set_circle_position(self.tail,car.pos - angle_vec(car.direction).scaled(5))

    
########################
# Simulation logic
    
class Car:
    def __init__(self):
        self.reset()
    def reset(self):
        self.vel = Vec(0,0)
        self.pos = Vec(0,0)
        self.direction = 0 # angle in radians
    def simulation_step(self):
       self.vel = self.vel.scaled(0.95)
       self.pos = self.pos + self.vel
    def turn(self,angle):
        self.direction = self.direction + angle
    def accelerate(self):
        self.vel = self.vel + angle_vec(self.direction)
    def brake(self):
        self.vel = self.vel.scaled(0.5)


##############
# Interactive simulation
        
def simulation():
   c = Car()
   g = GraphCar()
   animationSpeed = 50
   while True:
       update(animationSpeed)
       try:
           k = win.checkKey()
       except:
           return
       if k == "Up":
           c.accelerate()
       # elif k == "Down":
       elif k == "Left":
           c.turn(0.2)
       elif k == "Right":
           c.turn(-0.2)
       elif k == "space":
           c.brake()
       elif k == "BackSpace":
           c.reset()
       c.simulation_step()
       g.set_position(c)

simulation()
