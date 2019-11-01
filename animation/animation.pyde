# simple animation of a blue ball moving
# from left to right
# adapted from https://pages.uoregon.edu/park/Processing/process3.html

def setup():
    size(450, 350)
    # set xPosition and yPosition to global varaibles
    # so they can be changed anywhere
    global xPosition
    global yPosition
    yPosition = float(height/2)
    xPosition = float(0)
    smooth()
    noStroke()
    frameRate(24)


def draw():
    # set xPosition and yPosition to global varaibles
    # so they can be changed anywhere
    global xPosition
    global yPosition
    # black background
    background(0)
    # blue circle that moves as xPosition increases
    fill(0, 20, 220)
    ellipse(xPosition, yPosition, 50, 50)
    # after drawing the circle, increase xposition by 2
    xPosition += 2
