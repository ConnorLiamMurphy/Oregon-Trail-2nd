import unittest
from inventoryAndStats import InventoryAndStats
from actions import Actions
from parameters import Character
from landmarks import Landmark


def get_mock_inventory():
    inv = InventoryAndStats(100, 10, 10, 2, 2, 3, 200, 10, 10, Character("Hunter", "Axe"))
    return inv


class TestActions(unittest.TestCase):

    def setUp(self):
        self.mock_inventory = get_mock_inventory()
        Landmark._LOCATIONS = []
        Landmark._load_locations()

        self.mock_character = Character("Hunter", "Axe")
        self.actions = Actions(distance=100,
                               inventory=self.mock_inventory,
                               travel_speed="Moderate",
                               rations="Standard",
                               date="Apr",
                               char=self.mock_character)

    def test_initialization(self):
        self.assertEqual(self.actions._distance, 100)
        self.assertEqual(self.actions._rations, "Standard")
        self.assertEqual(self.actions._daily_food_loss, 5)
        self.assertEqual(self.actions._miles_per_day, 10)
        self.assertEqual(self.actions._weather, "Normal Oxygen Levels")

    def test_travel(self):
        self.actions.travel()
        self.assertEqual(self.actions._distance, 90)
        self.assertEqual(self.mock_inventory.get_food(), 95)

    def test_travel_with_zero_speed(self):

        self.actions.set_travel_speed("No Oxen")
        self.actions.travel()
        self.assertEqual(self.actions._distance, 99)
        self.assertEqual(self.mock_inventory.get_food(), 95)

    def test_change_date_across_months(self):
        """Test date transition across months."""
        self.actions._current_date = "03/31"
        self.actions.increment_date()
        self.assertEqual(self.actions._current_date, "04/01")

    def test_change_date_at_year_end(self):
        self.actions._current_date = "12/31"
        self.actions.increment_date()
        self.assertEqual(self.actions._current_date, "01/01")


    def test_set_encountered(self):
        self.actions.set_encountered(True)
        self.assertTrue(self.actions._encountered)

    def test_set_rations(self):
        self.actions.set_rations('Heavy')
        self.assertEqual(self.actions._rations, 'Heavy')
        self.assertEqual(self.actions._daily_food_loss, 8)

    def test_set_travel_speed(self):
        self.actions.set_travel_speed('Quick')
        self.assertEqual(self.actions._miles_per_day, 15)

    def test_get_weather(self):
        self.assertEqual(self.actions.get_weather(), "Normal Oxygen Levels")

    def test_increment_date(self):
        old_date = self.actions.get_date()
        self.actions.increment_date()
        new_date = self.actions.get_date()
        self.assertNotEqual(old_date, new_date)


if __name__ == "__main__":
    unittest.main()
