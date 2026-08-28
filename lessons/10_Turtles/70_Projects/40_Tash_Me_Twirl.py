"""
# 40_Tash_Me_Twirl.py
 
Copy your old 30_Tash_Me_Click.py code here and update the program so that the moustache will twirl when you click on it.

Hint: See 10_More_Turtle_Programs, section 'Clicking The Turtle Directly'
"""

import turtle
turtle.setup(width=600, height=600)         # Set the size of the window

tina = turtle.Turtle()     
tina.penup()                               # Prevent drawing when moving
tina.shape("turtle")                       # Set the shape of the turtle

screen = turtle.Screen()                # Set up the screen
screen.setup(width=600, height=600)     # Set the size of the window
screen.bgcolor('white')                 # Set the background color



def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""
    from pathlib import Path                                        # Import Path from pathlib module
    from PIL import Image                                           # Import Image from PIL (Pillow) library

    image_dir = Path(__file__).parent.parent / "images"                    # Define the directory containing images
    image_path = str(image_dir / image_name)                        # Create the full path to the image file

    image = Image.open(image_path)                                  # Open the image to get its dimensions
    
    window.setup(image.width, image.height, startx=0, starty=0)     # Set window size to image size
    window.bgpic(image_path)                                        # Set the background picture of the window

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path                        # Import Path from pathlib module
    image_dir = Path(__file__).parent.parent / "images"    # Define the directory containing images
    image_path = str(image_dir / image_name)        # Create the full path to the image file

    screen = turtle.getscreen()                     # Get the turtle's screen
    screen.addshape(image_path)                     # Register the image as a shape
    turtle.shape(image_path)                        # Set the turtle's shape to the image

# This is the function that gets called when you click on the screen
def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    tina.goto(x, y) # Move the turtle to the clicked location


set_background_image(screen, "emoji.png")   # Set the background image of the screen
set_turtle_image(tina, "moustache1.gif")                  
for i in range(0,360, 20):  # Full circle, 20 degrees at a time
        turtle.tilt(20)              # Tilt the turtle 20 degrees
 # Important! Tell Python which function to use when the screen is clicked

turtle.done() 