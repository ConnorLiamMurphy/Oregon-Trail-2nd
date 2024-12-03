import PySimpleGUI as sg
import random

_button_image = r'images/continue.png'


def select_travel_parameters():
    """open the window to select the parameters and return their values once closed"""
    _layout = [
        [sg.Text('Select your travel speed (Slow, Moderate, Quick):', font=("arial", 16), text_color='white',
                 background_color='black')],
        [sg.Combo(['Slow', 'Moderate', 'Quick'], default_value='Moderate', key='-SPEED-', font=('arial', 14),
                  size=(20, 1))],
        [sg.Text('Select ration size (light, standard, heavy):', font=("arial", 16), text_color='white',
                 background_color='black')],
        [sg.Combo(['Light', 'Standard', 'Heavy'], default_value='Standard', key='-RATIONS-', font=('arial', 14),
                  size=(20, 1))],
        [sg.Text('Select leave date (March, April, May, June):', font=("arial", 16), text_color='white',
                 background_color='black')],
        [sg.Combo(['Mar', 'Apr', 'May', 'Jun'], default_value='Apr', key='-DATE-', font=('arial', 14), size=(20, 1))],
        [sg.Button('Confirm', size=(10, 3), font="arial", image_filename=_button_image, button_color=("black", "black"),
                   border_width=0,
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
            'Alien Hunter': 700,
            'Space Trader': 1000,
            'Astro Explorer': 850
        }
        return money_by_class.get(self._char_class, 700)  # Default to 700 if class not found

    def assign_food(self):
        """Assign food based on the character class."""
        food_by_class = {
            'Alien Hunter': 15,
            'Space Trader': 10,
            'Astro Explorer': 5
        }
        return food_by_class.get(self._char_class, 10)  # Default to 10 if class not found

    def assign_health(self):
        """Assign health based on the character class."""
        health_by_class = {
            'Alien Hunter': 15,
            'Space Trader': 12,
            'Astro Explorer': 10
        }
        return health_by_class.get(self._char_class, 10)  # Default to 100 if class not found

    def assign_morale(self):
        """Assign morale based on the character class."""
        morale_by_class = {
            'Alien Hunter': 5,
            'Space Trader': 8,
            'Astro Explorer': 10
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

        # Display the background image

        # Text for character class selection
        [sg.Text('Select your character class (Alien Hunter, Space Trader, Astro Explorer):',
                 font=('arial', 16), text_color='white', background_color='black', justification='center')],
        [sg.Combo(['Alien Hunter', 'Space Trader', 'Astro Explorer'],
                  default_value='Alien Hunter', key='-CLASS-',
                  font=('arial', 14),
                  size=(20, 1))],
        [sg.Text('Select your starting weapon (Rifle, Knife, Axe):',
                 font=('Helvetica', 16), text_color='white', background_color='black', justification='center')],
        [sg.Combo(['Light saber', 'Laser blaster', 'Gravity hammer'],
                  default_value='Light saber', key='-WEAPON-',
                  font=('arial', 14),
                  size=(20, 1))],
        [sg.Button('Confirm', size=(10, 3), font=('Helvetica', 16), image_filename=_button_image,
                   button_color=("black", "black"), pad=(10, 10))]
    ]

    _window = sg.Window('Choose Class', _layout, size=(600, 300), finalize=True)

    # Event loop for the window
    while True:
        _event, _values = _window.read()
        if _event == sg.WINDOW_CLOSED:  # Handle window close
            _class, _weapon = 'Alien Hunter', 'Knife'
            break
        elif _event == 'Confirm':  # Handle confirm button
            _class = _values.get('-CLASS-', 'Alien Hunter')
            _weapon = _values.get('-WEAPON-', 'Knife')
            break

    _window.close()

    return _class, _weapon
