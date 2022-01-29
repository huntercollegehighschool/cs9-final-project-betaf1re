from turtle import Turtle
from players import Player, PlayerMove
from time import sleep


activesquare_fade = ["#494953", "#52535e", "#5b5e68", "#656873", "#6e737e", "#787e89", "#828a94", "#8c959f",
                     "#97a1ab", "#a1acb6", "#acb8c2", "#b6c4cd", "#c1d0d9", "#cddde4", "#d8e9f0"]
deactivesquare_fade = ["#d3d3d3", "#d3d5d5", "#d4d6d7", "#d4d8d9", "#d5d9db", "#d5dbdd", "#d5dcdf", "#d6dee1",
                       "#d6e0e3", "#d6e1e6", "#d7e3e8", "#d7e4ea", "#d7e6ec", "#d8e7ee", "#d8e9f0"]
blue_fade = ["#fcc201", "#ffb31b", "#ffa431", "#ff9445", "#ff8558", "#ff776c", "#ff6b80", "#ff6395",
            "#ff5fa8", "#ff60bb", "#f864cd", "#e06adc", "#c371e8", "#a278f1", "#797ef6"]
red_fade = ["#fcc201", "#fdb604", "#fdaa0b", "#fd9e13", "#fb931b", "#f98721", "#f67b27", "#f2702c",
             "#ee6431", "#e85936", "#e24e3a", "#db433e", "#d43841", "#cc2d44", "#c32147"]
gray_red_fade = ["#d3d3d3", "#d4cccd", "#d5c6c6", "#d5bfc0", "#d6b9b9", "#d6b2b3"]
gray_blue_fade = ["#d3d3d3", "#cecdd6", "#c9c6d9", "#c4c0db", "#bebade", "#b9b4e0"]

start_fade = ["#000000", "#001318", "#0f1d22", "#19272c", "#233136", "#2d3b41", "#38464c", "#435157", "#4e5d63",
              "#5a696f", "#65757b", "#718187", "#7d8d94", "#8a9aa0", "#96a7ad", "#a3b3ba", "#b0c1c7", "#bdced5",
              "#cbdbe2", "#d8e9f0"]


class Square(Turtle):

    def __init__(self, player1=None, player2=None):
        super().__init__(shape="square")
        self.setundobuffer(None)
        self.speed(0)
        self.up()
        self.turtlesize(2, 2, 3)
        self.fillcolor("")
        self.deactivate()
        self.player1 = player1
        self.player2 = player2
        self.currentplayer = 1
        self.mastergrid: Grid

    def activate(self):
        self.active = True
        self.pencolor("#494953")
        self.turtlesize(2.5, 2.5)
        self.onclick(self.squareplayed)

    def deactivate(self):
        self.active = False
        self.pencolor("light gray")
        self.turtlesize(2, 2)
        self.onclick(self.squareadded)

    def squareplayed(self, x, y):
        if not self.mastergrid.inplay and not self.mastergrid.gameover:
            self.mastergrid.inplay = self.mastergrid.expansion
            self.onclick(None)
            current = self.mastergrid.currentplayer
            self.mastergrid.currentplayer = [0, 2, 1][current]

            if current == 1:
                self.mastergrid.p1.move(self, self.mastergrid.screen)
                fade = gray_red_fade
            elif current == 2:
                self.mastergrid.p2.move(self, self.mastergrid.screen)
                fade = gray_blue_fade

            if self.mastergrid.expansion:
                for color in fade:
                    for square in self.mastergrid.squares:
                        if not square.active:
                            square.pencolor(color)
                    self.mastergrid.screen.update()
                    sleep(0.075)

    def squareadded(self, x, y):
        if self.mastergrid.inplay and not self.mastergrid.gameover:
            self.mastergrid.inplay = False
            self.hideturtle()
            self.mastergrid.addsquare_animate(self.xcor(), self.ycor())
            self.showturtle()
            self.activate()
            self.mastergrid.expand(self)

            if self.mastergrid.currentplayer == 2:
                fade = gray_red_fade
            else:
                fade = gray_blue_fade

            for color in fade[::-1]:
                for square in self.mastergrid.squares:
                    if not square.active:
                        square.pencolor(color)
                self.mastergrid.screen.update()
                sleep(0.075)


