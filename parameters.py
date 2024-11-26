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
            _travel_speed = 'Moderate'
            _rations = 'Standard'
            _date = 'Apr'
            break
        elif _event == 'Confirm':
            _travel_speed = _values['-SPEED-']
            _rations = _values['-RATIONS-']
            _date = _values['-DATE-']
            break

    _window.close()
    return _travel_speed, _rations, _date


def select_class_parameters():
    _layout = [
        [sg.Text('Select your character class (Merchant, Hunter, Guide):')],
        [sg.Combo(['Hunter', 'Merchant', 'Guide'], default_value='Hunter', key='-CLASS-')],
        [sg.Text('Select your starting weapon (Rifle, Knife, Axe):')],
        [sg.Combo(['Knife', 'Rifle', 'Axe'], default_value='Knife', key='-WEAPON-')],
        [sg.Text('Select your starting skill (Strength, Magic, Stealth):')],
        [sg.Combo(['Strength', 'Magic', 'Stealth'], default_value='Strength', key='-SKILL-')],
        [sg.Button('Confirm', size=(10, 2), font=('Helvetica', 16))]
    ]

    _window = sg.Window('Choose Class', _layout, size=(400, 250), finalize=True)

    while True:
        _event, _values = _window.read()
        if _event == sg.WINDOW_CLOSED:
            _class = 'Hunter'
            _weapon = 'Knife'
            _skill = 'Strength'
            break
        elif _event == 'Confirm':
            _class = _values['-CLASS-']
            _weapon = _values['-WEAPON-']
            _skill = _values['-SKILL-']
            break

    _window.close()
    return _class, _weapon, _skill

