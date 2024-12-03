import random

import PySimpleGUI as sg

from parameters import Character


def is_peaceful(area):
    """Returns True if the area is peaceful,
    False otherwise. For now, it's random."""
    # Simulate the peace status of the area, 70% chance peaceful.
    return random.choice([True, False])  # 70% peaceful, 30% encounter


def take_rest(_act, _inv, _char: Character):
    """Allow the player to rest for a
    specified number of days in a peaceful area."""
    # Check if the area is peaceful
    if not is_peaceful(_act.get_location()):
        sg.popup("This area is not peaceful. You cannot rest here.")
        return None

    # Prompt player to rest for 1, 2, or 3 days
    layout = [
        [sg.Text("It is peaceful here. Would you like to rest?", font=('Helvetica', 16))],
        [sg.Button("Rest for 1 day", size=(12, 2), font=('Helvetica', 14)),
         sg.Button("Rest for 2 days", size=(12, 2), font=('Helvetica', 14)),
         sg.Button("Rest for 3 days", size=(12, 2), font=('Helvetica', 14)),
         sg.Button("Cancel", size=(12, 2), font=('Helvetica', 14))]
    ]

    rest_window = sg.Window("Take a Rest", layout, size=(700, 400))

    # Event loop
    while True:
        event, _ = rest_window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            rest_window.close()
            return None

        # If the player chose to rest
        elif event == "Rest for 1 day" or event == "Rest for 2 days" or event == "Rest for 3 days":
            days = int(event.split()[2])  # Get the number of days from the button text

            # Simulate the night sky display for a few seconds
            _ = sg.Image(data='night_sky_image_path.png')  # You can replace this with an actual image file
            layout_night = [
                [sg.Text("The stars are so... Resting...", font=('Helvetica', 20))],
                [sg.Image(filename=r'images/space.png')]
            ]
            night_window = sg.Window("Night Sky", layout_night,
                                     size=(500, 300), no_titlebar=True, grab_anywhere=True)
            night_window.read(timeout=3000)  # Show the night sky for 3 seconds
            night_window.close()

            # Apply the resting effect: increase health/morale
            if _inv.get_health() < _char.get_class_health():  # Cap the health at 10
                # Increase health by 10 per day
                _inv.set_health(min(_char.get_class_health(), _inv.get_health() + days * 3))
            if _inv.get_morale() < 100:  # Cap the morale at 100
                _inv.set_morale(min(100, _inv.get_morale() + days * 5))  # Increase morale by 5 per day

            # Increment the date based on the number of rest days
            for _ in range(days):
                _act.increment_date()  # Increment the date by one day for each day of rest

            # Update the game window with the new stats
            rest_window.close()
            return f"You rested for {days} days. Health and morale have been improved."
