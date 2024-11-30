import PySimpleGUI as sg


# Story at the beginning of the game(This can be changed,
# we can add multiple story lines, choices. etc.)

def show_story():
    """Open a window that displays the story text until closed"""
    _story_text = (
        "Welcome to The Stellar Trail!\n\n"
        "It is the year 2355, humanity has spread across the stars.\n"
        "Your colony ship, the Explorer, lost contact with Earth during its journey.\n"
        "It became stranded in an uncharted part of the galaxy.\n"
        "You are one of the last survivors aboard, and your mission is clear \n\n"
        "Find a way to return to Earth...\n\n"
        "You must repair your ship, gather supplies, and navigate through space.\n"
        "Prepare to gather food, fuel, and ship parts, and set course for Earth.\n"
        "Will you make it home, or will the vastness of space claim you as its own?\n\n\n\n"
        "Good luck, traveler...."
    )
    sg.popup(_story_text, title="The Oregon Trail Story", font=('Arial', 14))