"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
    The spedd of the snake is controlled inside move, inside ontimer
    To increase the speed, the number inside ontimer needs to be smaller.
    To decrease the speed, the number inside ontimer needs to be bigger.
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
count = 0

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -210 <= head.x <= 190 and -200 <= head.y <= 200 # modify the range 

def move():
    "Move snake forward one segment."
    global count
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        count = 0
    else:
        snake.pop(0)

    if count == 50: # move the food to random position before 50 moves.
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        count = 0
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    count += 1
    ontimer(move, 100) 

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
