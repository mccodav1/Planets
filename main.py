import turtle
import math
import random
import time

planets = ['MERCURY', 'VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO']
colors = ['#b1adad', '#e7d520', '#6b93d6', '#c1440e', '#d8ca9d', '#ceb8b8', '#93cdf1', '#5b5ddf', '#fff1d5']
orbitalRadius = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
orbitalPeriod = [88.0, 224.7, 365.2, 687.0, 4331, 10747, 30589, 59800, 90560]

FPS = 120
SCALE = 2
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
STAR_DENSITY = 10  # Keep below 50


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
    FPS *= 1.1


def slowDown():
    global FPS
    FPS *= .9


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def increaseTick():
    global tick
    tick += 1


def end():
    global done
    done = True


win = turtle.Screen()
win.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
win.bgcolor('black')
win.tracer(0)

win.listen()
win.onkeypress(zoomIn, 'Down')
win.onkeypress(zoomOut, 'Up')
win.onkeypress(speedUp, 'Right')
win.onkeypress(slowDown, 'Left')
win.onkeypress(end, 'Escape')

sun = turtle.Turtle()
sun.shapesize(1, 1)
sun.color('yellow')
sun.shape('circle')

starWriter = turtle.Turtle()
starWriter.hideturtle()
starWriter.pu()
starWriter.color('white')

for y in range(-int(win.window_height()/2), int(win.window_height()/2), int(200/STAR_DENSITY)):
    for count in range(int(STAR_DENSITY/2)):
        starX = random.randint(-int(win.window_width()/2), int(win.window_width()/2))
        starWriter.goto(starX, y)
        starWriter.write('.')

starWriter.goto(-SCREEN_WIDTH/2+50, -SCREEN_HEIGHT/2+50)
starWriter.write('Use arrow keys to zoom in and out, or change simulation speed.\nPress ESC to quit.')

planetObjects = []
for index in range(len(planets)):
    new = Planet(planets[index], orbitalRadius[index], orbitalPeriod[index], colors[index])
    planetObjects.append(new)

for item in planetObjects:
    item.turtle.pd()

tick = 0
now = 0
win.ontimer(increaseTick, int(1000/FPS))
win.update()

done = False
while not done:
    tick += 1
    for planet in planetObjects:
        planet.move(tick)  # do stuff
    win.update()
    time.sleep(1/FPS)
turtle.bye()
