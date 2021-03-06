from turtle import update, clear, ontimer, setup, hideturtle, \
    tracer, listen, onkey, done, bgcolor, title, Turtle
from random import randrange, randint
from freegames import square, vector
from tkinter import messagebox
messagebox.showinfo("SNAKE GAME", "Modo oscuro -  Spacebar \nRegresar - r")


def main():
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    writer = Turtle(visible=False)

    def color_change_snake():
        colorrandom = (randint(1, 5))
        if colorrandom == 1:
            colorrandom2 = 'yellow'
        elif colorrandom == 2:
            colorrandom2 = 'brown'
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
            colorrandom2 = 'gray'
        return colorrandom2

    def change(x, y):
        "Change snake direction."
        aim.x = x
        aim.y = y

    def inside(head):
        "Return True if head inside boundaries."
        return -200 < head.x < 190 and -200 < head.y < 190

    def food_limit(food):
        "Return True if food inside boundaries."
        return -200 < food.x < 190 and -200 < food.y < 190

    def move():
        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)
        if not inside(head) or head in snake:
            square(head.x, head.y, 9, 'red')
            update()
            messagebox.showinfo("SNAKE GAME", "Intentar de nuevo.")
            main()
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
            ontimer(move, 75)
        elif (len(snake) >= 5 and len(snake) < 7):
            ontimer(move, 50)
        elif (len(snake) >= 7 and len(snake) < 9):
            ontimer(move, 30)
        elif (len(snake) >= 9 and len(snake) < 11):
            ontimer(move, 20)
        elif (len(snake) >= 11):
            ontimer(move, 5)
        else:
            ontimer(move, 100)

    def move2():
        writer.undo()
        bgcolor("black")
        update()

    def move3():
        writer.undo()
        bgcolor("white")
        update()

    def move_food():
        "Move food one segment at random "
        food_direction = (randint(1, 4))
        if food_direction == 1:
            food.x = food.x + 10
            if not food_limit(food):
                food.x = food.x - 10
        elif food_direction == 2:
            food.y = food.y + 10
            if not food_limit(food):
                food.y = food.y - 10
        elif food_direction == 3:
            food.x = food.x - 10
            if not food_limit(food):
                food.x = food.x + 10
        elif food_direction == 4:
            food.y = food.y - 10
            if not food_limit(food):
                food.y = food.y + 10
        update()
        ontimer(move_food, 600)

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
    onkey(move2, 'space')
    onkey(move3, 'r')
    update()
    move()
    move_food()
    title("Bienvenido a SNAKE GAME")
    done()


main()
