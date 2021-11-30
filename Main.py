from p5 import setup, draw, size, background, run
import numpy as np
from boid import Boid

width = 1000
height =1000

flock = [Boid(*np.random.rand(2)*1000, width, height) for _ in range(30)]


def setup():
    size(width,height)

def draw():
    background(0,0,0)

    for boid in flock:
        boid.show()
        boid.behavior(flock)
        boid.edges()
        boid.update()

run()
