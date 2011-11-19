##  Stephen Hoerner
##  CSCD 110
##  Assignment 1

# load math module
import math

# FUNCTIONS
def circleCircumference(p_radius):
    return math.pi * 2 * p_radius

def circleArea(p_radius):
    return math.pi * p_radius**2

def sphereSurfaceArea(p_radius):
    return 4 * math.pi * p_radius**2

def sphereVolume(p_radius):
    return (4/3) * math.pi * p_radius**3

def numInput(prompt): # user input
    return eval(input(prompt))


# MAIN
try:
    radius = numInput('Enter radius: ')
    if (abs(radius) != radius):
        raise ValueError; # throw neg-value exception
    
except ValueError: # cannot be negative
    print('Invalid number; negative values not permitted.')
    
except: # probably an eval() error
    print('Invalid value.')

else: # ideal execution, no errors
    print() # newline

    print('Circumference of circle: ' + str(circleCircumference(radius)))
    print('Area of circle:          ' + str(circleArea(radius)))
    print('Surface area of sphere:  ' + str(sphereSurfaceArea(radius)))
    print('Volume of sphere:        ' + str(sphereVolume(radius)))

    # Voila.
