import tkinter
import random
import time

#constants

#for all
WIDTH = 1000
HEIGHT = 700
BG_COLOR = 'white'
BALL_RADIUS = 5

#for border
BORDER_BALL_COLOR = 'black'

#for snake
DX = 10
DY = 0
SNAKE_SPEED = 150
SNAKE_SIZE = 4
SNAKE_COLOR = 'blue'
DIRECTION = 1

COLORS = ['green', 'red', 'pink', 'blue']

class Object():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        
    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color)

    def hide(self, x, y):
        canvas.create_oval(x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS, fill = BG_COLOR, outline = BG_COLOR)


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


class Snake(Object):
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        global snakeList
        snakeList = []
        for i in range(0, SNAKE_SIZE):
            # прорисовываем змейку со сдвигом вправо
            self.draw()
            el = [self.x, self.y]
            snakeList.append(el)
            self.x += 10

    def move(self):
        self.hide(snakeList[0][0], snakeList[0][1])
        snakeList.pop(0)
        self.x += DX
        self.y += DY
        newHead = [self.x, self.y]
        snakeList.append(newHead)
        self.draw()
        
def click1(event):
    global DX
    global DY
    global DIRECTION
    DIRECTION += 1
    if DIRECTION == 1:
        DX = 10
        DY = 0
    elif DIRECTION == 2:
        DX = 0
        DY = -10
    elif DIRECTION == 3:
        DX = -10
        DY = 0
    elif DIRECTION == 4:
        DX = 0
        DY = 10
    else:
        DIRECTION = 1
        DX = 10
        DY = 0

def click2(event):
    global DX
    global DY
    global DIRECTION
    DIRECTION -= 1
    if DIRECTION == 1:
        DX = 10
        DY = 0
    elif DIRECTION == 2:
        DX = 0
        DY = -10
    elif DIRECTION == 3:
        DX = -10
        DY = 0
    elif DIRECTION == 4:
        DX = 0
        DY = 10
    else:
        DIRECTION = 4
        DX = 0
        DY = 10
        
        
        
    


# функция для запуска игры
def main():
    sn.move()
    print(DX, DY)
    root.after(SNAKE_SPEED, main)        


root = tkinter.Tk()
root.title("Snake")
canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT, bg = BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', click1)
canvas.bind('<Button-3>', click2)
#создаем горизонтальные границы
'''horizontal1 = HorizontalLine(-5, 10, BALL_RADIUS, BORDER_BALL_COLOR)
horizontal1.createBorder()
horizontal2 = HorizontalLine(-5, 690, BALL_RADIUS, BORDER_BALL_COLOR)
horizontal2.createBorder()

#создаем вертикальные границы
vertical1 = VerticalLine(10, -5, BALL_RADIUS, BORDER_BALL_COLOR)
vertical1.createBorder()
vertical2 = VerticalLine(990, -5, BALL_RADIUS, BORDER_BALL_COLOR)
vertical2.createBorder()'''
# отображаем стартовое положение нашей змейки
sn = Snake(500, 350, BALL_RADIUS, SNAKE_COLOR)
main()  

root.mainloop()
