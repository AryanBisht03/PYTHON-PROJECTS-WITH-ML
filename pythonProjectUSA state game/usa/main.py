import turtle

import pandas as pd
from turtle import Turtle,Screen

screen=Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinates(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)

#this is same as exitonclick() but it will not exit even if we click.
# turtle.mainloop()
# screen.exitonclick()
df=pd.read_csv("50_states.csv")
all_state=df["state"].to_list()
guessed_state=[]


while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's another state name?").title()
    if answer_state=="Exit":
        missing_state=[]
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv("Missed by you")
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=df[df.state==answer_state]
        turtle.goto(state_data.x.item(),state_data.y.item())
        turtle.write(state_data.state.item())


#create a CSV file of the names that are not been guessed by the user


screen.exitonclick()