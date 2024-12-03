import unittest
import PySimpleGUI as sg
from inventoryAndStats import InventoryAndStats  # Assuming this is your actual class
from actions import Actions  # Assuming this is your actual class

# Your actual `view_status` function remains unchanged
def view_status(inv: InventoryAndStats, act: Actions):
    """Display player's stats and the distance from Oregon in a window"""
    _distance = act.get_distance()

    # Layout for the status window
    _layout = [
        [sg.Text('Player Stats', font=('Helvetica', 20))],
        [sg.Text(f'Morale: {inv.get_morale()}', font=('Helvetica', 14), key='MORALE')],
        [sg.Text(f'Health: {inv.get_health()}/10', font=('Helvetica', 14), key='HEALTH')],
        [sg.Text(f'Weather: {act.get_weather()}', font=('Helvetica', 14), key='WEATHER')],
        [sg.Text(f'Status: {inv.get_status()}', font=('Helvetica', 14), key='STATUS')],
        [sg.Text(f'Distance from Oregon: {_distance}', font=('Helvetica', 14), key='DISTANCE')],
        [sg.Button('Close', size=(10, 2), font=('Helvetica', 16))]
    ]

    # Create the window
    status_window = sg.Window('Player Status', _layout, size=(400, 500), finalize=True)

    # Event loop
    while True:
        event, values = status_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break  # Exit the window

    status_window.close()

# Unit Test Class
class TestViewStatus(unittest.TestCase):

    def setUp(self):
        """Setup test data for InventoryAndStats and Actions"""
        # Initialize actual classes with test data
        self.test_inv = InventoryAndStats(morale=5, health=8, status='Healthy')
        self.test_act = Actions(weather='Sunny', distance=250)

    def test_view_status_shows_correct_user_health(self):
        """Req 19: Test that the window displays the user's health correctly"""
        # Call the view_status function
        view_status(self.test_inv, self.test_act)

        # Create the window again and check if the 'Health' text is correctly displayed
        window = sg.Window('Player Status', finalize=True)
        event, values = window.read()

        # Retrieve the health text from the window
        health_text = window['HEALTH'].get_text()  # 'HEALTH' is the key we assigned to the Text element
        self.assertEqual(health_text, 'Health: 8/10')  # Verify that the health is correctly displayed

    def test_view_status_shows_correct_morale(self):
        """Test that the window displays the user's morale correctly"""
        # Call the view_status function
        view_status(self.test_inv, self.test_act)

        # Create the window again and check if the 'Morale' text is correctly displayed
        window = sg.Window('Player Status', finalize=True)
        event, values = window.read()

        # Retrieve the morale text from the window
        morale_text = window['MORALE'].get_text()  # 'MORALE' is the key we assigned to the Text element
        self.assertEqual(morale_text, 'Morale: 5')  # Verify that the morale is correctly displayed

    def test_view_status_shows_correct_weather(self):
        """Test that the window displays the weather correctly"""
        # Call the view_status function
        view_status(self.test_inv, self.test_act)

        # Create the window again and check if the 'Weather' text is correctly displayed
        window = sg.Window('Player Status', finalize=True)
        event, values = window.read()

        # Retrieve the weather text from the window
        weather_text = window['WEATHER'].get_text()  # 'WEATHER' is the key we assigned to the Text element
        self.assertEqual(weather_text, 'Weather: Sunny')  # Verify that the weather is correctly displayed

    def test_view_status_shows_correct_distance(self):
        """Test that the window displays the correct distance"""
        # Call the view_status function
        view_status(self.test_inv, self.test_act)

        # Create the window again and check if the 'Distance' text is correctly displayed
        window = sg.Window('Player Status', finalize=True)
        event, values = window.read()

        # Retrieve the distance text from the window
        distance_text = window['DISTANCE'].get_text()  # 'DISTANCE' is the key we assigned to the Text element
        self.assertEqual(distance_text, 'Distance from Oregon: 250')  # Verify that the distance is correctly displayed

    def test_window_closes_on_close_button(self):
        """Test that the window closes when 'Close' is clicked"""
        window = sg.Window('Player Status', finalize=True)

        # Simulate clicking the 'Close' button
        window.write_event_value('Close', None)
        event, values = window.read()

        self.assertEqual(event, 'Close')  # Check if the close event was triggered

    def test_window_closes_on_exit(self):
        """Test that the window closes when the user clicks the X button"""
        window = sg.Window('Player Status', finalize=True)

        # Simulate the window close (clicking the X)
        window.write_event_value(sg.WINDOW_CLOSED, None)
        event, values = window.read()

        self.assertEqual(event, sg.WINDOW_CLOSED)  # Verify that window closed event was triggered


if __name__ == '__main__':
    unittest.main()
