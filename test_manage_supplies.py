import unittest
from actions import Actions
from inventoryAndStats import InventoryAndStats
from parameters import Character
from manage_supplies import manage_supplies


class TestManageSupplies(unittest.TestCase):

    def set_up(self):
        # Create actual instances of the classes
        self.character = Character("Hunter", "Axe")
        self.inventory = InventoryAndStats(0, 0, 0, 0, 0, 0, 0, 0, 0, self.character)
        self.actions = Actions(0, self.inventory, "Moderate", "Standard", 'Mar', self.character)

    # Set initial values for the inventory and actions for testing
        self.inventory.set_parts(3)  # Enough parts to fix the ship
        self.inventory.set_medicine(2)  # 2 medicines available
        self.inventory.set_health(50)  # Health is 50
        self.inventory.set_status('Healthy')  # Status is healthy
        self.inventory.set_oxen(2)  # 2 oxen available

    def test_use_medicine_success(self):
        # Simulate using the 'Use Medicine' button when health is not full
        self.inventory.set_health(50)  # Set health to a value lower than the max
        self.inventory.set_medicine(2)  # Simulate having 2 medicines

        # Simulate calling the 'Use Medicine' event
        manage_supplies(self.actions, self.inventory, self.character)

        # Check that health is updated and medicine count is reduced
        self.assertEqual(self.inventory.get_health(), 52)
        self.assertEqual(self.inventory.get_medicine(), 1)
        self.assertEqual(self.inventory.get_status(), 'Healthy')

    def test_use_medicine_no_medicine(self):
        # Simulate using the 'Use Medicine' button when no medicine is left
        self.inventory.set_health(50)
        self.inventory.set_medicine(0)  # No medicine left

        # Simulate calling the 'Use Medicine' event
        manage_supplies(self.actions, self.inventory, self.character)

        # Health should remain the same as no medicine was used
        self.assertEqual(self.inventory.get_health(), 50)
        self.assertEqual(self.inventory.get_medicine(), 0)
        self.assertEqual(self.inventory.get_status(), 'Healthy')

    def test_fix_ship_success(self):
        # Simulate clicking the 'Fix Ship' button with enough parts
        self.inventory.set_parts(3)  # Enough parts to fix the ship

        # Simulate calling the 'Fix Ship' event
        manage_supplies(self.actions, self.inventory, self.character)

        # Check that travel speed was updated and parts count reduced
        self.assertEqual(self.actions.get_travel_speed(), 'Moderate')
        self.assertEqual(self.inventory.get_parts(), 2)

    def test_fix_ship_no_parts(self):
        # Simulate clicking the 'Fix Ship' button with no parts
        self.inventory.set_parts(0)  # No parts to fix the ship

        # Simulate calling the 'Fix Ship' event
        manage_supplies(self.actions, self.inventory, self.character)

        # The parts should still be 0, and the ship should not be fixed
        self.assertEqual(self.inventory.get_parts(), 0)
        self.assertEqual(self.actions.get_travel_speed(), 'Moderate')

    def test_confirm_changes(self):
        # Simulate the user confirming changes
        self.actions.set_travel_speed('Quick')
        self.actions.set_rations('Heavy')

        # Simulate calling the 'Confirm' event
        manage_supplies(self.actions, self.inventory, self.character)

        # The travel speed and rations should be updated
        self.assertEqual(self.actions.get_travel_speed(), 'Quick')
        self.assertEqual(self.actions.get_rations(), 'Heavy')

    def test_no_oxen_layout(self):
        # Set oxen to 0 to simulate the no oxen layout scenario
        self.inventory.set_oxen(0)

        # Simulate calling the manage_supplies function with no oxen
        manage_supplies(self.actions, self.inventory, self.character)

        # Check if the layout handles no oxen case correctly
        self.assertEqual(self.inventory.get_oxen(), 0)

    def test_travel_speed_layout(self):
        # Change the travel speed and simulate the layout change
        self.actions.set_travel_speed('Broken')

        # Simulate calling the manage_supplies function with 'Broken' travel speed
        manage_supplies(self.actions, self.inventory, self.character)

        # Check that the travel speed is set to 'Broken' as expected
        self.assertEqual(self.actions.get_travel_speed(), 'Broken')


if __name__ == '__main__':
    unittest.main()
