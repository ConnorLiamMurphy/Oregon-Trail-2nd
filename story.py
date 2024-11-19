import PySimpleGUI as sg


# Story at the beginning of the game(This can be changed,
# we can add multiple story lines, choices. etc.)
def show_story():
    """open a window that displays the story text until closed"""
    _story_text = (
        "Welcome to the Oregon Trail!\n\n"
        "In 1843, a group of pioneers set out from "
        "Missouri to settle in Oregon. "
        "They faced numerous challenges along the way, "
        "including harsh weather, "
        "limited supplies, "
        "and unpredictable dangers. "
        "As a traveler, "
        "you'll need to make wise choices to survive the journey. "
        "Prepare your oxen team, gather food, "
        "ammunition, and supplies, "
        "and embark on an adventure across the "
        "rugged landscape of the Oregon Trail.\n\n"
        "Good luck, traveler!"
    )
    # This is what the story will look like
    # (This can be changed -> maybe make it moving?)
    sg.popup(_story_text, title="The Oregon Trail Story", font=('Helvetica', 14))
