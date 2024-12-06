import unittest
from parameters import Character


class TestCharacter(unittest.TestCase):

    def test_initialization(self):
        """Test if the character is initialized correctly based on class and weapon."""
        char = Character("Alien Hunter", "Laser Gun")
        self.assertEqual(char.get_weapon(), "Laser Gun")
        self.assertEqual(char.get_class_food(), 15)
        self.assertEqual(char.get_class_money(), 700)
        self.assertEqual(char.get_class_morale(), 5)
        self.assertEqual(char.get_class_health(), 15)

    def test_assign_money(self):
        """Test the assign_money method."""
        char = Character("Space Trader", "Plasma Rifle")
        self.assertEqual(char.assign_money(), 1000)

        char = Character("Alien Hunter", "Plasma Rifle")
        self.assertEqual(char.assign_money(), 700)

        char = Character("Astro Explorer", "Laser Gun")
        self.assertEqual(char.assign_money(), 850)

        # Test with an unknown class (should default to 700)
        char = Character("Unknown Class", "Laser Gun")
        self.assertEqual(char.assign_money(), 700)

    def test_assign_food(self):
        """Test the assign_food method."""
        char = Character("Space Trader", "Plasma Rifle")
        self.assertEqual(char.assign_food(), 10)

        char = Character("Alien Hunter", "Plasma Rifle")
        self.assertEqual(char.assign_food(), 15)

        char = Character("Astro Explorer", "Laser Gun")
        self.assertEqual(char.assign_food(), 5)

        # Test with an unknown class (should default to 10)
        char = Character("Unknown Class", "Laser Gun")
        self.assertEqual(char.assign_food(), 10)

    def test_assign_health(self):
        """Test the assign_health method."""
        char = Character("Space Trader", "Plasma Rifle")
        self.assertEqual(char.assign_health(), 12)

        char = Character("Alien Hunter", "Plasma Rifle")
        self.assertEqual(char.assign_health(), 15)

        char = Character("Astro Explorer", "Laser Gun")
        self.assertEqual(char.assign_health(), 10)

        # Test with an unknown class (should default to 10)
        char = Character("Unknown Class", "Laser Gun")
        self.assertEqual(char.assign_health(), 10)

    def test_assign_morale(self):
        """Test the assign_morale method."""
        char = Character("Space Trader", "Plasma Rifle")
        self.assertEqual(char.assign_morale(), 8)

        char = Character("Alien Hunter", "Plasma Rifle")
        self.assertEqual(char.assign_morale(), 5)

        char = Character("Astro Explorer", "Laser Gun")
        self.assertEqual(char.assign_morale(), 10)

        # Test with an unknown class (should default to 5)
        char = Character("Unknown Class", "Laser Gun")
        self.assertEqual(char.assign_morale(), 5)

    def test_get_inventory(self):
        """Test the get_inventory method."""
        char = Character("Astro Explorer", "Laser Gun")
        inventory = char.get_inventory()
        self.assertEqual(inventory['Food'], 5)
        self.assertEqual(inventory['Health'], 10)
        self.assertEqual(inventory['Morale'], 10)
        self.assertEqual(inventory['Money'], 850)

    def test_update_inventory(self):
        """Test the update_inventory method."""
        char = Character("Alien Hunter", "Laser Gun")

        # Update food, health, and morale
        char.update_inventory(food_change=5, health_change=-3, morale_change=2)

        self.assertEqual(char.get_class_food(), 20)
        self.assertEqual(char.get_class_health(), 12)
        self.assertEqual(char.get_class_morale(), 7)

        # Update with no changes
        char.update_inventory()

        self.assertEqual(char.get_class_food(), 20)
        self.assertEqual(char.get_class_health(), 12)
        self.assertEqual(char.get_class_morale(), 7)

    def test_get_class_methods(self):
        """Test the getter methods for class attributes."""
        char = Character("Alien Hunter", "Laser Gun")

        self.assertEqual(char.get_class_food(), 15)
        self.assertEqual(char.get_class_money(), 700)
        self.assertEqual(char.get_class_morale(), 5)
        self.assertEqual(char.get_class_health(), 15)

    def test_get_weapon(self):
        """Test the get_weapon method."""
        char = Character("Astro Explorer", "Plasma Rifle")
        self.assertEqual(char.get_weapon(), "Plasma Rifle")


if __name__ == "__main__":
    unittest.main()
