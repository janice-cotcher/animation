# simple animation of a blue ball moving
# from left to right
# adapted from https://pages.uoregon.edu/park/Processing/process3.html

def setup():
    size(450, 350)
    # xPosition is the changing x-coordinate of the ball
    # yPosition is y-coordinate of the ball
    # set xPosition and yPosition to global variables
    # so they can be changed anywhere
    global xPosition
    global yPosition
    yPosition = float(height/2)
    xPosition = float(0)
    # xSpeed is the speed in the x-direction
    # ySpeed is the speed in the y-direction
    # set xSpeed and ySpeed to global variables so they can
    # be changed anywhere
    global xSpeed
    global ySpeed
    xSpeed = 3
    ySpeed = 3
    smooth()
    noStroke()
    frameRate(24)


def draw():
    global xPosition
    global yPosition
    global xSpeed
    global ySpeed
    # black background
    background(0)
    # if the ball position is larger than the
    # width of the sketch then it goes the opposite direction
    # in other words, when it hits the right wall
    if xPosition > width:
        xSpeed = -3
    # when ball hits the left wall, the ball goes towards the irght
    elif xPosition < 0:
        xSpeed = 3
    # blue circle that moves as xPosition increases
    fill(0, 20, 220)
    ellipse(xPosition, yPosition, 50, 50)
    # the value of xPosition will grow or shrink by 3 very frame
    xPosition += xSpeed
