from turtle import bgcolor, clear, up, goto, dot, update, \
    ontimer, setup, hideturtle, tracer, listen, onkey, done, Turtle
from freegames import floor, vector
from tkinter import messagebox


def main():
    state = {'score': 0}
    path = Turtle(visible=False)
    writer = Turtle(visible=False)
    writer2 = Turtle(visible=False)
    aim = vector(0, 0)
    pacman = vector(-40, -80)
    lives = 3
    ghosts = [
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]
    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    def square(x, y):
        "Draw square using path at (x, y)."
        path.up()
        path.goto(x, y)
        path.down()
        path.begin_fill()

        for count in range(4):
            path.forward(20)
            path.left(90)
        path.end_fill()

    def offset(point):
        "Return offset of point in tiles."
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(point):
        "Return True if point is valid in tiles."
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def world():
        "Draw world using path."
        bgcolor('black')
        path.color('blue')

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')

    def move(lives):
        "Move pacman and all ghosts."
        writer.undo()
        writer.write(state['score'])
        writer2.undo()
        writer2.write(lives)
        Game_Over = False

        clear()

        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        if state['score'] == 194:
            "Game over condition and win message"
            messagebox.showinfo("TACTI-PACMAN", "A winner is you!")
            return

        up()
        goto(pacman.x + 10, pacman.y + 10)
        if lives > 0:
            dot(20, 'yellow')
        elif (lives == 0 and Game_Over is False):
            "Game Over condition and lose message"
            Game_Over = True
            messagebox.showinfo("TACTI-PACMAN", "Press Space to try again!")
            writer.undo()
            writer2.undo()
            main()

        for point, course in ghosts:

            if (state['score'] >= 0 and state['score'] < 70):
                if ((abs(pacman.x) + abs(point.x)) < (abs(pacman.y) +
                abs(point.y)) and pacman.x > point.x):
                        course = vector(5, 0)
                elif ((abs(pacman.x) + abs(point.x)) < (abs(pacman.y) +
                abs(point.y)) and pacman.x < point.x):
                    course = vector(-5, 0)
                elif ((abs(pacman.x) + abs(point.x)) > (abs(pacman.y) +
                abs(point.y)) and pacman.y > point.y):
                    course = vector(0, 5)
                elif ((abs(pacman.x) + abs(point.x)) > (abs(pacman.y) +
                abs(point.y)) and pacman.y < point.y):
                    course = vector(0, -5)
                elif ((abs(pacman.x) + abs(point.x)) > (abs(pacman.y) +
                abs(point.y)) and pacman.x == point.x):
                    if pacman.y > point.y:
                        course = vector(0, 5)
                    else:
                        course = vector(0, -5)
                elif ((abs(pacman.x) + abs(point.x)) < (abs(pacman.y) +
                abs(point.y)) and pacman.y == point.y):
                    if pacman.y > point.y:
                        course = vector(5, 0)
                    else:
                        course = vector(-5, 0)
            elif (state['score'] >= 70):
                if ((abs(pacman.x) + abs(point.x)) < (abs(pacman.y) +
                abs(point.y)) and pacman.x > point.x):
                    course = vector(10, 0)
                elif ((abs(pacman.x) + abs(point.x)) < (abs(pacman.y) +
                abs(point.y)) and pacman.x < point.x):
                    course = vector(-10, 0)
                elif ((abs(pacman.x) + abs(point.x)) > (abs(pacman.y) +
                abs(point.y)) and pacman.y > point.y):
                    course = vector(0, 10)
                elif ((abs(pacman.x) + abs(point.x)) > (abs(pacman.y) +
                abs(point.y)) and pacman.y < point.y):
                    course = vector(0, -10)
                elif ((abs(pacman.x) + abs(point.x)) > (abs(pacman.y) +
                abs(point.y)) and pacman.x == point.x):
                    if pacman.y > point.y:
                        course = vector(0, 10)
                    else:
                        course = vector(0, -10)
                elif ((abs(pacman.x) + abs(point.x)) < (abs(pacman.y) +
                abs(point.y)) and pacman.y == point.y):
                    if pacman.y > point.y:
                        course = vector(10, 0)
                    else:
                        course = vector(-10, 0)
            if valid(point + course):
                point.move(course)

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, 'red')

        update()
        for point, course in ghosts:
            "Life counter and position reset upon death"
            if abs(pacman - point) < 20:
                lives -= 1
                if lives > 0:
                    pacman.x = -40
                    pacman.y = -80

        ontimer(move(lives), 40)

    def change(x, y):
        "Change pacman and ghost aim if valid."
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(160, 180)
    writer.color('white')
    writer.write(state['score'])
    writer2.goto(-160, 180)
    writer2.color('yellow')
    writer2.write(lives)
    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')
    world()
    move(lives)
    done()


