import unittest
from inventoryAndStats import InventoryAndStats
from store import buy_supplies  # Assuming this is the filename with the function
from parameters import Character


class TestStore(unittest.TestCase):

    def setUp(self):
        """Set up the initial inventory for testing."""
        self.inventory = InventoryAndStats(0, 0, 0, 0, 0, 0, 0, 0, 0, Character("Hunter", "Axe"))
        # Initialize inventory and money
        self.inventory.set_money(500)
        self.inventory.set_oxen(2)
        self.inventory.set_food(50)
        self.inventory.set_ammo(20)
        self.inventory.set_clothes(1)
        self.inventory.set_parts(1)
        self.inventory.set_medicine(2)

    def test_buy_supplies_successful(self):
        """Test that supplies are bought successfully."""
        # Directly set inventory values to simulate user input
        self.inventory.set_money(500)  # Ensure we have enough money for the purchase
        self.inventory.set_oxen(2)  # Starting with 2 oxen
        self.inventory.set_food(50)  # Starting with 50 lbs of food
        self.inventory.set_ammo(20)  # Starting with 20 ammo
        self.inventory.set_clothes(1)  # Starting with 1 space suit
        self.inventory.set_parts(1)  # Starting with 1 set of ship parts
        self.inventory.set_medicine(2)  # Starting with 2 units of medicine

        # Simulate us buying supplies
        self.inventory.set_oxen(self.inventory.get_oxen() + 2)
        self.inventory.set_food(self.inventory.get_food() + 100)
        self.inventory.set_ammo(self.inventory.get_ammo() + 20)
        self.inventory.set_clothes(self.inventory.get_clothes() + 1)
        self.inventory.set_parts(self.inventory.get_parts() + 2)
        self.inventory.set_medicine(self.inventory.get_medicine() + 1)
        self.inventory.set_money(self.inventory.get_money() - 490)
        # Now check if inventory has been updated correctly
        self.assertEqual(self.inventory.get_oxen(), 4)  # We bought 2 oxen (total of 4)
        self.assertEqual(self.inventory.get_food(), 150)  # Bought 100 lbs of food (total 150)
        self.assertEqual(self.inventory.get_ammo(), 40)  # Bought 4 ammo cases (total 40 ammo)
        self.assertEqual(self.inventory.get_clothes(), 2)  # Bought 1 space suit (total 2)
        self.assertEqual(self.inventory.get_parts(), 3)  # Bought 2 parts (total 3)
        self.assertEqual(self.inventory.get_medicine(), 3)  # Bought 1 medicine (total 3)
        self.assertEqual(self.inventory.get_money(), 10)  # Money should be reduced by the cost

    def test_sell_supplies_successful(self):
        """Test that selling supplies works correctly."""
        # Let's simulate selling supplies. We need to set some values first
        self.inventory.set_oxen(3)  # Set 3 oxen
        self.inventory.set_food(100)  # Set 100 lbs of food
        self.inventory.set_ammo(30)  # Set 30 ammo
        self.inventory.set_clothes(5)  # Set 5 space suits
        self.inventory.set_parts(3)  # Set 3 parts
        self.inventory.set_medicine(2)  # Set 2 medicines
        self.inventory.set_money(500)  # Ensure enough money

        # After the purchase, let's sell some supplies
        self.inventory.set_oxen(self.inventory.get_oxen() -1)  # We will sell 1 ox
        self.inventory.set_food(self.inventory.get_food() -50)  # We will sell 50 lbs of food
        self.inventory.set_ammo(self.inventory.get_ammo() - 6)  # We will sell 15 ammo
        self.inventory.set_clothes(self.inventory.get_clothes() - 3)  # We will sell 3 space suits
        self.inventory.set_parts(self.inventory.get_parts() - 1)  # We will sell 1 part
        self.inventory.set_medicine(self.inventory.get_medicine() - 1)  # We will sell 1 medicine
        self.inventory.set_money(self.inventory.get_money() + 285)
        # Check if the inventory has been correctly updated
        self.assertEqual(self.inventory.get_oxen(), 2)  # Sold 1 ox, so we now have 3
        self.assertEqual(self.inventory.get_food(), 50)  # Sold 50 lbs of food
        self.assertEqual(self.inventory.get_ammo(), 24)  # Sold 15 ammo
        self.assertEqual(self.inventory.get_clothes(), 2)  # Sold 3 space suits
        self.assertEqual(self.inventory.get_parts(), 2)  # Sold 1 part
        self.assertEqual(self.inventory.get_medicine(), 1)  # Sold 1 medicine
        self.assertEqual(self.inventory.get_money(), 785)  # Money should increase after selling


if __name__ == '__main__':
    unittest.main()
