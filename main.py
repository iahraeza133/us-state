import turtle

import pandas
# Create the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("US Game")

# Load the image as a custom shape
image = 'blank_states_img.gif'  # Ensure this image is in the same directory as your script
screen.addshape(image)

# Create a turtle object and set the shape to the image
t = turtle.Turtle()
t.shape(image)

data=pandas.read_csv('50_states.csv')
all_states=data['state'].to_list()
# Ask the user to guess the state
guessed_list=[]
while len(guessed_list)<5:
    answer_state = screen.textinput(title='Guess the state?', prompt='What\'s the state name?').title()

    print("answer_state: ", answer_state)
    # Define the function to handle mouse click events
    if answer_state in all_states:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data['state']==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state)
    def get_click_coordinates(x, y):
        print(f"Click coordinates: ({x}, {y})")
        # You can later compare the (x, y) with state coordinates to check if it's correct

    # Bind the click event to the get_click_coordinates function
    screen.onscreenclick(get_click_coordinates)

# Keep the window open
turtle.mainloop()  # Keeps the window open and listening for user interaction
