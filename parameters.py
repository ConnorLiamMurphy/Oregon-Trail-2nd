import PySimpleGUI as sg
import random


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


class Character:
    """store the data of your character class"""

    def __init__(self, char_class, char_weapon):
        self._char_class = char_class
        self._char_weapon = char_weapon
        self._money = self.assign_money()
        self._food = self.assign_food()
        self._health = self.assign_health()
        self._morale = self.assign_morale()

    def assign_money(self):
        """Assign money based on the character class."""
        money_by_class = {
            'Hunter': 700,
            'Merchant': 1000,
            'Guide': 850
        }
        return money_by_class.get(self._char_class, 700)  # Default to 700 if class not found

    def assign_food(self):
        """Assign food based on the character class."""
        food_by_class = {
            'Hunter': 15,
            'Merchant': 10,
            'Guide': 5
        }
        return food_by_class.get(self._char_class, 10)  # Default to 10 if class not found

    def assign_health(self):
        """Assign health based on the character class."""
        health_by_class = {
            'Hunter': 15,
            'Merchant': 12,
            'Guide': 10
        }
        return health_by_class.get(self._char_class, 10)  # Default to 100 if class not found

    def assign_morale(self):
        """Assign morale based on the character class."""
        morale_by_class = {
            'Hunter': 5,
            'Merchant': 8,
            'Guide': 10
        }
        return morale_by_class.get(self._char_class, 5)  # Default to 5 if class not found

    def get_inventory(self):
        """Return the character's inventory."""
        return {
            'Food': self._food,
            'Health': self._health,
            'Morale': self._morale,
            'Money': self._money
        }

    def update_inventory(self, food_change=0, health_change=0, morale_change=0):
        """Update the inventory"""
        self._food += food_change
        self._health += health_change
        self._morale += morale_change

    def get_class_food(self):
        """return the amount of food you get from your class"""
        return self._food

    def get_class_money(self):
        """return the amount of money you get from your class"""
        return self._money

    def get_class_morale(self):
        """return the amount of morale you get from your class"""
        return self._morale

    def get_class_health(self):
        """return the amount of health you get from your class"""
        return self._health

    def get_weapon(self):
        """return your chosen weapon"""
        return self._char_weapon


def select_class_parameters():
    """Display a GUI for selecting character class and weapon."""
    # Define the layout of the window
    _layout = [
        [sg.Text('Select your character class:', font=('Helvetica', 12))],
        [sg.Combo(['Hunter', 'Merchant', 'Guide'], default_value='Hunter', key='-CLASS-', font=('Helvetica', 10))],
        [sg.Text('Select your starting weapon:', font=('Helvetica', 12))],
        [sg.Combo(['Knife', 'Rifle', 'Axe'], default_value='Knife', key='-WEAPON-', font=('Helvetica', 10))],
        [sg.Button('Confirm', size=(10, 2), font=('Helvetica', 16))]
    ]

    # Create the window
    _window = sg.Window('Choose Class', _layout, size=(400, 200), finalize=True)

    # Event loop for the window
    while True:
        _event, _values = _window.read()
        if _event == sg.WINDOW_CLOSED:  # Handle window close
            _class, _weapon = 'Hunter', 'Knife'
            break
        elif _event == 'Confirm':  # Handle confirm button
            _class = _values.get('-CLASS-', 'Hunter')
            _weapon = _values.get('-WEAPON-', 'Knife')
            break

    _window.close()
    return _class, _weapon
