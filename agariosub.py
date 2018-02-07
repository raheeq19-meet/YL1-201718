import turtle
import time
import random
import math
from ball import Ball
turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.05
SCREEN_WIDTH=round(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=round(turtle.getcanvas().winfo_height()/2)
#PART 0:
MY_BALL=Ball(0,0,0,0,20,"red")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=60
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]
for i in range (NUMBER_OF_BALLS):
    x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
    y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(),random.random(),random.random())
    BBB=Ball(x,y,dx,dy,r,color)
    BALLS.append(BBB)
#PART 1:
def move_all_balls():
    for value in BALLS:
        value.move(SCREEN_WIDTH,SCREEN_HEIGHT)

#PART 2:
def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    
    d=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d+10<=ball_a.r+ball_b.r:
        return True
    else:
        return False
#PART 3:
def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a,ball_b):
        
                x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
                y=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color=(random.random(),random.random(),random.random())
                while dx==0:
                    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                while dy==0:
                    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                if ball_a.r>ball_b.r:
                    ball_a.r+=1
                    ball_a.shapesize(ball_a.r/10)
                    ball_b.goto(x, y)
                    ball_b.dx=dx
                    ball_b.dy=dy
                    ball_b.r=r
                    ball_b.color(color)
                    ball_b.shapesize(r/10)
                elif ball_b.r>ball_a.r:
                    ball_b.r+=1
                    ball_b.shapesize(ball_b.r/10)
                    ball_a.dx=dx
                    ball_a.dy=dy
                    ball_a.r=r
                    ball_a.color(color)
                    ball_a.shapesize(r/10)

#PART 4:
#need to check!!!!!!!!
def check_myball_collision():
    for ball_x in BALLS:
        if collide(MY_BALL,ball_x):
            
            if ball_x.r>MY_BALL.r:
                return False
            else:
                MY_BALL.r+=1
                MY_BALL.shapesize(MY_BALL.r/10)
            
                x_coordinate=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
                y_coordinate=random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                ball_x.goto(x_coordinate,y_coordinate)
                ball_x.dx=dx
                ball_x.dy=dy
                ball_x.r=radius
                r=random.random()
                b=random.random()
                g=random.random()
                color=(r,b,g)
                ball_x.color(color)
                ball_x.shapesize(ball_x.r/10)
                MY_BALL.r=MY_BALL.r+1
                MY_BALL.shapesize(MY_BALL.r/10)
    return True

#PART 5:
def movearound(event):
    MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()
            


#PART 6:
while RUNNING==True:
            if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2:
                SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
            if SCREEN_HEIGHT!= turtle.getcanvas().winfo_height()/2:
                SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
            move_all_balls()
            check_all_balls_collision()
            if check_myball_collision()== False:
                turtle.bgcolor("blue")
                turtle.write("game over :(",move=False,align="left",font=('Arial',30, "normal"))
                RUNNING=False
            time.sleep(SLEEP)
            turtle.getscreen().update()
turtle.mainloop()
            
                                 
            
            
            
            
            
        
            
            
                

        
                
                
                
            
            
    
    
    

    
    
    
    
