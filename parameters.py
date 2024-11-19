import PySimpleGUI as sg


def select_travel_parameters():
    """open the window to select the parameters and return their values once closed"""
    _layout = [
        [sg.Text('Select your travel speed (Slow, Moderate, Quick):')],
        [sg.Combo(['Slow', 'Moderate', 'Quick'], default_value='Moderate', key='-SPEED-')],
        [sg.Text('Select ration size (light, standard, heavy):')],
        [sg.Combo(['Light', 'Standard', 'Heavy'], default_value='Standard', key='-RATIONS-')],
        [sg.Text('Select leave date (March, April, May, June):')],
        [sg.Combo(['Mar', 'Apr', 'May', 'Jun'], default_value=f'Apr', key='-DATE-')],
        [sg.Button('Confirm', size=(10, 2), font=('Helvetica', 16))],
    ]

    _window = sg.Window('Travel Parameters', _layout, size=(400, 200), finalize=True)

    while True:  # Event loop
        _event, _values = _window.read()
        if _event == sg.WINDOW_CLOSED:
            break
        elif _event == 'Confirm':
            _travel_speed = _values['-SPEED-']
            _rations = _values['-RATIONS-']
            _date = _values['-DATE-']
            break

    _window.close()
    if _travel_speed and _rations and _date:
        return _travel_speed, _rations, _date
    return 'Moderate', 'Standard', 'Apr'  # Default values if window is closed
