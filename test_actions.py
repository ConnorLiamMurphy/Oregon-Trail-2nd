import unittest
from random import randint
from inventoryAndStats import InventoryAndStats
from actions import Actions
from encounters import Encounter
from landmarks import Landmark


# Mock InventoryAndStats instance for testing
def get_mock_inventory():
    """Mock InventoryAndStats with basic values for testing"""
    inv = InventoryAndStats()
    inv.set_food(100)  # Mock food amount
    inv.set_health(10)  # Mock health
    inv.set_ammo(10)  # Mock ammo
    inv.set_status('Healthy')  # Mock status
    return inv


# Mock Actions instance for testing
def get_mock_actions(distance=100, inventory=None, travel_speed='Moderate', rations='Standard', date='Mar'):
    """Create and return a mock Actions instance"""
    if inventory is None:
        inventory = get_mock_inventory()  # Use the mock inventory if not provided
    return Actions(distance, inventory, travel_speed, rations, date)


class TestActions(unittest.TestCase):

    def test_initialization(self):
        """Test the initialization of Actions class"""
        inv = get_mock_actions()
        self.assertEqual(inv.get_distance(), 100)  # Check initial distance
        self.assertEqual(inv.get_weather(), 'chilly')  # Check initial weather (March)
        self.assertEqual(inv.get_travel_speed(), 'Moderate')  # Check travel speed
        self.assertEqual(inv.get_rations(), 'Standard')  # Check rations
        self.assertEqual(inv.get_daily_food_loss(), 5)  # Standard rations should consume 5 food per day

    def test_travel(self):
        """Test travel method of Actions class"""
        inv = get_mock_actions()
        initial_distance = inv.get_distance()
        inv.travel()  # Perform a travel action
        self.assertEqual(inv.get_distance(), initial_distance - inv._miles_per_day)  # Distance should decrease

        # Check food consumption after travel
        self.assertEqual(inv.get_inventory().get_food(), 100 - inv._daily_food_loss)  # Food should decrease

    def test_set_encountered(self):
        """Test set_encountered method"""
        inv = get_mock_actions()
        inv.set_encountered(True)
        self.assertTrue(inv._encountered)  # Encountered should be set to True

    def test_hunt(self):
        """Test hunt method"""
        inv = get_mock_actions()
        food_gained, injuries = inv.hunt(ammo_used=2, time_spent=2)  # Hu
