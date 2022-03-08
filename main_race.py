from turtle import Turtle, Screen
import random

KOLORY = ['red', 'black', 'green', 'purple', 'yellow', 'blue']
LISTA_IMION_GRACZY = ['Tom', 'Ela', 'Aniela', 'Kinga', 'Mariusz', 'Adam']
SLOWNIK_OBIETKOW = {imie: Turtle() for imie in LISTA_IMION_GRACZY}
KRZTAŁT = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
    
screen = Screen()
user_input = screen.textinput(title="Twój Traf", prompt="Podaj kolor który wygra: 'red', 'black', 'green', 'purple', 'yellow', 'blue'")
screen.setup(width=500, height=500)



for enum, obiekt in enumerate(SLOWNIK_OBIETKOW):
    SLOWNIK_OBIETKOW[obiekt].pu()
    SLOWNIK_OBIETKOW[obiekt].color(KOLORY[enum])
    SLOWNIK_OBIETKOW[obiekt].goto(x=-230, y=enum*50 + -100)
    SLOWNIK_OBIETKOW[obiekt].shape(KRZTAŁT[enum])


warunek_petli_while = True

while warunek_petli_while:
    for obiekt in SLOWNIK_OBIETKOW:
        liczba = random.randint(0, 10)
        SLOWNIK_OBIETKOW[obiekt].forward(liczba)
        if int(SLOWNIK_OBIETKOW[obiekt].xcor()) >= 240:
            warunek_petli_while = False 
            if SLOWNIK_OBIETKOW[obiekt].color()[0] == user_input:
                print('You win')
                break
            else:
                print(f"you lose Wine is {obiekt}: {SLOWNIK_OBIETKOW[obiekt].color()[0].title()}")
                break

screen.exitonclick()