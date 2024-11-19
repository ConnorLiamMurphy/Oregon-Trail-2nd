import PySimpleGUI as sg
from actions import Actions


def traveling(act: Actions):
    """show the window that displays the traveling progress of the player when not at a landmark."""
    # game states and other variables
    _distance = act.get_distance()

    _layout = [
        [sg.Text(f'Distance from Oregon: {_distance}',
                 font=('Helvetica', 16), key='-DISTANCE-')],
        [sg.Text(f'Date: {act.get_date()}',
                 font=('Helvetica', 16), key='-DATE-')]
    ]

    _travel_window = sg.Window('Game', _layout, size=(500, 400))

    # game loop
    while True:
        _event, _values = _travel_window.read(timeout=1000)
        # a landmark returns a string, traveling returns
        # an int, an encounter returns an Encounter
        if isinstance(_distance, str):
            act.set_encountered(True)
            break
        elif isinstance(_distance, int):
            act.set_encountered(False)
            _travel_window['-DISTANCE-'].update(
                f'Distance from Oregon: {_distance}')
            _travel_window['-DATE-'].update(
                f'Date: {act.get_date()}')
            _distance = act.travel()
            # Check if food is sufficient
            if act.get_inventory().get_food() <= 0:
                _distance = None
                break
        else:
            break
        if _event == sg.WINDOW_CLOSED:
            break

    _travel_window.close()
    return _distance
