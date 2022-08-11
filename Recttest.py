import numpy
import random
import matplotlib.pyplot as plt

#x = height y = width, i = x = u j = y = v
class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_h(self):
        return self.h
    def get_w(self):
        return self.w


def bounds(i,j):

    u = random.randrange(0,107,1)
    v = random.randrange(0,191,1)

    x = random.randrange(0, 107-u, 1)
    y = random.randrange(0, 191-v, 1)
    r = Rectangle(x,y,u,v)
    return r



i = 108
j = 192

m = numpy.zeros(shape=(i,j))

rect_array = []
for i in range(3):
    rect_array.append(bounds(i,j))

#If the rectangles have any overlap in the grid in the i direction then the two rectangles need to be merged#





numpy.savetxt("output.csv", m, delimiter=",")