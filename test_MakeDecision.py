import unittest
from makeDecision import Decision


class MockEncounter:
    """A simple mock version of the Encounter class for testing."""

    def __init__(self, original_name, extra_change=None):
        self.original_name = original_name
        self.extra_change = extra_change
        self.food_change = 0
        self.ammo_change = 0
        self.clothes_change = 0
        self.parts_change = 0
        self.medicine_change = 0
        self.oxen_change = 0
        self.money_change = 0
        self.morale_change = 0
        self.health_change = 0

    def get_original_name(self):
        return self.original_name

    def get_extra_change(self):
        return self.extra_change

    def set_food_change(self, change):
        self.food_change = change

    def set_ammo_change(self, change):
        self.ammo_change = change

    def set_clothes_change(self, change):
        self.clothes_change = change

    def set_parts_change(self, change):
        self.parts_change = change

    def set_medicine_change(self, change):
        self.medicine_change = change

    def set_oxen_change(self, change):
        self.oxen_change = change

    def set_money_change(self, change):
        self.money_change = change

    def set_morale_change(self, change):
        self.morale_change = change

    def set_health_change(self, change):
        self.health_change = change

    def set_extra_change(self, change):
        self.extra_change = change


class TestDecision(unittest.TestCase):

    def setUp(self):
        # Prepare mock encounter object for testing
        self.mock_encounter = MockEncounter("One of your engines is broken.", "None")

    def test_valid_decision(self):
        """Test if a valid decision updates the encounter correctly."""
        decision = Decision(self.mock_encounter, 2)
        decision.make_decision()

        # Assert changes in encounter
        self.assertEqual(self.mock_encounter.food_change, 0)
        self.assertEqual(self.mock_encounter.ammo_change, 0)
        self.assertEqual(self.mock_encounter.clothes_change, 0)
        self.assertEqual(self.mock_encounter.parts_change, 0)
        self.assertEqual(self.mock_encounter.medicine_change, 0)
        self.assertEqual(self.mock_encounter.oxen_change, 0)
        self.assertEqual(self.mock_encounter.money_change, 0)
        self.assertEqual(self.mock_encounter.morale_change, 0)
        self.assertEqual(self.mock_encounter.health_change, 0)
        self.assertEqual(self.mock_encounter.extra_change, "None")

    def test_invalid_decision(self):
        """Test if an invalid decision returns False and doesn't update encounter."""
        self.mock_encounter = MockEncounter("Invalid Encounter", "None")
        decision = Decision(self.mock_encounter, 99)  # Invalid decision input
        self.assertFalse(decision._valid)
        decision.make_decision()

        # Check that no changes were made to the encounter
        self.assertEqual(self.mock_encounter.food_change, 0)
        self.assertEqual(self.mock_encounter.ammo_change, 0)

    def test_encounter_not_found(self):
        """Test if no matching encounter found leads to _valid being False."""
        self.mock_encounter = MockEncounter("Unknown Encounter", "None")
        decision = Decision(self.mock_encounter, 1)
        self.assertFalse(decision._valid)  # Invalid decision



if __name__ == "__main__":
    unittest.main()