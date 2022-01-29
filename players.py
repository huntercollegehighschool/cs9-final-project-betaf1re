from turtle import Turtle


class PlayerMove(Turtle):

    def __init__(self, player_number):
        super().__init__()
        self.setundobuffer(None)
        self.pensize(3)
        self.speed(0)
        self.up()
        self.hideturtle()
        self.player = player_number
        if self.player == 1:
            self.pencolor("#C32147")
        elif self.player == 2:
            self.pencolor("#797EF6")

    def draw_icon(self, screen):
        x = self.xcor()
        y = self.ycor()
        screen.tracer(1)
        if self.player == 1:
            self.goto(x - 15, y + 15)
            self.right(45)
            self.speed(1)
            self.down()
            self.fd(42.426)
            self.up()
            self.speed(0)
            self.goto(x-15, y-15)
            self.left(90)
            self.speed(1)
            self.down()
            self.fd(42.426)
            self.up()
            self.speed(10)
        elif self.player == 2:
            self.screen.tracer(1, 5)
            self.goto(x, y+15)
            self.speed(10)
            self.down()
            self.circle(-15.5)
            self.up()
            self.speed(1)
        self.goto(x, y)
        screen.tracer(0, 10)


class Player():

    def __init__(self, player_num):
        self.player = player_num
        self.move_coords = []
        self.win_coords = []
        self.moves = []

        if player_num not in [1, 2]:
            raise Exception("Only two players have been implemented!")

    def move(self, grid_square: Turtle, screen):
        pos = grid_square.pos()
        playermove = PlayerMove(self.player)
        playermove.goto(pos)
        self.move_coords.append(pos)
        self.moves.append(playermove)
        playermove.draw_icon(screen)

        if self.player == 2 and not grid_square.mastergrid.expansion:
            grid_square.mastergrid.expansion = True
            grid_square.mastergrid.start_expansion()
            grid_square.mastergrid.inplay = True

        if self.check_win(playermove):
            move_coords = grid_square.mastergrid.p1.move_coords
            move_coords += grid_square.mastergrid.p2.move_coords
            grid_square.mastergrid.victory(self.player, self.win_coords, move_coords)

    def check_win(self, move: PlayerMove):
        x = move.xcor()
        y = move.ycor()
        in_row = 0
        self.win_coords = []

        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(move.xcor()+50, y)
        move.goto(x-50, y)
        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(move.xcor()-50, y)

        move.goto(x, y)
        if in_row >= 4:
            return True

        in_row = 0
        self.win_coords = []
        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(x, move.ycor()+50)
        move.goto(x, y-50)
        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(x, move.ycor()-50)

        move.goto(x, y)
        if in_row >= 4:
            return True

        in_row = 0
        self.win_coords = []
        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(move.xcor()+50, move.ycor()+50)
        move.goto(x-50, y-50)
        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(move.xcor()-50, move.ycor()-50)

        move.goto(x, y)
        if in_row >= 4:
            return True

        in_row = 0
        self.win_coords = []
        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(move.xcor()+50, move.ycor()-50)
        move.goto(x-50, y+50)
        while move.pos() in self.move_coords:
            in_row += 1
            self.win_coords.append(move.pos())
            move.goto(move.xcor()-50, move.ycor()+50)

        move.goto(x, y)
        return in_row >= 4