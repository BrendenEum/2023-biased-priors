# custome overlaps def is checking if two circels are overlaps
# this def will run thruout the full experiment
def customOverlaps(a, b):
    ''' a custom function to detect overlap between circular objects
    Locally we can use psychopys inbuild overlaps method, this does not
    yet exist in psychoJS so we need a custom function for online use.
    
    input:
        a: a circular object with attributed pos and size
        b: a circular object with attributes pos and size'''
    pt1 = a.pos
    pt2 = b.pos
    
    sep = ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**0.5
    
    # if the seperation is less than the sum of the radi
    if sep < a.size[0]/2 + b.size[0]/2:
        return True
    else:
        return False

# insideCircles def is checking if  circle is inside a bigger backgound circle

def insideCircle(circle1, circle2):
    '''
    circle1: larger circle
    circle2: smaller circle
    
    return: boolean true or false if smaller circle inside larger
    '''
    x1 = circle1.pos[0]
    y1 = circle1.pos[1]
    r1 = circle1.size[0]/2
    x2 = circle2.pos[0]
    y2 = circle2.pos[1]
    r2 = circle2.size[0]/2
    
    distSq = (((x1 - x2)* (x1 - x2))+ ((y1 - y2)* (y1 - y2)))**(.5)
    isInside = False
    if (distSq + r2 == r1):
        x = 1
    elif (distSq + r2 < r1):
        x = 2
        isInside = True
    else:
        x = 3
    return isInside