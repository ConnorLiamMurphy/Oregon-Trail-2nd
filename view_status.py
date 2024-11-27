import PySimpleGUI as sg

from inventoryAndStats import InventoryAndStats
from actions import Actions


def view_status(inv: InventoryAndStats, act: Actions):
    """Display player's stats and the distance from Oregon in a window"""
    # Get the current distance from Oregon (using act.get_distance())
    _distance = act.get_distance()

    # Layout for the status window
    _layout = [
        [sg.Text('Player Stats', font=('Helvetica', 20))],
        [sg.Text(f'Morale: {inv.get_morale()}', font=('Helvetica', 14))],
        [sg.Text(f'Health: {inv.get_health()}/10', font=('Helvetica', 14))],
        [sg.Text(f'Weather: {act.get_weather()}', font=('Helvetica', 14))],
        [sg.Text(f'Status: {inv.get_status()}', font=('Helvetica', 14))],
        [sg.Text(f'Distance from Oregon: {_distance}', font=('Helvetica', 14))],  # Show distance here
        [sg.Button('Close', size=(10, 2), font=('Helvetica', 16))]
    ]

    # Create the window
    status_window = sg.Window('Player Status', _layout, size=(400, 500), finalize=True)

    # Event loop
    while True:
        event, values = status_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break  # Exit the window

    status_window.close()
