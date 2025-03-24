#Custom Cursor - Suhaani Singh
#This program draws a red and blue circle, one embedded into another, that follows the mouse cursor 
#and does not leave a trail of circles behind 


def setup():
    """this extends the canvas and makes the background colour black"""
    size(400,400)                                  #changes canvas size 
    background(0)                                  #changes background to black 
    
def embedded_circles():
    """this draws the two embedded circles that has the center of the current mouse coordinates"""
    fill(255,0,0)                                  #changes larger circle's colour to red 
    ellipse(mouseX, mouseY, 100,100)               #larger circle
    fill(0,0,255)                                  #changes smaller circle's colour to blue 
    ellipse(mouseX,mouseY,50,50)                   #smaller circle embedded inside the larger one 
    
def draw():
    """this function calls/draws the embedded circles"""
    background(0)                                  #makes sure no trail of circles is left behind
    embedded_circles()                             #calls the embedded circles function
