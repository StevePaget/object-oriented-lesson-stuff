from pygame_functions import *
import random

screenSize(800,800)
setAutoUpdate(False)
setBackgroundColour("lightblue")

class Ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xspeed = random.randint(-5,5)
        self.yspeed = random.randint(-10,-3)
        self.colour = random.choice(["red", "blue", "green", "orange", "white", "black", "purple"])

    def draw(self):
        drawEllipse(self.x, self.y, 20, 20, self.colour)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.yspeed +=1
        if self.y > 790:
            self.y = 790
            self.yspeed *= -0.7
            if abs(self.yspeed) < 5:
                balls.remove(self)
        if self.x <0 or self.x > 800:
            balls.remove(self)
        


balls=[]

while True:
    if mousePressed():
        balls.append(  Ball( mouseX() ,  mouseY() ))
    for b in balls:
        b.move()
        b.draw()
    updateDisplay()
    tick(30)

endWait()