from time import strftime as t
from time import sleep as s
from os import name, system


def update():  # Updates strings to current time
    global month, day, hour, minutes, seconds, amorpm, offset, abreviation,year,dayoftheweek
    # Time Strings
    year = t('%Y')
    month = t('%B')
    dayoftheweek = t('%A')
    day = t('%d')
    hour = t('%l')
    minutes = t('%M')
    seconds = t('%S')
    amorpm = t("%p")
    offset = t('%z')

    # Abreviation decider
    if (day == 1) or (day == 21) or (day == 31):  #st
        abreviation = "st"
    elif (day == 2) or (day == 22):  #nd
        abreviation = "nd"
    elif (day == 3) or (day == 23):  #rd
        abreviation = "rd"
    else:
        abreviation = "th"


def clearscreen():  # Clears the screen
    if name == 'nt':  # If it's windows
        _ = system("cls")
    else:             # If it's other than windows
        _ = system("clear")

while True:
    update()        # Update the strings
    clearscreen()   # Clear the screen
    print(
        f"It's {dayoftheweek}, {month} {day}{abreviation} {year}.\nThe current time is{hour}:{minutes}:{seconds} {amorpm} \n\nOffset: {offset}"
    )
    s(1)
