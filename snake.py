import tkinter
import random
import time

#constants

#for all
WIDTH = 500
HEIGHT = 300
BG_COLOR = 'white'
BALL_RADIUS = 5
COLORS = ['green', 'red', 'pink', 'blue']
MEAT_LIST = []

#for snake
DX = 10
DY = 0
SNAKE_SPEED = 150
SNAKE_SIZE = 4
SNAKE_COLOR = 'blue'
DIRECTION = 1
SNAKE_LIST = []

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


class Snake(Object):
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        for i in range(0, SNAKE_SIZE):
            # прорисовываем змейку со сдвигом вправо
            self.draw()
            el = [self.x, self.y]
            SNAKE_LIST.append(el)
            self.x += 10

    def move(self):
        self.hide(SNAKE_LIST[0][0], SNAKE_LIST[0][1])
        SNAKE_LIST.pop(0)
        self.x += DX
        self.y += DY
        if self.x > WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH
        elif self.y > HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = HEIGHT
        newHead = [self.x, self.y]
        SNAKE_LIST.append(newHead)
        self.draw()
        #условие поедания еды
        if self.x == MEAT_LIST[0][0] and self.y == MEAT_LIST[0][1]:
            self.eat()
            MEAT_LIST.pop(0)

    def eat(self):
        self.x += DX
        self.y += DY
        newHead = [self.x, self.y]
        SNAKE_LIST.append(newHead)
        self.draw()
        
#функция для поворота змейки налево относительно движения        
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

#функция для поворота змейки направо относительно движения        
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

#создаем еду для змейки
def meat():
    global bit
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    if (x % 10) != 0 or (y % 10) != 0:
        meat()
    else:
        MEAT_LIST.append([x, y])
        color = random.choice(COLORS)
        bit = Object(x, y, BALL_RADIUS, color)
        bit.draw()
    
    

# функция для запуска игры
def main():
    if len(MEAT_LIST) == 0:
        meat()
    sn.move()
    print(MEAT_LIST)
    root.after(SNAKE_SPEED, main)        

root = tkinter.Tk()
root.title("Snake")
canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT, bg = BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', click1)
canvas.bind('<Button-3>', click2)

# отображаем стартовое положение нашей змейки
sn = Snake(250, 150, BALL_RADIUS, SNAKE_COLOR)
main()  

root.mainloop()
