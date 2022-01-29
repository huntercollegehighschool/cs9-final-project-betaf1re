from master import TicTacGrow
from turtle import Screen


screen = Screen()
screen.title("Tic Tac Grow")
screen.setup(1200, 900)
screen.colormode(255)
screen.tracer(0)

TicTacGrow(screen)


screen.mainloop()