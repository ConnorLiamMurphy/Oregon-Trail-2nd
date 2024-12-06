import PySimpleGUI as sg

from initiate_trade import initiate_trade
from manage_supplies import manage_supplies
from perform_hunt import perform_hunt
from store import buy_supplies  # Import the buy_supplies function
from encountering import encountering
from encounters import Encounter
from show_inventory import show_inventory
from parameters import select_travel_parameters, select_class_parameters, Character
from actions import Actions
from inventoryAndStats import InventoryAndStats
from story import show_story
from test_makeDecision import take_rest
from traveling import traveling
from view_status import view_status


# Use Pygbag to make a web browser game

def start_game():
    button_image = r'images/new_button.png'
    sg.theme("Dark Blue 2")
    """open the window for the main game loop and menu for the player"""
    # initialize inventory class
    # Prints the beginning story(This can be changed in story.py)
    show_story()
    _class, _weapon = select_class_parameters()
    _char_class = Character(_class, _weapon)
    _inv = InventoryAndStats(_char_class.get_class_food(), 0, 0, 0, 0,
                             0, _char_class.get_class_money(), _char_class.get_class_morale(),
                             _char_class.get_class_health(), _char_class)
    buy_supplies(_inv)  # Enter the store to buy supplies(store.py)

    # Get travel parameters from the player
    _travel_speed, _rations, _date = select_travel_parameters()

    # initialize action class and set travel distance, speed, and rations
    _act = Actions(500, _inv, _travel_speed, _rations, _date, _char_class)
    # This is what the game window will look like(Lots of work here still)

    _layout = [
        # Single row containing two columns: left-aligned text and right-aligned buttons
        [
            # Left-aligned text column
            sg.Column([
                [sg.Text('Game Started!', font=('Helvetica', 20, "bold"),
                         key='-GAME-', justification='left')],
                [sg.Text(f'Current Location: {_act.get_location()}',
                         font=('Helvetica', 16, "bold"), key='-LOCATION-',
                         justification='left')],
                [sg.Text(f'Food: {_inv.get_food()}', key='-FOOD-', justification='left')],
                [sg.Text(f'Distance Left: {_act.get_distance()} light years',
                         key='-DISTANCE-', justification='left')],
                [sg.Text(f'Date: {_act.get_date()}', key='-DATE-', justification='left')],
                [sg.Image(r'images/Spaceship.png', size=(500, 479))]  # Image placed below the text
            ], element_justification='left'),

            # Right-aligned buttons column
            sg.Column([
                [sg.Button('Travel', size=(10, 2), image_filename=button_image,
                           font=('Orbitron', 16))],
                [sg.Button('Check Inventory', image_filename=button_image, size=(10, 3),
                           font=('Helvetica', 16))],
                [sg.Button('View Status', image_filename=button_image, size=(10, 3),
                           font=('Helvetica', 16))],
                [sg.Button('Manage Supplies', image_filename=button_image, size=(10, 3),
                           font=('Helvetica', 16))],
                [sg.Button('Initiate Trade', image_filename=button_image, size=(10, 3),
                           font=('Helvetica', 16))],
                [sg.Button('Take Rest', image_filename=button_image, size=(10, 3),
                           font=('Helvetica', 16))],
                [sg.Button('Go Scavenging', image_filename=button_image, size=(10, 3),
                           font=('Helvetica', 16))],
                [sg.Button('Quit', image_filename=button_image, size=(10, 3),
                           font=('Helvetica', 16))]
            ], justification='right', vertical_alignment='top')
            # Ensure buttons align vertically on the right side
        ]
    ]

    # This is what the game window will look like(Lots of work here still)
    _game_window = sg.Window('Game', _layout, size=(800, 700))

    # Event loop
    while True:
        _event, _values = _game_window.read()  # Reads in the event
        if _event == sg.WINDOW_CLOSED or _event == 'Quit':
            break  # Exit loop here
        elif _event == 'Travel':
            _game_window.hide()
            while True:
                _var_type = traveling(_act)
                if isinstance(_var_type, Encounter):
                    encountering(_var_type)
                elif not _var_type:
                    if _inv.get_food() <= 0:
                        sg.popup('You have run out of food! Game Over!')
                    elif _inv.get_health() <= 0:
                        sg.popup('You have died on your journey! Game Over!')
                    elif _inv.get_morale() <= 0:
                        sg.popup('You are hopeless and can\'t keep going! Game Over!')
                    elif _inv.get_oxen() <= 0 and _act.get_travel_speed() == 'Broken':
                        sg.popup('You\'re ship is completely inoperable! Game Over!')
                    elif _inv.get_clothes() <= 0 and _act.get_weather() == 'No Oxygen':
                        sg.popup('You have died from lack of air! Game Over!')
                    elif _inv.get_clothes() <= 0 and _act.get_weather() == 'Dangerously High Oxygen Levels ':
                        sg.popup('You have died of oxygen poisoning! Game Over!')
                    break
                else:
                    break
            _game_window.un_hide()
            if not _var_type:
                break
            _game_window['-LOCATION-'].update(f'Current Location: {_act.get_location()}')
            _game_window['-FOOD-'].update(f'Food: {_inv.get_food()}')
            _game_window['-DISTANCE-'].update(f'Distance Left: {_act.get_distance()} light years')
            _game_window['-DATE-'].update(f'Date: {_act.get_date()}')
            _game_window['-GAME-'].update("")
        elif _event == 'Check Inventory':
            show_inventory(_inv)  # Open the inventory window
        elif _event == 'Manage Supplies':
            manage_supplies(_act, _inv, _char_class)  # Open the manage_supplies window
        elif _event == 'View Status':
            # Call the view_status function when 'View Status' button is clicked
            view_status(_inv, _act, _char_class)
        elif _event == 'Initiate Trade':
            # Call the initiate trade function when 'Initiate Trade' button is clicked
            initiate_trade(_inv)
        elif _event == 'Take Rest':
            # Call the take rest function when 'Take Rest' button is clicked
            take_rest(_act, _inv, _char_class)
            _game_window['-DATE-'].update(f'Date: {_act.get_date()}')
        elif _event == 'Go Scavenging':
            if _act.get_hunted():
                sg.popup("you cannot scavenge more than once per day")
            elif _inv.get_ammo() <= 0:
                sg.popup("You have no weapon energy")
            else:
                perform_hunt(_act, _inv, _char_class)  # Open the perform_hunt window
                _game_window['-FOOD-'].update(f'Food: {_inv.get_food()}')
                if _inv.get_health() <= 0:
                    sg.popup('You have died on your journey! Game Over!')
                    break
        if _act.get_distance() == 0:
            _game_window.hide()
            sg.popup("Game Over", "You have reached the end of your journey!", font=('Helvetica', 16))
            end_game_results(_inv, _act)
            break
    _game_window.close()


def end_game_results(inventory, actions):
    """end the game once the player reaches the final destination"""
    food_remaining = inventory.get_food()
    health_remaining = inventory.get_health()
    morale_remaining = inventory.get_morale()
    distance_traveled = 500

    final_location = actions.get_location()
    date = actions.get_date()

    # Generate the end-game summary
    results = [
        "Your journey on the Stellar Trail has ended!",
        f"Final Location: {final_location}",
        f"Date of Arrival: {date}",
        f"Distance Traveled: {distance_traveled} light years",
        "",
        "Final Stats:",
        f"  Food Remaining: {food_remaining}",
        f"  Health Remaining: {health_remaining}",
        f"  Morale Remaining: {morale_remaining}",
    ]

    # Display the results in a GUI window
    layout = [
                 [sg.Text(line, font=('Helvetica', 14))] for line in results
             ] + [[sg.Button('Close', size=(10, 2), font=('Helvetica', 16))]]

    window = sg.Window('End Game Results', layout, size=(400, 400))

    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break

    window.close()
