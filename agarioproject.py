from turtle import Turtle
class Circle(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.penup()
        self.dx=dx
        self.dy=dy
        self.r=r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
        
    def move(self,screen_width,screen_height):
        current_x=self.xcor()
        new_x=current_x+self.dx
        current_y=self.ycor()
        new_y=current_y+self.dy
        right_side_ball=new_x+self.r
        left_side_ball=new_x-self.r
        up_side_ball=new_y+self.r
        down_side_ball=new_y-self.r
        self.goto(new_x,new_y)
        if (new_x==-(screen_width*0.5)):
            self.dx=-self.dx
        if (new_x== screen_width*0.5):
            self.dx=-self.dx
        if (new_y==-(screen_height*0.5)):
            self.dy=-self.dy
        if (new_y== screen_height*0.5):
            self.dy=-self.dy



import turtle
import time
import random
import Circle from agarioproject.py
turtle.tracer(0,50)

        

        
    
    
