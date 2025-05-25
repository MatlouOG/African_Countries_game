import turtle
import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("Guess African Countries Game")
image = "Africa1112.gif"
screen.addshape(image)
t.shape(image)

data = pd.read_csv("AfricanCountries.csv")
print(data)
countries = data.country.to_list()

print(countries)
guessed_country = []
while len(guessed_country) < 55:

    answer_country = screen.textinput(title=f"{len(guessed_country)}/55 Correct Countries",
                                      prompt="Which country's name can you guess?").title()
    if answer_country == "Exit":
        missing_country = []
        for country in countries:
            if country not in guessed_country:
                missing_country.append(country)
        new_data = pd.DataFrame(missing_country)
        new_data.to_csv("countries_missed.csv")

        break
    if answer_country in countries:
        guessed_country.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data =data[data.country == answer_country]
        t.goto(country_data.x.item(), country_data.y.item())
        t.write(answer_country)

#used to get coordinates on turtle image
'''
def get_mouse_click_coor(x, y):
    print(x,y)

t.onscreenclick(get_mouse_click_coor)
'''

#t.mainloop()
screen.exitonclick()
