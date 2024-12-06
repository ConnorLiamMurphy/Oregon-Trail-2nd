import unittest
from encounters import Encounter  # Assuming you have the Encounter class in encounter.py


# Mock classes for InventoryAndStats and Actions
class MockInventory:
    def __init__(self):
        self.food = 10
        self.ammo = 5
        self.clothes = 3
        self.parts = 2
        self.medicine = 1
        self.oxen = 2
        self.money = 100
        self.morale = 50
        self.health = 80
        self.status = None

    def get_food(self):
        return self.food

    def get_ammo(self):
        return self.ammo

    def get_clothes(self):
        return self.clothes

    def get_parts(self):
        return self.parts

    def get_medicine(self):
        return self.medicine

    def get_oxen(self):
        return self.oxen

    def get_money(self):
        return self.money

    def get_morale(self):
        return self.morale

    def get_health(self):
        return self.health

    def set_food(self, value):
        self.food = value

    def set_ammo(self, value):
        self.ammo = value

    def set_clothes(self, value):
        self.clothes = value

    def set_parts(self, value):
        self.parts = value

    def set_medicine(self, value):
        self.medicine = value

    def set_oxen(self, value):
        self.oxen = value

    def set_money(self, value):
        self.money = value

    def set_morale(self, value):
        self.morale = value

    def set_health(self, value):
        self.health = value

    def set_status(self, value):
        self.status = value


class MockActions:
    def __init__(self):
        self.weather = 'Clear'
        self.travel_speed = 'Normal'
        self.rations = 'Standard'
        self.date = 0
        self.daily_food_loss = 1

    def get_weather(self):
        return self.weather

    def get_travel_speed(self):
        return self.travel_speed

    def get_rations(self):
        return self.rations

    def increment_date(self):
        self.date += 1

    def get_daily_food_loss(self):
        return self.daily_food_loss


class TestEncounter(unittest.TestCase):
    def setUp(self):
        # Create mock inventory and actions
        self.mock_inventory = MockInventory()
        self.mock_actions = MockActions()

        # Create an Encounter instance using mocked inventory and actions
        self.encounter = Encounter(self.mock_inventory, self.mock_actions)

    def test_load_stats(self):
        """Test if encounter stats are loaded properly."""
        Encounter._load_stats()
        # Verify that the stats are loaded into the _STATS list.
        self.assertGreater(len(Encounter._STATS), 0)

    def test_encounter_initialization(self):
        """Test if an encounter is initialized with correct values."""
        encounter = self.encounter

        # Check if the initial encounter values are correctly assigned.
        self.assertEqual(encounter.get_food_change(), encounter._food_change)
        self.assertEqual(encounter.get_ammo_change(), encounter._ammo_change)
        self.assertEqual(encounter.get_clothes_change(), encounter._clothes_change)
        self.assertEqual(encounter.get_parts_change(), encounter._parts_change)
        self.assertEqual(encounter.get_medicine_change(), encounter._medicine_change)
        self.assertEqual(encounter.get_oxen_change(), encounter._oxen_change)
        self.assertEqual(encounter.get_money_change(), encounter._money_change)
        self.assertEqual(encounter.get_morale_change(), encounter._morale_change)
        self.assertEqual(encounter.get_health_change(), encounter._health_change)



    def test_check_encounter_invalid(self):
        """Test if the check_encounter method correctly identifies a valid encounter."""
        encounter = self.encounter

        # Simulate that the inventory has sufficient food
        self.mock_inventory.food = 10
        self.assertFalse(encounter.check_encounter())

    def test_change_encounter(self):
        """Test if the change_encounter method properly updates the encounter."""
        encounter = self.encounter

        initial_name = encounter.get_name()
        encounter.change_encounter()
        new_name = encounter.get_name()

        # Ensure the encounter has changed after calling change_encounter
        self.assertNotEqual(initial_name, new_name)


if __name__ == "__main__":
    unittest.main()
