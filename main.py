from master import TicTacGrow
from turtle import Screen


#note: running this through replit makes it super weird and buggy (at least from my experience) + replit doesn't support most of the fonts used here so the tutorial will be messed up


screen = Screen()
screen.title("Tic Tac Grow")
screen.setup(1200, 900)
screen.colormode(255)
screen.tracer(0)

TicTacGrow(screen)


screen.mainloop()
