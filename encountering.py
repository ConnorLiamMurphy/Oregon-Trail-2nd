from encounters import Encounter
import PySimpleGUI as sg

from makeDecision import Decision


def encountering(encounter: Encounter):
    """open the encounter window until it is closed"""
    if encounter.get_prompt() == "True":
        _line_1, _line_2, _line_3 = encounter.get_name()
        _layout = [
            [sg.Text(f'{_line_1}', font=('Helvetica', 20))],
            [sg.Text(f'{_line_2}', font=('Helvetica', 20))],
            [sg.Text(f'{_line_3}', font=('Helvetica', 20))],
            [sg.Text('', font=('Helvetica', 20), key='-BAD_INPUT-')],
            [sg.Text(f'decision: ', font=('Helvetica', 20)),
             sg.Input(key='-INPUT-'),
             sg.Button('Submit')]
        ]
    else:
        _layout = [
            [sg.Text(f'{encounter.get_name()}', font=('Helvetica', 20))],
            [sg.Button('Return to Game', size=(15, 2), font=('Helvetica', 16))]
        ]

    _encounter_window = sg.Window('Encounter', _layout, size=(900, 600))

    while True:
        _event, _values = _encounter_window.read()
        if _event == 'Submit':
            _final_dec = Decision(encounter, _values["-INPUT-"])
            _valid_input = _final_dec.make_decision()
            if _valid_input:
                break
            else:
                _values["-INPUT-"] = ""
                _encounter_window['-BAD_INPUT-'].update('Bad Input')

        if _event == sg.WINDOW_CLOSED or _event == 'Return to Game':
            encounter.decision()
            break

    _encounter_window.close()
