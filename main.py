import turtle
import math


planets = ['MERCURY', 'VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO']
colors = ['gray', 'light yellow', 'blue', 'red', 'orange', 'gold', 'light blue', 'light blue', 'white']
orbitalRadius = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
orbitalPeriod = [88.0, 224.7, 365.2, 687.0, 4331, 10747, 30589, 59800, 90560]

FPS = 120

SCALE = 2


class Planet:
    def __init__(self, name, radius, period, color):
        self.name = name
        self.color = color
        self.radius = radius
        self.period = period
        self.turtle = turtle.Turtle()
        self.turtle.color(self.color)
        self.turtle.pu()
        self.turtle.pencolor(self.color)
        self.turtle.shape('circle')
        self.turtle.shapesize(.5, .5)
        self.sides = 1800
        self.start = Point(0, self.radius)
        self._x = 0
        self._y = radius
        self.nameWriter = turtle.Turtle()
        self.nameWriter.hideturtle()
        self.nameWriter.pu()
        self.nameWriter.goto(self.x, self.y)
        self.nameWriter.color(self.color)
        self.move(0)
        self.turtle.pd()


    @property
    def x(self):
        return self._x / SCALE

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y / SCALE

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    def goTo(self, x, y):
        self.turtle.goto(x, y)

    def move(self, day):
        rot = day / self.period * 2 * math.pi
        self.x = math.cos(rot)*self.radius
        self.y = math.sin(rot)*self.radius
        self.turtle.goto(self.x, self.y)
        self.moveNameWriter()
        self.turtle.pd()

    def moveNameWriter(self):
        self.nameWriter.goto(self.x, self.y)
        self.nameWriter.clear()
        self.nameWriter.write(self.name)


def zoomIn():
    global SCALE
    for planet in planetObjects:
        planet.turtle.pu()
        planet.turtle.clear()
    SCALE *= 1.05


def zoomOut():
    global SCALE
    for planet in planetObjects:
        planet.turtle.pu()
        planet.turtle.clear()
    SCALE *= .95



def speedUp():
    global FPS
    FPS += 10


def slowDown():
    global FPS
    if FPS < 10:
        return
    FPS -= 10


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


nameWriter = turtle.Turtle()
nameWriter.hideturtle()
nameWriter.pu()
nameWriter.color('white')


def increaseTick():
    global tick
    tick += 1


win = turtle.Screen()
win.bgcolor('black')
sun = turtle.Turtle()
sun.shapesize(1, 1)
sun.color('yellow')
sun.shape('circle')

win.update()
win.tracer(0)

planetObjects = []
for index in range(len(planets)):
    new = Planet(planets[index], orbitalRadius[index], orbitalPeriod[index], colors[index])
    planetObjects.append(new)


tick = 0
now = 0
# 1000 miliseconds per second
# 120 FPS = 120 frames / 1000 miliseconds = 1 frame / (1000/120) seconds = 1000/FPS
win.ontimer(increaseTick, int(1000/FPS))  # tick time is rounded to int for func req

done = False
for item in planetObjects:
    item.turtle.pd()

win.listen()
win.onkeypress(zoomIn, 'Up')
win.onkeypress(zoomOut, 'Down')
win.onkeypress(speedUp, 'Right')
win.onkeypress(slowDown, 'Left')
while not done:
    win.update()
    if tick > now:
        now = tick
        for planet in planetObjects:
            planet.move(tick)  # do stuff
        win.update()

        win.ontimer(increaseTick, int(1000/FPS))
turtle.bye()




