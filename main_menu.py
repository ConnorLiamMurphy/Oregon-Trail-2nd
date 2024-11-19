import PySimpleGUI as sg
from start_game import start_game


def main_menu():
    """open the main menu window until it is classed"""
    # Background image(This is a placeholder)
    _background_image_path = r'images/main_menu_background.png'

    # This is what the menu will look like(This can be changed)
    _layout = [
        [sg.Image(_background_image_path, key='-BACKGROUND-', size=(721, 473))],
        [sg.Text('Welcome to The Oregon Trail!', font=('Arial', 24), text_color='white',
                 pad=(10, 10), justification='center')],
        [sg.Button('Start', size=(10, 2), font=('Arial', 16),
                   button_color=('black', '#4E8C31'), pad=(10, 10)),
         sg.Button('Quit', size=(10, 2), font=('Arial', 16),
                   button_color=('black', '#B72A2A'), pad=(10, 10))]
    ]

    # This is what the menu will look like(This can be changed)
    _window = sg.Window('Game Menu', _layout, finalize=True, element_justification='center',
                        resizable=False, background_color='#000000')

    # Resize the window to fit the image
    _window.size = (800, 600)

    while True:
        _event, _values = _window.read()
        if _event == sg.WINDOW_CLOSED or _event == 'Quit':
            break
        elif _event == 'Start':
            _window.close()  # Close the menu window
            start_game()  # Start the game after the intro
            break

    _window.close()  # Closes window
