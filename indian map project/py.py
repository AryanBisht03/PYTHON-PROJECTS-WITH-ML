import turtle

from PIL import Image
import pandas as pd
from turtle import Turtle,Screen

#changing the type of an image from jpeg to gif
jpg_image=Image.open("doodle-freehand-drawing-of-india-map-free-vector.jpg")
jpg_image.save("doodle-freehand-drawing-of-india-map-free-vector.gif")

#creating new size of an image
image=Image.open("doodle-freehand-drawing-of-india-map-free-vector.gif")
new_width=600
new_height=(new_width/image.width)*image.height
new_image=image.resize((new_width,int(new_height)))
new_image.save("New_resized_image.gif")

tim_the_turtle=Turtle()
screen=Screen()
image="New_resized_image.gif"
screen.title("Indian State Guesser")
screen.addshape(image)
tim_the_turtle.shape(image)
def turtlr_cooor(x,y):
    print(int(x), int(y))

state_cori_=[]
state_cori_.append(turtle.onscreenclick(turtlr_cooor))
print(state_cori_)
screen.mainloop()