class Grid():

    def __init__(self, screen, player1:Player, player2:Player, announcer:Turtle):
        self.squares = []
        self.expansion = False
        self.inplay = False
        self.gameover = False
        self.grid_coords = []
        self.screen = screen
        self.p1 = player1
        self.p2 = player2
        self.currentplayer = 1
        self.announcer = announcer
        self.drawer_initiate()

        announcer.drawer1.clear()
        announcer.drawer2.clear()
        announcer.button2.clear()

        self.screen.bgcolor("#D8E9F0")
        for color in start_fade:
            self.announcer.button2.color(color)
            self.screen.update()
            sleep(0.0175)
        self.announcer.button2.hideturtle()

        coords = [(0, 0), (50, 0), (-50, 0), (0, 50), (50, 50), (-50, 50), (0, -50), (50, -50), (-50, -50)]
        for n in range(9):
            square = Square()
            square.activate()
            square.goto(coords[n])
            self.setup(square)

        sleep(1.5)
        for n in activesquare_fade[::-1]:
            for square in self.squares:
                square.pencolor(n)
            self.screen.update()
            sleep(0.03)

    def start_expansion(self):
        coords = [(-100, -50), (-100, 0), (-100, 50), (-50, 100), (0, 100), (50, 100), (100, 50), (100, 0), (100, -50), (50, -100), (0, -100), (-50, -100)]
        for n in range(12):
            square = Square()
            square.goto(coords[n])
            self.setup(square)

        for n in deactivesquare_fade[::-1]:
            for square in self.squares:
                if not square.active:
                    square.pencolor(n)
            self.screen.update()
            sleep(0.02)

    def drawer_initiate(self):
        self.drawer = Turtle()
        self.drawer.setundobuffer(None)
        self.drawer.hideturtle()
        self.drawer.left(90)
        self.drawer.up()

    def addsquare_animate(self, x, y):
        self.drawer.pensize(3)
        self.drawer.pencolor("#494953")
        self.screen.tracer(1)
        self.drawer.goto(x+25, y-25)
        self.drawer.down()
        for _ in range(4):
            self.drawer.speed(3)
            self.drawer.fd(50)
            self.drawer.speed(0)
            self.drawer.left(90)
        self.drawer.up()
        self.screen.tracer(0)
        self.drawer.clear()

    def setup(self, square):
        square.mastergrid = self
        self.squares.append(square)
        self.grid_coords.append(square.pos())

    def expand(self, target):
        x = target.xcor()
        y = target.ycor()

        if (x+50, y) not in self.grid_coords:
            square = Square()
            square.goto(x + 50, y)
            self.setup(square)
        if (x-50, y) not in self.grid_coords:
            square = Square()
            square.goto(x - 50, y)
            self.setup(square)
        if (x, y+50) not in self.grid_coords:
            square = Square()
            square.goto(x, y + 50)
            self.setup(square)
        if (x, y-50) not in self.grid_coords:
            square = Square()
            square.goto(x, y - 50)
            self.setup(square)

        self.screen.update()

    def victory(self, playernum, coords_list: list, move_coords: list):
        self.gameover = True

        def sort_key(n):
            return n[0]

        coords_list.sort(key=sort_key)
        self.drawer.pensize(7)
        self.drawer.pencolor("#FCC201")
        self.drawer.goto(coords_list[0])
        self.drawer.down()

        sleep(1)

        self.screen.tracer(1)
        for n in range(len(coords_list)):
            self.drawer.goto(coords_list[n])
            self.drawer.speed(10-1.25*n)
        self.drawer.up()
        self.drawer.speed(0)
        self.screen.tracer(0)

        if playernum == 1:
            victoryline_fade = red_fade
        elif playernum == 2:
            victoryline_fade = blue_fade

        sleep(3)
        for n in range(15):

            for square in self.squares:
                if square.active:
                    square.pencolor(activesquare_fade[n])
                else:
                    square.pencolor(deactivesquare_fade[n])
                if n == 14:
                    square.goto(-1000, -1000)

            self.drawer.goto(coords_list[0])
            self.drawer.down()
            self.drawer.pencolor(victoryline_fade[n])
            for n in range(len(coords_list)):
                self.drawer.goto(coords_list[n])
            self.screen.update()

            sleep(0.025)

        sleep(2)
        self.announcer.end_screen(playernum, move_coords, coords_list)