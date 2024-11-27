from actions import Actions
import PySimpleGUI as sg

from inventoryAndStats import InventoryAndStats


def perform_hunt(act: Actions, inv: InventoryAndStats):
    """set the values tou use for the hunt from the GUI and then hunt"""
    ammo = []
    if inv.get_ammo() <= 6:
        for i in range(1, inv.get_ammo() + 1):
            ammo.append(f'{i}')
    else:
        ammo = ['1', '2', '3', '4', '5', '6']
    _layout = [
        [sg.Text(f'Current Weather: {act.get_weather()}', font=('Helvetica', 16), key='-LOCATION-')],
        [sg.Text('How much ammunition will you use:')],
        [sg.Combo(ammo, default_value=f'{ammo[len(ammo) - 1]}', key='-AMMO-')],
        [sg.Text('How long will you hunt for(hrs):')],
        [sg.Combo(['1', '2', '3'], default_value='3', key='-TIME-')],
        [sg.Button('Confirm', size=(10, 2), font=('Helvetica', 16)),
         sg.Button('Quit', size=(10, 2), font=('Helvetica', 16))]
    ]

    _hunt_window = sg.Window('Hunting', _layout, size=(500, 400), finalize=True)

    # Event loop
    while True:
        _event, _values = _hunt_window.read()
        if _event == sg.WINDOW_CLOSED or _event == 'Quit':
            break  # Exit loop here
        elif _event == 'Confirm':
            _food, _health = act.hunt(int(_values['-AMMO-']), int(_values['-TIME-']))
            sg.popup(f'injuries: -{_health}, food gained: {_food}')
            break
        elif _event == 'Quit':
            break

    _hunt_window.close()
