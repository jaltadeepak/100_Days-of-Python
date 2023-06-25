from turtle import Turtle, Screen
import pandas

ALIGN = "Center"
FONT = ('Arial', 10, 'normal')

screen = Screen()
screen.title("U.S. States Game")
image = r"25_csvdata+pandaslib\us-states-game\blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

writer = Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv(r"25_csvdata+pandaslib\us-states-game\50_states.csv")
score = 0
guessed_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        game_is_on = False
        continue

    flag = 0
    for state in data.state:
        if state == answer_state:
            flag = 1
            break

    if flag == 1:
        guessed_states.append(answer_state)
        score += 1
        data_row = data[data.state == answer_state]
        state = data_row.state.values[0]
        print(state)
        writer.goto(int(data_row.x.item()), int(data_row.y.item()))
        writer.write(f"{state}", align = ALIGN, font = FONT)

    if score == 50:
        writer.clear()
        writer.goto(0, 0)
        writer.write("Game Won.", align=ALIGN, font=FONT)
        game_is_on = False

missed_state = []

#states_to_learn.csv
for state in data.state:
    flag = 0
    for guessed_state in guessed_states:
        if state == guessed_state:
            flag = 1
    if flag == 0:
        missed_state.append(state)

new_data = pandas.Series(missed_state)
new_data.to_csv(r"25_csvdata+pandaslib\us-states-game\states_to_learn.csv")
    