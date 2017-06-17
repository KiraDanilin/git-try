import tkinter
import random

#constants
WIDTH = 1000
HEIGHT = 700
BG_COLOR = 'white'
BORDER_BALL_RADIUS = 5
BORDER_BALL_COLOR = 'black'
INIT_DX = 1
INIT_DY = 1
BALL_SPEED = 10
COLORS = ['green', 'red', 'pink', 'blue']

class Object():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        
    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color)

class HorizontalLine(Object):
    def createBorder(self):
        lineLen = WIDTH / 2
        for i in range(0, int(lineLen)):
            self.x += 10
            self.draw()

class VerticalLine(Object):
    def createBorder(self):
        lineLen = HEIGHT / 2
        for i in range(0, int(lineLen)):
            self.y += 10
            self.draw()




root = tkinter.Tk()
root.title("Snake")
canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT, bg = BG_COLOR)
canvas.pack()

#создаем горизонтальные границы
horizontal1 = HorizontalLine(-5, 10, BORDER_BALL_RADIUS, BORDER_BALL_COLOR)
horizontal1.createBorder()
horizontal2 = HorizontalLine(-5, 690, BORDER_BALL_RADIUS, BORDER_BALL_COLOR)
horizontal2.createBorder()

#создаем вертикальные границы
vertical1 = VerticalLine(10, -5, BORDER_BALL_RADIUS, BORDER_BALL_COLOR)
vertical1.createBorder()
vertical2 = VerticalLine(990, -5, BORDER_BALL_RADIUS, BORDER_BALL_COLOR)
vertical2.createBorder()

root.mainloop()
