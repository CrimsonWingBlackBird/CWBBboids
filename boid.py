import p5
import math
import numpy as np

class Boid():

    def __init__(self, x, y, width, height):
        self.position = p5.Vector(x,y)

        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = p5.Vector(*vec)

        vec = (np.random.rand(2) - 0.5)/2
        self.acceleration = p5.Vector(*vec)

    def show(self):
        p5.stroke(255)
        p5.circle((self.position.x, self.position.y), 3)

    def behavior(self, boids):
        self.cohesion(boids)
        self.seperation(boids)

    def cohesion(self, boids):
        neighborList = self.neighborBoids(boids, 50)
        averageNeighborList = p5.Vector(0,0)
        for boid in neighborList:
            averageNeighborList += boid.position
        averageNeighborList  = averageNeighborList/len(neighborList)
        self.velocity += averageNeighborList-self.position

    def seperation(self, boids):
        neighborList = self.neighborBoids(boids, 20)
        averageNeighborList = p5.Vector(0,0)
        for boid in neighborList:
            averageNeighborList += boid.position
        averageNeighborList  = averageNeighborList/len(neighborList)
        self.velocity += self.position - averageNeighborList

    def alignment(self, boids):
        neighborList = self.neighborBoids(boids, 50)
        averageNeighborList = p5.Vector(0,0)
        for boid in neighborList:
            averageNeighborList += boid.velocity
        averageNeighborList  = averageNeighborList/len(neighborList)
        self.acceleration += averageNeighborList-self.velocity


    def edges(self):
        if (self.position.x>=950):
            self.acceleration.x -= 1
        if (self.position.x<=50):
            self.acceleration.x += 1
        if (self.position.y>=950):
            self.acceleration.y -= 1
        if (self.position.y<=50):
            self.acceleration.y += 1

    def update(self):
        self.applySpeedLimit()
        self.position += self.velocity
        self.velocity += self.acceleration
        self.acceleration = p5.Vector(0,0)

    def applySpeedLimit(self):
        if (self.mag(self.velocity) > 10):
            self.velocity.normalize()
            self.velocity = self.velocity*10

    def mag(self, vector):
        return math.sqrt(vector.x**2+vector.y**2)

    def distance(self, vector1, vector2):
        differenceVector = p5.Vector(vector1.x-vector2.x, vector1.y-vector2.y)
        return self.mag(differenceVector)

    def neighborBoids(self, boids, radius):
        neighborList = []
        for boid in boids:
            distance = self.distance(self.position, boid.position)
            if (distance <= radius):
                neighborList.append(boid)
        return neighborList
