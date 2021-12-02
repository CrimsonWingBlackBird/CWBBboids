from tkinter import *
import numpy as np
from boid import Boid

# Sets the size of the simulation environment
sizeX = 1000
sizeY = 1000

# Simulation Parameters
numberOfBoids = 50
cohesionStrength = 0.05
seperationStrength = 0.20
alignmentStrength = 0.05
speedLimit = 10

# Defines short name for random numbers
rng = np.random.default_rng()

# Makes the window
root = Tk()
root.title('Boids')


# This block controls the reset flag
resetFlag = False


def restart():
    global resetFlag
    resetFlag = True


# Adds the restart button to the window
menuBar = Menu(root)
restartMenu = Menu(menuBar, tearoff=0)
restartMenu.add_command(label="Restart Boids", command=restart)
menuBar.add_cascade(label="Restart", menu=restartMenu)


# Starts the Simulation
def startSimulation():
    global numberOfBoids
    global cohesionStrength
    global seperationStrength
    global alignmentStrength
    global speedLimit
    global flock

    # Sets simulation parameters
    if inputBox1.get() != '':
        numberOfBoids = int(inputBox1.get())
    if inputBox2.get() != '':
        cohesionStrength = int(inputBox2.get())
    if inputBox3.get() != '':
        seperationStrength = int(inputBox3.get())
    if inputBox4.get() != '':
        alignmentStrength = int(inputBox4.get())
    if inputBox5.get() != '':
        speedLimit = int(inputBox5.get())

    # Removes input information
    inputLabel1.grid_forget()
    inputLabel2.grid_forget()
    inputLabel3.grid_forget()
    inputLabel4.grid_forget()
    inputLabel5.grid_forget()
    inputBox1.grid_forget()
    inputBox2.grid_forget()
    inputBox3.grid_forget()
    inputBox4.grid_forget()
    inputBox5.grid_forget()
    startButton.grid_forget()

    # Start simulation
    flock = [Boid(rng.random()*sizeX, rng.random()*sizeY, sizeX, sizeY)
             for _ in range(numberOfBoids)]
    c = Canvas(root, width=sizeX, height=sizeY)
    c.grid(row=0, column=0)
    App(c)


# Definitions for input box labels
inputLabel1 = Label(root, text="Number of Boids:")
inputLabel2 = Label(root, text="Cohesion Strength:")
inputLabel3 = Label(root, text="Seperation Strength:")
inputLabel4 = Label(root, text="Alignment Strength:")
inputLabel5 = Label(root, text="Speed Limit:")

# Defines the input boxes
inputBox1 = Entry(root)
inputBox2 = Entry(root)
inputBox3 = Entry(root)
inputBox4 = Entry(root)
inputBox5 = Entry(root)

# Defines the start simulation Button
startButton = Button(root, text="Start Simulation!", command=startSimulation)

# Puts up the input screen
inputLabel1.grid(row=0, column=0)
inputLabel2.grid(row=1, column=0)
inputLabel3.grid(row=2, column=0)
inputLabel4.grid(row=3, column=0)
inputLabel5.grid(row=4, column=0)

inputBox1.grid(row=0, column=1)
inputBox2.grid(row=1, column=1)
inputBox3.grid(row=2, column=1)
inputBox4.grid(row=3, column=1)
inputBox5.grid(row=4, column=1)

startButton.grid(row=5, column=0)


# Draws the boids, applies behavior and updates the boids.
# Restarts the simulation if the reset flag is on.
def App(canvas):
    canvas.delete("all")
    global flock
    global resetFlag
    global rng
    global numberofBoids
    for boid in flock:
        boid.show(canvas)
        boid.behavior(flock, cohesionStrength,
                      seperationStrength, alignmentStrength)
        boid.edges()
        boid.update(speedLimit)
    if resetFlag is not True:
        root.after(25, lambda: App(canvas))
    else:
        flock = [Boid(rng.random()*sizeX, rng.random()*sizeY, sizeX, sizeY)
                 for _ in range(numberOfBoids)]
        resetFlag = False
        root.after(1, lambda: App(canvas))


# Initializes the window
root.config(menu=menuBar)
root.mainloop()