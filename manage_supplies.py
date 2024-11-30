from actions import Actions
import PySimpleGUI as sg

from inventoryAndStats import InventoryAndStats
from show_inventory import show_inventory


def manage_supplies(act: Actions, inv: InventoryAndStats):
    """allow the user to manage and use their supplies in the GUI"""
    _layout = [
        [sg.Text('Select your travel speed (Slow, Moderate, Quick):')],
        [sg.Combo(['Slow', 'Moderate', 'Quick'], default_value=f'{act.get_travel_speed()}', key='-SPEED-')],
        [sg.Text('Select ration size (light, standard, heavy):')],
        [sg.Combo(['Light', 'Standard', 'Heavy'], default_value=f'{act.get_rations()}', key='-RATIONS-')],
        [sg.Button('Use Medicine', size=(10, 2), font=('Helvetica', 16)),
         sg.Button('Fix Ship', size=(10, 2), font=('Helvetica', 16))],
        [sg.Button('Confirm', size=(10, 2), font=('Helvetica', 16))]
    ]

    _Broken_layout = [
        [sg.Text('Select your travel speed:')],
        [sg.Combo(['Broken'], default_value=f'{act.get_travel_speed()}', key='-SPEED-')],
        [sg.Text('Select ration size (light, standard, heavy):')],
        [sg.Combo(['Light', 'Standard', 'Heavy'], default_value=f'{act.get_rations()}', key='-RATIONS-')],
        [sg.Button('Use Medicine', size=(10, 2), font=('Helvetica', 16)),
         sg.Button('Fix Ship', size=(10, 2), font=('Helvetica', 16))],
        [sg.Button('Confirm', size=(10, 2), font=('Helvetica', 16))]
    ]

    _No_Oxen_layout = [
        [sg.Text('Select your travel speed:')],
        [sg.Combo(['No Oxen'], default_value=f'{act.get_travel_speed()}', key='-SPEED-')],
        [sg.Text('Select ration size (light, standard, heavy):')],
        [sg.Combo(['Light', 'Standard', 'Heavy'], default_value=f'{act.get_rations()}', key='-RATIONS-')],
        [sg.Button('Use Medicine', size=(10, 2), font=('Helvetica', 16)),
         sg.Button('Fix Ship', size=(10, 2), font=('Helvetica', 16)),
         sg.Button('Check Inventory', size=(15, 2), font=('Helvetica', 16))],
        [sg.Button('Confirm', size=(10, 2), font=('Helvetica', 16))]
    ]

    if act.get_travel_speed() == 'Broken':
        _supply_window = sg.Window('Manage Supplies', _Broken_layout, size=(500, 400), finalize=True)
    elif act.get_travel_speed() == 'No_Oxen':
        _supply_window = sg.Window('Manage Supplies', _No_Oxen_layout, size=(500, 400), finalize=True)
    else:
        _supply_window = sg.Window('Manage Supplies', _layout, size=(500, 400), finalize=True)

    # Event loop
    while True:
        _event, _values = _supply_window.read()
        if _event == sg.WINDOW_CLOSED or _event == 'Quit':
            break  # Exit loop here
        elif _event == 'Fix Ship':
            if act.get_travel_speed() == 'Broken':
                if inv.get_parts() > 0:
                    act.set_travel_speed('Moderate')
                    inv.set_parts(inv.get_parts() - 1)
                    _supply_window.close()  # Close the current window
                    # open with new layout
                    _supply_window = sg.Window("Game", _layout, size=(500, 400), finalize=True)
                    _supply_window['-SPEED-'].update(value=act.get_travel_speed())
                else:
                    sg.popup('You don\'t have the supplies to fix the ship', title='No parts')
            else:
                sg.popup('There is nothing to fix', title='Not Broken')

        elif _event == 'Use Medicine':
            if inv.get_health() < 10 or inv.get_status() != 'Healthy':
                if inv.get_medicine() > 0:
                    inv.set_health(inv.get_health() + 2)
                    inv.set_medicine(inv.get_medicine() - 1)
                    inv.set_status('Healthy')
                else:
                    sg.popup('you don\'t have the medicine to use any', title='no medicine')
            else:
                sg.popup('you are perfectly healthy, no need for medicine', title='full health')
        elif _event == 'Confirm':
            act.set_travel_speed(_values['-SPEED-'])
            act.set_rations(_values['-RATIONS-'])
            break

    _supply_window.close()
