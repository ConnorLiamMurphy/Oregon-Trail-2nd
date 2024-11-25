import PySimpleGUI as sg

from manage_supplies import manage_supplies
from store import buy_supplies  # Import the buy_supplies function
from encountering import encountering
from encounters import Encounter
from show_inventory import show_inventory
from parameters import select_travel_parameters
from actions import Actions
from inventoryAndStats import InventoryAndStats
from traveling import traveling
from view_status import view_status

def start_game():
    """open the window for the main game loop and menu for the player"""
    # initialize inventory class
    _inv = InventoryAndStats(0, 0, 0, 0, 0, 0, 0, 5, 10)

    buy_supplies(_inv)  # Enter the store to buy supplies(store.py)

    # Get travel parameters from the player
    _travel_speed, _rations, _date = select_travel_parameters()

    # initialize action class and set travel distance, speed, and rations
    _act = Actions(500, _inv, _travel_speed, _rations, _date)
    # This is what the game window will look like(Lots of work here still)
    _layout = [
        [sg.Text('Game Started!', font=('Helvetica', 20), key='-GAME-')],
        [sg.Text(f'Current Location: {_act.get_location()}', font=('Helvetica', 16), key='-LOCATION-')],
        [sg.Text(f'Morale: {_inv.get_morale()}', key='-MORALE-')],
        [sg.Text(f'Health: {_inv.get_health()}', key='-HEALTH-')],
        [sg.Text(f'Food: {_inv.get_food()}', key='-FOOD-')],
        [sg.Text(f'Distance Left: {_act.get_distance()}', key='-DISTANCE-')],
        [sg.Text(f'Date: {_act.get_date()}', key='-DATE-')],
        [sg.Button('Travel', size=(10, 2), font=('Helvetica', 16)),
         sg.Button('Check Inventory', size=(15, 2), font=('Helvetica', 16)),
         sg.Button('View Status', size=(15, 2), font=('Helvetica', 16)),
         sg.Button('Quit', size=(10, 2), font=('Helvetica', 16))],
        [sg.Button('Manage Supplies', size=(10, 2), font=('Helvetica', 16))]
    ]
    # This is what the game window will look like(Lots of work here still)
    _game_window = sg.Window('Game', _layout, size=(500, 400))

    # Event loop
    while True:
        _event, _values = _game_window.read()  # Reads in the event
        if _event == sg.WINDOW_CLOSED or _event == 'Quit':
            break  # Exit loop here
        elif _event == 'Travel':
            while True:
                _var_type = traveling(_act)
                if isinstance(_var_type, Encounter):
                    encountering(_var_type)
                elif not _var_type:
                    sg.popup('You have run out of food! Game Over!')
                    break
                else:
                    break
            if not _var_type:
                break
            _game_window['-LOCATION-'].update(f'Current Location: {_act.get_location()}')
            _game_window['-MORALE-'].update(f'Morale: {_inv.get_morale()}')
            _game_window['-HEALTH-'].update(f'Health: {_inv.get_health()}')
            _game_window['-FOOD-'].update(f'Food: {_inv.get_food()}')
            if _inv.get_food() <= 0:
                sg.popup('You have run out of food! Game Over!')
                break
            _game_window['-DISTANCE-'].update(f'Distance Left: {_act.get_distance()}')
            _game_window['-DATE-'].update(f'Date: {_act.get_date()}')
            _game_window['-GAME-'].update("")
        elif _event == 'Check Inventory':
            show_inventory(_inv)  # Open the inventory window
        elif _event == 'Manage Supplies':
            manage_supplies(_act, _inv)  # Open the manage_supplies window
        elif _event == 'View Status':
            # Call the view_status function when 'View Status' button is clicked
            view_status(_inv, _act)
    _game_window.close()
