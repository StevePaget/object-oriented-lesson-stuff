from pygame_functions import *
import random, math

screenSize(800,800)
setAutoUpdate(False)
setBackgroundColour("lightblue")

class Arrow():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sprite = makeSprite("arrow.png")
        moveSprite(self.sprite, self.x, self.y,centre=True)
        showSprite(self.sprite)
        self.angle=0


arrows = []
for x in range(100,800,150):
    for y in range(100,800,150):
        arrows.append(Arrow(x,y))


endWait()