import PySimpleGUI as sg

from show_inventory import show_inventory
from inventoryAndStats import InventoryAndStats


# This file has lots of things that we can change and update for the second release

# Buying supplies at the beginning of the game(Logic here can be revisited)
def buy_supplies(inventory: InventoryAndStats):
    """open the store window which allows the player
    to buy items with their money until closed"""
    # Starting money(This can change)
    _total_money = 700
    # Set the player's starting money
    inventory.set_money(_total_money)
    # This is what the store window will look like(This can be changed)
    _layout = [
        [sg.Text('Welcome to the Store!', font=('Helvetica', 20))],
        [sg.Text(f'You have ${inventory.get_money()} to spend.',
                 font=('Helvetica', 14), key="-MONEY-")],
        [sg.Text('How many oxen do you want to purchase? at least 2 are required. ($100 each)',
                 font=('Helvetica', 14))],
        [sg.InputText(size=(5, 1), key='-OXEN-')],
        [sg.Text('How many pounds of food would you like to purchase? ($1/lbs)',
                 font=('Helvetica', 14))],
        [sg.InputText(size=(5, 1), key='-FOOD-')],
        [sg.Text('How many cases of ammunition would you like to purchase? ($15/case of six)',
                 font=('Helvetica', 14))],
        [sg.InputText(size=(5, 1), key='-AMMO-')],
        [sg.Text('How many sets of clothing would you like to purchase? ($20/set)',
                 font=('Helvetica', 14))],
        [sg.InputText(size=(5, 1), key='-CLOTHING-')],
        [sg.Text('How many wagon parts would you like to purchase? ($50/set)',
                 font=('Helvetica', 14))],
        [sg.InputText(size=(5, 1), key='-PARTS-')],
        [sg.Text('How Much Medicine would you like to purchase? ($10 each)',
                 font=('Helvetica', 14))],
        [sg.InputText(size=(5, 1), key='-MEDICINE-')],
        [sg.Button('Buy', font=('Helvetica', 16)),
         sg.Button('Sell', font=('Helvetica', 16)),
         sg.Button('Recommendations', font=('Helvetica', 16)),
         sg.Button('Check Inventory', font=('Helvetica', 16)),
         sg.Button('Leave Store', font=('Helvetica', 16))]

    ]

    _store_window = sg.Window('Store', _layout)  # Create store window

    while True:  # Event loop
        _event, _values = _store_window.read()
        if _event == sg.WINDOW_CLOSED:
            break
        elif _event == 'Leave Store':
            # Check oxen spending
            if inventory.get_oxen() < 2:
                sg.popup('Invalid amount of oxen. '
                         'you should have at least 2.', title='purchase more oxen')
            else:
                break

        elif _event == 'Buy':
            try:  # Here I parsed spending amounts(this logic can be changed)
                _oxen_spent = int(_values['-OXEN-']) * 100 if _values['-OXEN-'] else 0
                _food_spent = int(_values['-FOOD-']) if _values['-FOOD-'] else 0
                _ammo_spent = int(_values['-AMMO-']) * 15 if _values['-AMMO-'] else 0
                _clothing_spent = int(_values['-CLOTHING-']) * 20 if _values['-CLOTHING-'] else 0
                _parts_spent = int(_values['-PARTS-']) * 50 if _values['-PARTS-'] else 0
                _medicine_spent = int(_values['-MEDICINE-']) * 10 if _values['-MEDICINE-'] else 0

                # Check total spending
                _total_spent = (_oxen_spent + _food_spent + _ammo_spent + _clothing_spent
                                + _parts_spent + _medicine_spent)
                if _total_spent > _total_money:
                    sg.popup('You do not have enough money '
                             'to make this purchase.', title='not enough money')
                    continue
                else:
                    # Update player stats
                    # Assume 1 ox costs $100
                    inventory.set_oxen(inventory.get_oxen() + _oxen_spent//100)
                    # eventually change the cost of items
                    inventory.set_food(inventory.get_food() + _food_spent)
                    # so they don't all cost $1
                    inventory.set_ammo(inventory.get_ammo() + (_ammo_spent//15) * 6)
                    inventory.set_clothes(inventory.get_clothes() + _clothing_spent//20)
                    inventory.set_parts(inventory.get_parts() + _parts_spent//50)
                    inventory.set_medicine(inventory.get_medicine() + _medicine_spent//10)
                    inventory.set_money(inventory.get_money() - _total_spent)
                    _store_window['-MONEY-'].update(f'You have ${inventory.get_money()} to spend.')
                    _total_money = inventory.get_money()
                    # Summary of everything the user bought
                    # (This output can be changed)
                    sg.popup(f'You spent:\nOxen: ${_oxen_spent}\n'
                             f'Food: ${_food_spent}\n'
                             f'Ammunition: ${_ammo_spent}\n'
                             f'Clothing: ${_clothing_spent}\n'
                             f'Parts: ${_parts_spent}\n'
                             f'Medicine: ${_medicine_spent}\n'
                             f'You now have ${inventory.get_money()} left.', title='purchase complete')
                    _store_window['-OXEN-'].update(value="")
                    _store_window['-FOOD-'].update(value="")
                    _store_window['-AMMO-'].update(value="")
                    _store_window['-CLOTHING-'].update(value="")
                    _store_window['-PARTS-'].update(value="")
                    _store_window['-MEDICINE-'].update(value="")

            except ValueError:
                sg.popup('Please enter valid numbers for your purchases.', title='value error')
        elif _event == 'Sell':
            try:
                _oxen_sold = int(_values['-OXEN-']) * 100 if _values['-OXEN-'] else 0
                _food_sold = int(_values['-FOOD-']) if _values['-FOOD-'] else 0
                _ammo_sold = int(_values['-AMMO-']) * 15 if _values['-AMMO-'] else 0
                _clothing_sold = int(_values['-CLOTHING-']) * 20 if _values['-CLOTHING-'] else 0
                _parts_sold = int(_values['-PARTS-']) * 50 if _values['-PARTS-'] else 0
                _medicine_sold = int(_values['-MEDICINE-']) * 10 if _values['-MEDICINE-'] else 0

                _total_sold = (_oxen_sold + _food_sold + _ammo_sold + _clothing_sold
                               + _parts_sold + _medicine_sold)
                if ((_oxen_sold//100 > inventory.get_oxen() or _food_sold > inventory.get_food()
                        or (_ammo_sold//15) * 6 > inventory.get_ammo()
                        or _clothing_sold//20 > inventory.get_clothes()
                        or _parts_sold//50 > inventory.get_parts())
                        or _medicine_sold//10 > inventory.get_medicine()):
                    sg.popup('You do not have items '
                             'to sell these amounts.', title='not enough items')
                    continue
                else:
                    # Update player stats
                    # Assume 1 ox costs $100
                    inventory.set_oxen(inventory.get_oxen() - _oxen_sold//100)
                    # eventually change the cost of items
                    inventory.set_food(inventory.get_food() - _food_sold)
                    # so they don't all cost $1
                    inventory.set_ammo(inventory.get_ammo() - (_ammo_sold//15) * 6)
                    inventory.set_clothes(inventory.get_clothes() - _clothing_sold//20)
                    inventory.set_parts(inventory.get_parts() - _parts_sold//50)
                    inventory.set_medicine(inventory.get_medicine() - _medicine_sold//10)
                    inventory.set_money(inventory.get_money() + _total_sold)
                    _store_window['-MONEY-'].update(f'You have ${inventory.get_money()} to spend.')
                    _total_money = inventory.get_money()
                    # Summary of everything the user bought
                    # (This output can be changed)
                    sg.popup(f'You sold:\n${_oxen_sold} worth of oxen\n'
                             f'${_food_sold} worth of food\n'
                             f'${_ammo_sold} worth of ammunition\n'
                             f'${_clothing_sold} worth of clothing\n'
                             f'${_parts_sold} worth of parts\n'
                             f'${_medicine_sold} worth of medicine\n'
                             f'You now have ${inventory.get_money()} left.', title='selling complete')
                    _store_window['-OXEN-'].update(value="")
                    _store_window['-FOOD-'].update(value="")
                    _store_window['-AMMO-'].update(value="")
                    _store_window['-CLOTHING-'].update(value="")
                    _store_window['-PARTS-'].update(value="")
                    _store_window['-MEDICINE-'].update(value="")

            except ValueError:
                sg.popup('Please enter valid numbers for your items.', title='value error')
        elif _event == 'Check Inventory':
            show_inventory(inventory)
        elif _event == 'Recommendations':
            sg.popup(f'Recommended amounts:\n'
                     '3 oxen\n'
                     '100 lbs of food\n'
                     '4 cases of Ammunition, or 60 ammo\n'
                     '3 sets of clothing per party member\n'
                     '3 sets of wagon parts\n'
                     '3 Medicine\n', title='recommendations')
    _store_window.close()  # Closes window
