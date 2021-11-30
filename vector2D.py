import math

class Vector2D():

    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord

    #Returns magnitude of the vector
    def mag(self):
        return math.sqrt(self.x**2+self.y**2)

    #Normalizes the vector
    def normalize(self):
        return self / self.mag()

    #Takes the dot product of two vectors
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    #Checks if two vectors are orthagonal
    def isOrthagonal(self, other):
        if self.dot(other) == 0:
            return True
        else:
            return False

    #Returns the squard magnitude
    def magSquared(self):
        return self.x**2 + self.y**2

    #Gives the component of the first vector along the second
    def component(self, other):
        return self.dot(other) / other.mag()

#Special functions

    def __add__(self, other):
        if type(other) is Vector2D:
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2D(x,y)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) is Vector2D:
            x = self.x - other.x
            y = self.y - other.y
        else:
            x = self.x - other
            y = self.y - other
        return Vector2D(x,y)

    def __rsub__(self, other):
        x = other - self.x
        y = other - self.y
        return Vector2D(x,y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector2D(x,y)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector2D(x,y)

    def __floordiv__(self, other):
        x = self.x // other
        y = self.y // other

    def __neg__(self):
        return Vector2D(-self.x,-self.y)

    def __abs__(self):
        return Vector2D(abs(self.x),abs(self.y))


    def __invert__(self):
        return Vector2D(self.y,self.x)

    def __repr__(self):
        return "(" + repr(self.x) + ", " + repr(self.y) + ")"

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        if type(other) is Vector2D:
            if (self.x == other.x && self.y == other.y):
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if type(other) is Vector2D:
            if (self.x == other.x && self.y == other.y):
                return False
            else:
                return True
        else:
            return True
