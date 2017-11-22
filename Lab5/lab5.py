from turtle import Turtle
class square(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
