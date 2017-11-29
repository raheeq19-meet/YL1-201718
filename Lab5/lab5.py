from turtle import *
#class square(Turtle):
    #def __init__(self,size):
   #     Turtle.__init__(self)
  #      self.shapesize(size)
 #       self.shape("square")
#square(5)

class hexagon (Turtle):
    def __init__(self,size,speed,color):
        self.speed=speed
        self.color=color
        Turtle.__init__(self)
        self.begin_poly()
        self.pendown()
        for i in range (6):
            self.forward(size)
            self.left(60)
        self.end_poly()
        hexaa=self.get_poly()
        register_shape("hexagon",hexaa)
        self.shape("hexagon")
hexaa=hexagon(100,50,"Red")
        
        
      



        
        
            
