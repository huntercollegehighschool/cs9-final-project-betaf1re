from turtle import Turtle, Screen
from time import sleep
from grid import Grid, Player, deactivesquare_fade, activesquare_fade

FONT = "Courier"
TUTORIAL_FONT = ("Comic Sans MS", 15, "normal")


class TicTacGrow():

    def __init__(self, screen: Screen):
        self.screen = screen
        self.started = False
        self.button1 = Turtle()
        self.button2 = Turtle()
        self.drawer1 = Turtle()
        self.drawer2 = Turtle()
        self.background = Turtle()
        self.p1 = Player(1)
        self.p2 = Player(2)

        self.setup(self.button1)
        self.setup(self.button2)
        self.setup(self.drawer1)
        self.setup(self.drawer2)
        self.setup(self.background)

        self.titlescreen()

    def setup(self, turtle):
        turtle.reset()
        turtle.setundobuffer(None)
        turtle.speed(0)
        turtle.shape("square")
        turtle.hideturtle()
        turtle.up()
        turtle.pencolor("white")
        turtle.fillcolor("")

    def titlescreen(self):
        self.screen.bgcolor("black")
        sleep(1)

        self.drawer1.goto(0, 200)
        for n in range(17):
            self.drawer1.pencolor(15 * n, 15 * n, 15 * n)
            self.drawer1.write("Tic Tac Toe", align="center", font=(FONT, 50, "normal"))
            self.screen.update()
            sleep(0.02)

        sleep(1)
        self.screen.tracer(2)
        self.drawer2.goto(240, -350)
        self.drawer2.pensize(8)
        self.drawer2.pencolor("#c32147")
        self.drawer2.circle(300, -150)
        self.drawer2.down()
        self.drawer2.speed(1)
        self.drawer2.circle(300, -30)
        self.drawer2.up()
        self.drawer2.seth(0)

        grow_text = "grow text.gif"
        self.screen.register_shape(grow_text)

        sleep(0.5)
        self.screen.tracer(1)
        self.button1.goto(200, 305)
        self.background.goto(220, 305)
        self.button1.color("black")
        self.button1.right(10)
        self.background.right(10)
        self.button1.turtlesize(4, 10)
        self.background.shape(grow_text)
        self.button1.showturtle()
        self.background.showturtle()
        self.button1.speed(2)
        self.button1.fd(200)
        self.screen.tracer(0)

        self.play_text = "play text.gif"
        self.screen.register_shape(self.play_text)

        sleep(1)
        self.button1.speed(0)
        self.button1.shape(self.play_text)
        self.button1.goto(-200, -75)
        self.button2.turtlesize(5, 11, 5)
        self.button2.goto(205, -95)
        self.button2.write("Tutorial", align="center", font=(FONT, 30, "normal"))
        self.button2.goto(203, -75)
        self.drawer1.goto(0, -75)
        self.drawer1.turtlesize(4, 60)
        self.drawer1.color("black")
        self.drawer1.showturtle()
        self.drawer1.speed(2)
        self.screen.tracer(1)
        self.drawer1.fd(1000)

        self.screen.tracer(0)
        self.drawer1.fillcolor("")
        self.drawer1.pensize(5)
        self.drawer1.hideturtle()
        self.drawer2.pensize(5)
        self.drawer2.pencolor("white")

        self.button1.onclick(self.start_game)
        self.button2.onclick(self.tutorial)
        self.button2.pencolor("")
        self.button2.showturtle()
        self.titlescreen_animation()

    def titlescreen_animation(self):
        if self.started:
            return

        lengths = [200, 100, 200, 100]
        lengths2 = [220, 100, 220, 100]

        self.drawer1.goto(-300, -25)
        self.drawer1.pencolor('#D8E9F0')
        self.drawer1.down()
        self.screen.tracer(1, 15)

        for n in range(4):
            self.drawer1.speed(3)
            self.drawer1.fd(lengths[n])
            self.drawer1.speed(0)
            self.drawer1.right(90)

        self.screen.tracer(0)
        self.drawer1.speed(0)

        for n in range(1, 18):
            self.drawer1.pencolor(int(121 - (121 / 17) * n), int(126 - (126 / 17) * n), int(246 - (246 / 17) * n))
            for n in range(4):
                self.drawer1.fd(lengths[n])
                self.drawer1.right(90)
            self.screen.update()
        self.drawer1.up()

        if self.started:
            return

        self.drawer2.goto(93, -25)
        self.drawer2.pencolor("#D8E9F0")
        self.drawer2.down()
        self.screen.tracer(1, 15)

        for n in range(4):
            self.drawer2.speed(3)
            self.drawer2.fd(lengths2[n])
            self.drawer2.speed(0)
            self.drawer2.right(90)

        self.screen.tracer(0)
        self.drawer2.speed(0)

        for n in range(1, 18):
            self.drawer2.pencolor(255 - 15 * n, 255 - 15 * n, 255 - 15 * n)
            for n in range(4):
                self.drawer2.fd(lengths2[n])
                self.drawer2.right(90)
            self.screen.update()
        self.drawer2.up()

        if not self.started:
            self.screen.ontimer(self.titlescreen_animation, 2000)

    def tutorial(self, x, y):
        self.title_clear()
        self.grid = Grid(self.screen, self.p1, self.p2, self)
        self.grid.gameover = True

        arrow_l = "arrow_left.gif"
        self.arrow_r = "arrow_right.gif"
        self.screen.register_shape(arrow_l)
        self.screen.register_shape(self.arrow_r)
        self.button1.shape(arrow_l)
        self.button2.shape(self.arrow_r)

        self.button1.goto(-200, -300)
        self.button2.goto(200, -300)
        self.button1.showturtle()
        self.button2.showturtle()
        self.button1.onclick(self.prev)
        self.button2.onclick(self.next)

        self.background.color("#D8E9F0")
        self.background.shape("square")
        self.background.seth(0)
        self.background.turtlesize(10, 90)
        self.background.showturtle()

        self.tutorial_num = 0
        self.tutorial_highestnum = 0
        self.tutorial_pause = False
        self.screen.update()
        self.tutorial_cont()

    def prev(self, x, y):
        if self.tutorial_pause or self.tutorial_num <= 0:
            return
        self.tutorial_num -= 1
        self.tutorial_cont()

    def next(self, x, y):
        if self.tutorial_pause:
            return
        if self.tutorial_num >= 8:
            self.tutorial_num = 0
        self.tutorial_num += 1
        self.tutorial_cont()

    def tutorial_cont(self):
        self.tutorial_pause = True

        if self.tutorial_highestnum < self.tutorial_num:
            self.tutorial_highestnum = self.tutorial_num

        self.screen.tracer(0)
        self.background.goto(450, 300)
        self.drawer1.goto(-415, 250)
        self.drawer1.pencolor("#494953")
        self.drawer1.clear()

        if self.tutorial_highestnum == 8:
            self.button2.shape(self.arrow_r)
            self.button2.onclick(self.next)

        if self.tutorial_num == 0:
            self.drawer1.write("Welcome to Tic Tac Grow! Press the arrow buttons at the bottom to navigate this tutorial.", font=TUTORIAL_FONT)
        elif self.tutorial_num == 1:
            self.drawer1.write("This game is identical to Tic Tac Toe, with two groundbreaking twists. You win by "
                               "getting\n4 in a row instead of 3, and every time you move, you also add a square to the grid.",
                               font=TUTORIAL_FONT)
        elif self.tutorial_num == 2:
            self.drawer1.write("That rule excludes the first move, where the first player does NOT add a square for\nbalance reasons.",
                               font=TUTORIAL_FONT)
        elif self.tutorial_num == 3:
            self.drawer1.write("The two players alternate turns. On each turn, they will make a move and THEN\nadd a square.",
                               font=TUTORIAL_FONT)
        elif self.tutorial_num == 4:
            self.drawer1.write("These smaller gray squares represent possible places where you can add a square.\nYou can only add"
                               " a square to the grid horizontally or vertically.",
                               font=TUTORIAL_FONT)
        elif self.tutorial_num == 5:
            self.drawer1.write("They'll also change color based on the turn; if it's no one's turn to expand, they're gray. "
                               "\nIf it's player 1's turn to expand, they're tinted red, and they're tinted blue for player 2.",
                               font=TUTORIAL_FONT)
        elif self.tutorial_num == 6:
            self.drawer1.write("With these rules in place, there's a huge number of ways you can out-think and\nout-strategize"
                               " your opponent to win by 4 in a row.",
                               font=TUTORIAL_FONT)
        elif self.tutorial_num == 7:
            self.drawer1.write("In this particular program, there'll also be some bugs here and there because I had to rush\nthis"
                               " in 2 days due to procrastination, ehe (just graphics bugs, not actual functionality)",
                               font=TUTORIAL_FONT)
        elif self.tutorial_num == 8:
            self.drawer1.write("This program does not support more than 2 players and also does not support 1 player since "
                               "I'm\nnot smart enough to write such a complex AI. With that, press Play to enter into the game!",
                               font=TUTORIAL_FONT)

        self.screen.tracer(1, 10)
        self.background.speed(3)
        self.background.fd(900)
        self.background.speed(0)
        self.screen.tracer(0)

        if self.tutorial_highestnum == self.tutorial_num:

            def filler():
                pass

            self.grid.gameover = False
            if self.tutorial_num == 2:
                sleep(1.25)
                self.grid.squares[0].squareplayed(None, None)
                self.screen.ontimer(filler, 1000)
                self.grid.squares[1].squareplayed(None, None)
                self.screen.ontimer(filler, 1000)
                self.grid.squares[10].squareadded(None, None)
            elif self.tutorial_num == 3:
                sleep(1.25)
                self.grid.squares[4].squareplayed(None, None)
                self.screen.ontimer(filler, 1000)
                self.grid.squares[15].squareadded(None, None)
                self.screen.ontimer(filler, 1000)
                self.grid.squares[3].squareplayed(None, None)
                self.screen.ontimer(filler, 1000)
                self.grid.squares[13].squareadded(None, None)
            elif self.tutorial_num == 5:
                sleep(1.25)
                self.grid.squares[10].squareplayed(None, None)
                self.screen.ontimer(filler, 3000)
                self.grid.squares[17].squareadded(None, None)
                self.screen.ontimer(filler, 1000)
                self.grid.squares[17].squareplayed(None, None)
                self.screen.ontimer(filler, 3000)
                self.grid.squares[19].squareadded(None, None)

            self.grid.gameover = True

        if self.tutorial_num == 8:
            self.button2.shape(self.play_text)
            self.button2.onclick(self.tutorial_finish)
            self.screen.update()
        self.tutorial_pause = False

    def tutorial_finish(self, x, y):
        self.screen.tracer(0, 10)

        for move in self.p1.moves:
            move.reset()
            move.hideturtle()
        for move in self.p2.moves:
            move.reset()
            move.hideturtle()

        self.p1.move_coords = []
        self.p2.move_coords = []
        self.p1.moves = []
        self.p2.moves = []
        self.button1.onclick(None)
        self.button2.onclick(None)
        self.button1.shape("square")
        self.button2.shape("square")
        self.button1.hideturtle()
        self.button2.hideturtle()
        self.background.hideturtle()
        self.drawer1.clear()

        for n in range(15):
            for square in self.grid.squares:
                if square.active:
                    square.pencolor(activesquare_fade[n])
                else:
                    square.pencolor(deactivesquare_fade[n])
            self.screen.update()
            sleep(0.02)

        for square in self.grid.squares:
            square.reset()
            square.hideturtle()

        self.grid = Grid(self.screen, self.p1, self.p2, self)

    def start_game(self, x, y):
        self.title_clear()
        self.screen.tracer(0, 10)
        self.grid = Grid(self.screen, self.p1, self.p2, self)

    def title_clear(self):
        self.started = True
        self.button1.onclick(None)
        self.button2.onclick(None)
        self.drawer1.up()
        self.drawer2.up()

        self.screen.tracer(0)

        self.button2.hideturtle()
        self.button2.goto(0, 900)
        self.button2.turtlesize(45, 60)
        self.button2.color("black")
        self.button2.speed(3)
        self.button2.showturtle()

        self.screen.tracer(1)
        self.button2.goto(0, 0)
        self.screen.tracer(0)

        self.drawer1.hideturtle()
        self.drawer2.hideturtle()
        self.button1.hideturtle()
        self.background.hideturtle()

    def end_screen(self, winner: int, move_coords: list, coords_list: list):
        x_coords = [n[0] for n in move_coords]
        y_coords = [n[1] for n in move_coords]

        x_highest = max(x_coords) + 50
        x_lowest = min(x_coords) - 50
        y_highest = max(y_coords) + 50
        y_lowest = min(y_coords) - 50

        if x_highest < 100:
            x_highest = 100
        if x_lowest > -100:
            x_lowest = -100
        if y_highest < 100:
            y_highest = 100
        if y_lowest > -100:
            y_lowest = -100

        dist_x = x_highest - x_lowest
        dist_y = y_highest - y_lowest
        dists = [dist_x, dist_y, dist_x, dist_y]

        self.screen.tracer(0)
        self.drawer1.reset()
        self.drawer2.reset()
        self.drawer1.hideturtle()
        self.drawer2.hideturtle()
        self.drawer1.up()
        self.drawer2.up()

        def line():
            self.screen.tracer(1)
            self.drawer1.speed(3)
            self.drawer1.down()
            self.drawer1.fd(150)
            self.drawer1.up()
            self.drawer1.speed(0)
            self.screen.tracer(0)

        self.drawer1.pensize(3)
        self.drawer1.pencolor("#494953")

        self.drawer1.goto(-75, 25)
        self.drawer1.seth(0)
        line()
        self.drawer1.goto(-75, -25)
        line()
        self.drawer1.goto(-25, 75)
        self.drawer1.seth(270)
        line()
        self.drawer1.goto(25, 75)
        line()

        def sort_key(n):
            return n[0]

        coords_list.sort(key=sort_key)
        self.drawer1.pensize(7)
        if winner == 1:
            self.drawer1.pencolor("#C32147")
        else:
            self.drawer1.pencolor("#797EF6")
        self.drawer1.goto(coords_list[0])
        self.drawer1.down()

        for n in range(len(coords_list)):
            self.drawer1.goto(coords_list[n])
            self.drawer1.speed(10 - 1.25 * n)
        self.screen.update()
        self.drawer1.up()
        self.drawer1.speed(0)

        self.drawer1.pensize(7)
        self.drawer1.pencolor("black")
        self.drawer1.goto(x_lowest, y_highest)
        self.drawer1.seth(0)
        self.drawer1.down()

        self.screen.tracer(1)
        for x in range(4):
            self.drawer1.speed(3)
            self.drawer1.fd(dists[x])
            self.drawer1.speed(0)
            self.drawer1.right(90)

        sleep(1)

        self.screen.tracer(0)
        for n in range(1, 35):
            self.drawer1.pencolor(int(7.5 * n), int(7.5 * n), int(7.5 * n))
            for x in range(4):
                self.drawer1.fd(dists[x])
                self.drawer1.right(90)
            self.screen.bgcolor(255 - int(7.5 * n), 255 - int(7.5 * n), 255 - int(7.5 * n))
            self.screen.update()

        if winner == 1:
            win_text = "player 1 wins.gif"
        else:
            win_text = "player 2 wins.gif"
        self.screen.register_shape(win_text)

        self.background.shape(win_text)
        y = 300
        y2 = -300
        if y_highest > 300:
            y = y_highest + 75
        elif y_highest > 200:
            y = y_highest + 100
        if y_lowest < -300:
            y2 = y_lowest - 75
        elif y_lowest < -200:
            y2 = y_lowest - 100

        self.background.goto(0, y)
        self.button2.goto(0, y)
        self.button2.color("black")
        self.button2.turtlesize(4, 20)
        self.button2.speed(2)
        self.button2.showturtle()
        self.background.showturtle()

        self.screen.tracer(1)
        self.button2.fd(500)
        self.screen.tracer(0)

        self.playagain_text = "play again.gif"
        self.screen.register_shape(self.playagain_text)

        self.button1.goto(-205, y2)
        self.button2.goto(-205, y2)
        self.button1.shape(self.playagain_text)
        self.button2.showturtle()
        self.button1.showturtle()

        self.screen.tracer(1)
        self.button2.fd(500)
        self.screen.tracer(0)

        self.button2.hideturtle()
        self.button2.goto(205, y2-20)

        for n in range(1, 35):
            self.button2.color(int(7.5*n), int(7.5*n), int(7.5*n))
            self.button2.write("Exit & Finish", align="center", font=(FONT, 30, "normal"))
            self.screen.update()
        self.button2.goto(203, y2)
        self.button2.color("")
        self.button2.showturtle()
        self.screen.update()

        self.button1.onclick(self.restart_game)
        self.button2.onclick(self.credits)

    def restart_game(self, x, y):
        for move in self.p1.moves:
            move.reset()
            move.hideturtle()
        for move in self.p2.moves:
            move.reset()
            move.hideturtle()
        for square in self.grid.squares:
            square.reset()
            square.hideturtle()
        self.grid.drawer.reset()
        self.grid.drawer.hideturtle()

        self.p1.move_coords = []
        self.p2.move_coords = []
        self.p1.moves = []
        self.p2.moves = []

        self.start_game(None, None)

    def credits(self, x, y):
        self.title_clear()
        for move in self.p1.moves:
            move.reset()
            move.hideturtle()
        for move in self.p2.moves:
            move.reset()
            move.hideturtle()
        self.drawer1.clear()
        self.grid.drawer.clear()
        self.button2.clear()
        self.button2.color("black")
        self.button2.speed(5)
        self.button2.goto(1200, 0)
        self.button2.showturtle()

        def text_fadein(text: str, sleeptime=0, fontsize=25):
            for n in range(1, 35):
                self.drawer1.color(int(7.5 * n), int(7.5 * n), int(7.5 * n))
                self.drawer1.write(text, align="center", font=("Comic Sans MS", fontsize, "normal"))
                self.screen.update()
                sleep(0.01)
            if sleeptime > 0:
                sleep(float(sleeptime))
                text_fadeout(text)

        def text_fadeout(text: str):
            for n in range(1, 35):
                self.drawer1.color(255-int(7.5*n), 255-int(7.5*n), 255-int(7.5*n))
                self.drawer1.write(text, align="center", font=("Comic Sans MS", 25, "normal"))
                self.screen.update()
                sleep(0.01)
            self.drawer1.clear()
            self.screen.update()

        def scrolltext(text: str, color):
            self.button2.turtlesize(4, 60)
            self.drawer1.pencolor(color)
            self.drawer1.write(text, align="center", font=("Courier", 25, "normal"))
            self.button2.goto(self.drawer1.pos())
            self.screen.tracer(1)
            self.button2.fd(1200)
            self.screen.tracer(0)

        def scrolltext_out():
            self.button2.turtlesize(80, 60)
            self.button2.goto(-1200, self.drawer1.ycor())
            self.screen.tracer(1)
            self.button2.fd(1200)
            self.screen.tracer(0)
            self.drawer1.clear()
            self.button2.goto(1200, 0)

        self.drawer1.goto(0, 0)
        text_fadein("Credits", 2)
        sleep(1.5)

        self.drawer1.goto(0, 150)
        text_fadein("for inventing the game through sheer innovation")
        sleep(1.5)
        self.drawer1.goto(0, -50)
        scrolltext("Wrye Bolgatz", "#797EF6")
        self.drawer1.goto(0, -150)
        scrolltext("Grisha London", "#C32147")
        sleep(1.5)
        scrolltext_out()
        sleep(1)

        self.drawer1.goto(0, 150)
        text_fadein("for creating and refining this project")
        sleep(1.5)
        self.drawer1.goto(0, -50)
        scrolltext("Leo Ni", "#797EF6")
        self.drawer1.goto(0, -150)
        scrolltext("Olam Ho", "#C32147")
        sleep(1.5)
        scrolltext_out()
        sleep(1)

        self.drawer1.goto(0, 100)
        text_fadein("for developing this project")
        sleep(1.5)
        self.drawer1.goto(0, -100)
        scrolltext("Leo Ni", "light gray")
        sleep(1.5)
        scrolltext_out()
        sleep(1)

        self.drawer1.goto(0, 250)
        text_fadein("for playtesting and advising along the way")
        sleep(1.5)
        self.drawer1.goto(0, 50)
        scrolltext("Wrye Bolgatz", "light gray")
        self.drawer1.goto(0, -50)
        scrolltext("Leo Ni", "light gray")
        self.drawer1.goto(0, -150)
        scrolltext("Olam Ho", "light gray")
        self.drawer1.goto(0, -250)
        scrolltext("Zoe Ni", "light gray")
        sleep(1.5)
        scrolltext_out()
        sleep(1)

        ss = "credits_screenshot.gif"
        self.screen.register_shape(ss)
        self.button1.shape(ss)
        self.button1.goto(0, 500)
        self.screen.tracer(1)
        self.button1.speed(1)
        self.button1.showturtle()
        self.button1.goto(0, -500)
        self.screen.tracer(0)
        self.button1.hideturtle()

        self.drawer1.goto(0, 350)
        text_fadein("for emotional and moral support")
        sleep(1.5)
        self.drawer1.goto(0, 150)
        scrolltext("Olam Ho", "light gray")
        self.drawer1.goto(0, 50)
        scrolltext("Alyosha Vak", "light gray")
        self.drawer1.goto(0, -50)
        scrolltext("Cal Chen", "light gray")
        self.drawer1.goto(0, -150)
        scrolltext("Sophia Li", "light gray")
        self.drawer1.goto(0, -250)
        scrolltext("Diya Mangaraj", "light gray")
        self.drawer1.goto(0, -350)
        scrolltext("Zoe Ni", "light gray")
        sleep(1.5)
        scrolltext_out()

        finalcredits = "finalcredits.gif"
        self.screen.register_shape(finalcredits)
        self.button1.shape(finalcredits)

        sleep(0.5)

        self.button1.goto(0, -1475)
        self.button1.speed(1)
        self.button1.showturtle()
        self.screen.tracer(1, 15)
        self.button1.goto(0, 1200)

        self.screen.tracer(0)

        self.button2.hideturtle()
        self.button2.turtlesize(2.5, 2.5, 5)
        self.button2.pencolor("white")
        self.button2.goto(-275, -165)
        self.button2.showturtle()

        self.drawer1.goto(150, -200)
        text_fadein("I have read and agreed to the\nTerms of Use and Privacy Policy", fontsize=20)

        self.button2.onclick(self.end)

    def end(self, x, y):
        self.screen.clear()

        end = Turtle()
        end.hideturtle()
        end.up()

        end.goto(0, 0)
        end.write("LIAR", align="center", font=("Times New Roman", 60, "normal"))

        self.screen.update()
        sleep(0.5)
        self.screen.bye()