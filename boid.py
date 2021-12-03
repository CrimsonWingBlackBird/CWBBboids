from tkinter import *
import math
import numpy as np
from vector2D import Vector2D


class Boid():

    # Initializes the boid
    def __init__(self, x, y, width, height):
        self.position = Vector2D(x, y)
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = Vector2D(*vec)
        vec = (np.random.rand(2) - 0.5)/2
        self.acceleration = Vector2D(*vec)

    # Draws the boid on the canvas
    def show(self, canvas):
        radius = 3
        coord = (self.position.x - radius, self.position.y - radius,
                 self.position.x + radius, self.position.y + radius)
        canvas.create_oval(coord, fill="red")

    # Calls the behavior functions
    def behavior(self, boids, cohesionStrength, seperationStrength,
                 alignmentStrength):
        self.cohesion(boids, cohesionStrength)
        self.seperation(boids, seperationStrength)
        self.alignment(boids, alignmentStrength)

    # Makes the boids stick together.
    def cohesion(self, boids, cohesionStrength):
        neighborList = self.neighborBoids(boids, 50)
        averageNeighborList = Vector2D(0, 0)
        for boid in neighborList:
            averageNeighborList += boid.position
        averageNeighborList = averageNeighborList/len(neighborList)
        self.velocity += cohesionStrength*(averageNeighborList-self.position)

    # Makes the boids not get too close
    def seperation(self, boids, seperationStrength):
        neighborList = self.neighborBoids(boids, 20)
        averageNeighborList = Vector2D(0, 0)
        for boid in neighborList:
            averageNeighborList += boid.position
        averageNeighborList = averageNeighborList/len(neighborList)
        self.velocity += seperationStrength * \
            (self.position - averageNeighborList)

    # Makes the boids go in the same direction as their neighbors
    def alignment(self, boids, alignmentStrength):
        neighborList = self.neighborBoids(boids, 50)
        averageNeighborList = Vector2D(0, 0)
        for boid in neighborList:
            averageNeighborList += boid.velocity
        averageNeighborList = averageNeighborList/len(neighborList)
        self.acceleration += alignmentStrength * \
            (averageNeighborList-self.velocity)

    # Steers the boids away from the edges
    # NEED TO UPDATE USING sizeX AND sizeY
    def edges(self, width, height):
        if (self.position.x >= width-100):
            self.acceleration.x -= 1
        if (self.position.x <= 100):
            self.acceleration.x += 1
        if (self.position.y >= height-100):
            self.acceleration.y -= 1
        if (self.position.y <= 100):
            self.acceleration.y += 1

    # Pushes velocity and position changes to boids
    def update(self, speedLimit):
        self.applySpeedLimit(speedLimit)
        self.position += self.velocity
        self.velocity += self.acceleration
        self.acceleration = Vector2D(0, 0)

    # Stops the boids from going too fast
    def applySpeedLimit(self, speedLimit):
        if (self.velocity.mag() > speedLimit):
            self.velocity = self.velocity.normalize()
            self.velocity = self.velocity*speedLimit
        pass

    # Finds the distance between two vectors
    def distance(self, vector1, vector2):
        differenceVector = vector1 - vector2
        return differenceVector.mag()

    # Finds boids nearby, in a certain radius
    def neighborBoids(self, boids, radius):
        neighborList = []
        for boid in boids:
            distance = self.distance(self.position, boid.position)
            if (distance <= radius):
                neighborList.append(boid)
        return neighborList
