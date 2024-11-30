import PySimpleGUI as sg

_button_image = r'images/continue.png'
def select_travel_parameters():
    """open the window to select the parameters and return their values once closed"""
    _layout = [
        [sg.Text('Select your travel speed (Slow, Moderate, Quick):', font=("arial", 16), text_color='white',
                 background_color='black')],
        [sg.Combo(['Slow', 'Moderate', 'Quick'], default_value='Moderate', key='-SPEED-', font=('arial', 14), size=(20, 1))],
        [sg.Text('Select ration size (light, standard, heavy):', font=("arial", 16), text_color='white',
                 background_color='black')],
        [sg.Combo(['Light', 'Standard', 'Heavy'], default_value='Standard', key='-RATIONS-', font=('arial', 14), size=(20, 1))],
        [sg.Text('Select leave date (March, April, May, June):', font=("arial",16), text_color='white',
                 background_color='black')],
        [sg.Combo(['Mar', 'Apr', 'May', 'Jun'], default_value='Apr', key='-DATE-', font=('arial', 14), size=(20, 1))],
        [sg.Button('Confirm', size=(10, 3), font="arial", image_filename = _button_image, button_color = ("black", "black"), border_width=0,
                   pad=(10, 10))],
    ]

    _window = sg.Window('Travel Parameters', _layout, size=(600, 300), finalize=True)

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


def select_class_parameters():   #FIXME
    """set the values of the players class from the GUI"""
    _layout = [
        # Display the background image

        # Text for character class selection
        [sg.Text('Select your character class (Merchant, Hunter, Guide):',
                 font=('arial', 16), text_color='white', background_color='black', justification='center')],
        [sg.Combo(['Hunter', 'Merchant', 'Guide'], default_value='Hunter', key='-CLASS-', font=('arial', 14),
                  size=(20, 1))],
        [sg.Text('Select your starting weapon (Rifle, Knife, Axe):',
                 font=('Helvetica', 16), text_color='white', background_color='black', justification='center')],
        [sg.Combo(['Knife', 'Rifle', 'Axe'], default_value='Knife', key='-WEAPON-', font=('arial', 14),
                  size=(20, 1))],
        [sg.Text('Select your starting skill (Strength, Magic, Stealth):',
                 font=('Helvetica', 16), text_color='white', background_color='black', justification='center')],
        [sg.Combo(['Strength', 'Magic', 'Stealth'], default_value='Strength', key='-SKILL-', font=('arial', 14),
                  size=(20, 1))],
        [sg.Button('Confirm', size=(10, 3), font=('Helvetica', 16), image_filename = _button_image,
                   button_color = ("black", "black"), pad=(10, 10))]
    ]

    _window = sg.Window('Choose Class', _layout, size=(600, 300), finalize=True)

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