main()

from random import choice
from turtle import bgcolor, clear, up, goto, dot, update, \
    ontimer, setup, hideturtle, tracer, listen, onkey, done, Turtle
from freegames import floor, vector
from tkinter import messagebox

def main():
    state = {'score': 0}
    path = Turtle(visible=False)
    writer = Turtle(visible=False)
    writer2 = Turtle(visible=False)
    aim = vector(0, 0)
    pacman = vector(-40, -80)
    lives = 3
    ghosts = [
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]
    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]


    def square(x, y):
        "Draw square using path at (x, y)."
        path.up()
        path.goto(x, y)
        path.down()
        path.begin_fill()

        for count in range(4):
            path.forward(20)
            path.left(90)

        path.end_fill()


    def offset(point):
        "Return offset of point in tiles."
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index


    def valid(point):
        "Return True if point is valid in tiles."
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0


    def world():
        "Draw world using path."
        bgcolor('black')
        path.color('blue')

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')


    def move(lives):
        "Move pacman and all ghosts."
        writer.undo()
        writer.write(state['score'])
        writer2.undo()
        writer2.write(lives)
        Game_Over = False

        clear()

        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
        
        if state['score'] == 194:
            "Game over condition and win message"
            messagebox.showinfo("TACTI-PACMAN", "A winner is you!")
            return

        up()
        goto(pacman.x + 10, pacman.y + 10)
        if lives > 0:
            dot(20, 'yellow')
        elif lives == 0 and Game_Over == False:
            "Game Over condition and lose message"
            Game_Over = True
            messagebox.showinfo("TACTI-PACMAN", "A loser is you! \n Press Space to try again!")
            writer.undo()
            writer2.undo()
            main()
            

        for point, course in ghosts:
            
            if (state['score'] >= 0 and state['score'] < 70):
                if (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x > point.x:
                    course = vector(5, 0)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x < point.x:
                    course = vector(-5, 0)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y > point.y:
                    course = vector(0, 5)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y < point.y:
                    course = vector(0, -5)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.x == point.x:
                    if pacman.y > point.y:
                        course = vector(0, 5)
                    else:
                        course = vector(0, -5)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.y == point.y:
                    if pacman.y > point.y:
                        course = vector(5, 0)
                    else:
                        course = vector(-5, 0)
            elif (state['score'] >= 70):
                if (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x > point.x:
                    course = vector(10, 0)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x < point.x:
                    course = vector(-10, 0)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y > point.y:
                    course = vector(0, 10)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y < point.y:
                    course = vector(0, -10)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.x == point.x:
                    if pacman.y > point.y:
                        course = vector(0, 10)
                    else:
                        course = vector(0, -10)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.y == point.y:
                    if pacman.y > point.y:
                        course = vector(10, 0)
                    else:
                        course = vector(-10, 0)
            if valid(point + course):
                point.move(course)

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, 'red')

        update()
        for point, course in ghosts:
            "Life counter and position reset upon death"
            if abs(pacman - point) < 20:
                lives -= 1
                if lives > 0:
                    pacman.x = -40
                    pacman.y = -80
                
        ontimer(move(lives),40)

    def change(x, y):
        "Change pacman and ghost aim if valid."
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(160, 180)
    writer.color('white')
    writer.write(state['score'])
    writer2.goto(-160, 180)
    writer2.color('yellow')
    writer2.write(lives)
    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')
    world()
    move(lives)
    done()


main()

from turtle import bgcolor, clear, up, goto, dot, update, \
    ontimer, setup, hideturtle, tracer, listen, onkey, done, Turtle
from freegames import floor, vector
from tkinter import messagebox


def main():
    state = {'score': 0}
    path = Turtle(visible=False)
    writer = Turtle(visible=False)
    writer2 = Turtle(visible=False)
    aim = vector(0, 0)
    pacman = vector(-40, -80)
    lives = 3
    ghosts = [
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]
    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    def square(x, y):
        "Draw square using path at (x, y)."
        path.up()
        path.goto(x, y)
        path.down()
        path.begin_fill()

        for count in range(4):
            path.forward(20)
            path.left(90)
        path.end_fill()

    def offset(point):
        "Return offset of point in tiles."
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(point):
        "Return True if point is valid in tiles."
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def world():
        "Draw world using path."
        bgcolor('black')
        path.color('blue')

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')

    def move(lives):
        "Move pacman and all ghosts."
        writer.undo()
        writer.write(state['score'])
        writer2.undo()
        writer2.write(lives)
        Game_Over = False

        clear()

        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        if state['score'] == 194:
            "Game over condition and win message"
            messagebox.showinfo("TACTI-PACMAN", "A winner is you!")
            return

        up()
        goto(pacman.x + 10, pacman.y + 10)
        if lives > 0:
            dot(20, 'yellow')
        elif (lives == 0 and Game_Over is False):
            "Game Over condition and lose message"
            Game_Over = True
            messagebox.showinfo("TACTI-PACMAN", "Press Space to try again!")
            writer.undo()
            writer2.undo()
            main()

        for point, course in ghosts:

            if (state['score'] >= 0 and state['score'] < 70):
                if ((abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x > point.x):
                    course = vector(5, 0)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x < point.x:
                    course = vector(-5, 0)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y > point.y:
                    course = vector(0, 5)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y < point.y:
                    course = vector(0, -5)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.x == point.x:
                    if pacman.y > point.y:
                        course = vector(0, 5)
                    else:
                        course = vector(0, -5)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.y == point.y:
                    if pacman.y > point.y:
                        course = vector(5, 0)
                    else:
                        course = vector(-5, 0)
            elif (state['score'] >= 70):
                if (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x > point.x:
                    course = vector(10, 0)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.x < point.x:
                    course = vector(-10, 0)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y > point.y:
                    course = vector(0, 10)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.y < point.y:
                    course = vector(0, -10)
                elif (abs(pacman.x) + abs(point.x)) > (abs(pacman.y) + abs(point.y)) and pacman.x == point.x:
                    if pacman.y > point.y:
                        course = vector(0, 10)
                    else:
                        course = vector(0, -10)
                elif (abs(pacman.x) + abs(point.x)) < (abs(pacman.y) + abs(point.y)) and pacman.y == point.y:
                    if pacman.y > point.y:
                        course = vector(10, 0)
                    else:
                        course = vector(-10, 0)
            if valid(point + course):
                point.move(course)

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, 'red')

        update()
        for point, course in ghosts:
            "Life counter and position reset upon death"
            if abs(pacman - point) < 20:
                lives -= 1
                if lives > 0:
                    pacman.x = -40
                    pacman.y = -80

        ontimer(move(lives), 40)

    def change(x, y):
        "Change pacman and ghost aim if valid."
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(160, 180)
    writer.color('white')
    writer.write(state['score'])
    writer2.goto(-160, 180)
    writer2.color('yellow')
    writer2.write(lives)
    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')
    world()
    move(lives)
    done()


main()

