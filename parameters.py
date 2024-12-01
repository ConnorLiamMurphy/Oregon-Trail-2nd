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
    def __init__(self, char_class):
        self.char_class = char_class
        self.money = self.assign_money()
        self.food = 10  # Default food
        self.health = 10  # Default health
        self.morale = 10  # Default morale

    def assign_money(self):
        """Assign money based on the character class."""
        money_by_class = {
            'Hunter': 100,
            'Merchant': 200,
            'Guide': 150
        }
        return money_by_class.get(self.char_class, 100)  # Default to 100 if class not found

    def get_inventory(self):
        """Return the character's inventory."""
        return {
            'Food': self.food,
            'Health': self.health,
            'Morale': self.morale,
            'Money': self.money
        }

    def update_inventory(self, food_change=0, health_change=0, morale_change=0):
        """Update the inventory based on trade outcomes."""
        self.food += food_change
        self.health += health_change
        self.morale += morale_change

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

if __name__ == "__main__":
    # Call the function and display the selected options
    selected_class, selected_weapon = select_class_parameters()
    character = Character(selected_class)
    print(f"Class: {character.char_class}, Weapon: {selected_weapon}, Money: {character.money}")
