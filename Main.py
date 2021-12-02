from tkinter import *
import numpy as np
from boid import Boid

# Sets the size of the simulation environment
sizeX = 1000
sizeY = 1000

# Initializes the flock of boids
numberOfBoids = 30
rng = np.random.default_rng()
flock = [Boid(rng.random()*sizeX, rng.random()*sizeY, sizeX, sizeY)
         for _ in range(numberOfBoids)]

# Makes the window
root = Tk()
root.title('Boids')


# This block controls the reset flag
resetFlag = False


def restart():
    global resetFlag
    resetFlag = True


# Adds the restart button to the window
restartButton = Button(root, text="Restart Simulation", command=restart)
restartButton.pack()

# Adds the simulation enviroment to the window
c = Canvas(root, width=sizeX, height=sizeY)
c.pack()


# Draws the boids, applies behavior and updates the boids.
# Restarts the simulation if the reset flag is on.
def App(canvas):
    canvas.delete("all")
    global flock
    global resetFlag
    for boid in flock:
        boid.show(canvas)
        boid.behavior(flock)
        boid.edges()
        boid.update()
    if resetFlag is not True:
        root.after(25, lambda: App(canvas))
    else:
        flock = [Boid(*np.random.rand(2)*1000, sizeX, sizeY)
                 for _ in range(30)]
        resetFlag = False
        root.after(1, lambda: App(canvas))


# Initializes the simulation
App(c)
root.mainloop()
