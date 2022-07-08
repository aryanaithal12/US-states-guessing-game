import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.color("black")
data = pd.read_csv('50_states.csv')
list_of_states = data.state.to_list()
list_of_states_guessed = []
Game_is_running = True
while Game_is_running:
    player_answer = screen.textinput(title=f"{len(list_of_states_guessed)}/50 states correct",
                                     prompt="Whats another state name you know").strip().title()
    if (player_answer == "Exit") or (len(list_of_states_guessed) == 50):
        Game_is_running = False
    elif (player_answer in list_of_states) and (player_answer in list_of_states_guessed):
        pass
    elif player_answer in list_of_states:
        list_of_states_guessed.append(player_answer)
        x = int(data[data.state == player_answer].x)
        y = int(data[data.state == player_answer].y)
        tim.goto(x, y)
        tim.write(arg=f"{player_answer.title()}")
list_of_states = [states for states in list_of_states if not (states in list_of_states_guessed)]
remaining_states = {"states": list_of_states}
dt = pd.DataFrame(remaining_states)
dt.to_csv("remaining_states.csv", index=False)
