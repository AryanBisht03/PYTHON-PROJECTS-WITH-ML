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


#importing the CSV and converting the state columns content into a seperate list
df=pd.read_csv("list of states wit lat and long.csv")
print(df.head())

#creating a list
print(df.state)
list_of_states=df["state"].to_list()
print(list_of_states)

guessed_state=[]

while len(guessed_state)<29:
    answer=screen.textinput(title=f"The Guesser,{(len(guessed_state)+1)}/29",prompt="Guess the next state").title()
    if answer=="Exit":
        missing_states=[]
        for states in list_of_states:
            if states not in guessed_state:
                missing_states.append(states)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("States missed by you")


        break
    if answer in list_of_states:
        guessed_state.append(answer)
        turtle_u=Turtle()
        turtle_u.hideturtle()
        turtle_u.penup()
        state_data=df[df.state==answer]
        turtle_u.goto(state_data.x.item(),state_data.y.item())
        turtle_u.pensize(50)
        turtle_u.pencolor("blue")
        turtle_u.write(state_data.state.item(),align="center",font=("arial",8,"bold"))


