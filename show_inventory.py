import PySimpleGUI as sg
from inventoryAndStats import InventoryAndStats


def show_inventory(inventory: InventoryAndStats):
    # When the player clicks show inventory, we run this function
    # This is what the inventory will actually look like( This can be changed)
    """open a window that displays the players inventory until closed"""
    _inventory_layout = [
        [sg.Text('Inventory', font=('Helvetica', 20))],
        [sg.Text(f'Food: {inventory.get_food()}', font=('Helvetica', 16))],
        [sg.Text(f'Ammo: {inventory.get_ammo()}', font=('Helvetica', 16))],
        [sg.Text(f'Clothes: {inventory.get_clothes()}', font=('Helvetica', 16))],
        [sg.Text(f'Ship Parts: {inventory.get_parts()}', font=('Helvetica', 16))],
        [sg.Text(f'Engines: {inventory.get_oxen()}', font=('Helvetica', 16))],
        [sg.Text(f'Medicine: {inventory.get_medicine()}', font=('Helvetica', 16))],
        [sg.Text(f'money: {inventory.get_money()}', font=('Helvetica', 16))],
        [sg.Button('Return to Game', size=(15, 2), font=('Helvetica', 16))]
    ]

    # What the inventory window looks like(This can be changed)
    _inventory_window = sg.Window('Inventory', _inventory_layout, size=(300, 350))

    while True:
        _event, _values = _inventory_window.read()
        if _event == sg.WINDOW_CLOSED or _event == 'Return to Game':
            break

    _inventory_window.close()  # Close window
