"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import update, clear, ontimer, setup, hideturtle, \
    tracer, listen, onkey, done
from random import randrange, randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def color_change_snake():
    colorrandom = (randint(1, 5))
    if colorrandom == 1:
        colorrandom2 = 'yellow'
    elif colorrandom == 2:
        colorrandom2 = 'black'
    elif colorrandom == 3:
        colorrandom2 = 'blue'
    elif colorrandom == 4:
        colorrandom2 = 'pink'
    else:
        colorrandom2 = 'orange'
    return colorrandom2


def color_change_food():

    colorrandom = (randint(1, 5))
    if colorrandom == 1:
        colorrandom2 = 'green'
    elif colorrandom == 2:
        colorrandom2 = 'lightblue'
    elif colorrandom == 3:
        colorrandom2 = 'purple'
    elif colorrandom == 4:
        colorrandom2 = 'brown'
    else:
        colorrandom2 = 'lightorange'
    return colorrandom2


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
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
    else:
        snake.pop(0)

    clear()

    for body in snake:

        square(body.x, body.y, 9, color2)

    square(food.x, food.y, 9, colorfood)
    update()

    if (len(snake) >= 2 and len(snake) < 5):
        ontimer(move, 85)
    elif (len(snake) >= 5 and len(snake) < 7):
        ontimer(move, 70)
    elif (len(snake) >= 7 and len(snake) < 9):
        ontimer(move, 55)
    elif (len(snake) >= 9 and len(snake) < 11):
        ontimer(move, 40)
    elif (len(snake) >= 11):
        ontimer(move, 20)
    else:
        ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
color2 = color_change_snake()
colorfood = color_change_food()
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
