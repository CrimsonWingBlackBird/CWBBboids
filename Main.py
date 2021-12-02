from tkinter import *
import numpy as np
from boid import Boid

sizeX = 1000
sizeY = 1000
flock = [Boid(*np.random.rand(2)*1000, sizeX, sizeY) for _ in range(30)]

root = Tk()
root.title('Boids')

newInstanceFlag = False


def restart():
    global newInstanceFlag
    newInstanceFlag = True


restartButton = Button(root, text="Restart Simulation", command=restart)
restartButton.pack()
c = Canvas(root, width=sizeX, height=sizeY)
c.pack()


def App(canvas):
    canvas.delete("all")
    global flock
    global newInstanceFlag
    for boid in flock:
        boid.show(canvas)
        boid.behavior(flock)
        boid.edges()
        boid.update()
    if newInstanceFlag is not True:
        root.after(25, lambda: App(canvas))
    else:
        flock = [Boid(*np.random.rand(2)*1000, sizeX, sizeY)
                 for _ in range(30)]
        newInstanceFlag = False
        root.after(1, lambda: App(canvas))


App(c)
root.mainloop()
