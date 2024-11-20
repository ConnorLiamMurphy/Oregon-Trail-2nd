import csv
import random
from inventoryAndStats import InventoryAndStats


class Encounter:
    """randomly chose a encounter and change the inventory values of the player if encountered"""
    _STATS = []

    @staticmethod
    def _load_stats():
        """load encounters from the encounter_stats file and append them to the _STATS list"""
        with open('./encounter_stats', 'r') as f:
            _reader = csv.reader(f)
            for row in _reader:
                Encounter._STATS.append(row)

    def __init__(self, inventory: InventoryAndStats, actions):
        """create a random encounter and assign the values to individual variables"""
        Encounter._load_stats()
        self._encounter = random.choice(Encounter._STATS)
        self._name = self._encounter[0]
        self._food_change = self._encounter[1]
        self._ammo_change = self._encounter[2]
        self._clothes_change = self._encounter[3]
        self._parts_change = self._encounter[4]
        self._medicine_change = self._encounter[5]
        self._oxen_change = self._encounter[6]
        self._money_change = self._encounter[7]
        self._morale_change = self._encounter[8]
        self._health_change = self._encounter[9]
        self._prompt = self._encounter[10]
        self._extra_change = self._encounter[11]
        self._inventory = inventory
        self._actions = actions

    def get_name(self):
        """get the encounter name"""
        if self._prompt == "True":
            split = self._name.split('1')
            _first_half = split[0]
            _second_half = f'1{split[1]}'
            return _first_half, _second_half
        else:
            return self._name

    def get_original_name(self):
        """return the unedited name for encounters with
        inputs so that they read correctly into the
        Decisions class"""
        return self._name

    def get_food_change(self):
        """get the value that the food will change by"""
        return self._food_change

    def set_food_change(self, food_change: int):
        """set the value that the food will change by"""
        self._food_change = food_change

    def get_ammo_change(self):
        """get the value that the ammo will change by"""
        return self._ammo_change

    def set_ammo_change(self, ammo_change: int):
        """set the value that the ammo will change by"""
        self._ammo_change = ammo_change

    def get_clothes_change(self):
        """get the value that the clothes will change by"""
        return self._clothes_change

    def set_clothes_change(self, clothes_change: int):
        """set the value that the clothes will change by"""
        self._clothes_change = clothes_change

    def get_parts_change(self):
        """get the value that the parts will change by"""
        return self._parts_change

    def set_parts_change(self, parts_change: int):
        """set the value that the parts will change by"""
        self._parts_change = parts_change

    def get_medicine_change(self):
        """get the value that the medicine will change by"""
        return self._medicine_change

    def set_medicine_change(self, medicine_change: int):
        """set the value that the medicine will change by"""
        self._medicine_change = medicine_change

    def get_oxen_change(self):
        """get the value that the oxen will change by"""
        return self._oxen_change

    def set_oxen_change(self, oxen_change: int):
        """set the value that the oxen will change by"""
        self._oxen_change = oxen_change

    def get_money_change(self):
        """get the value that the money will change by"""
        return self._money_change

    def set_money_change(self, money_change: int):
        """set the value that the money will change by"""
        self._money_change = money_change

    def get_morale_change(self):
        """get the value that the morale will change by"""
        return self._morale_change

    def set_morale_change(self, morale_change: int):
        """set the value that the morale will change by"""
        self._morale_change = morale_change

    def get_health_change(self):
        """get the value that the health will change by"""
        return self._health_change

    def set_health_change(self, health_change: int):
        """set the value that the health will change by"""
        self._health_change = health_change

    def get_prompt(self):
        """get whether the encounter takes user input"""
        return self._prompt

    def decision(self):
        """change the inventory values based on the current values of the change variables"""
        if self._extra_change == 'None':
            self._inventory.set_food(self._inventory.get_food() + int(self._food_change))
            self._inventory.set_ammo(self._inventory.get_ammo() + int(self._ammo_change))
            self._inventory.set_clothes(self._inventory.get_clothes() + int(self._clothes_change))
            self._inventory.set_parts(self._inventory.get_parts() + int(self._parts_change))
            self._inventory.set_medicine(self._inventory.get_medicine() + int(self._medicine_change))
            self._inventory.set_oxen(self._inventory.get_oxen() + int(self._oxen_change))
            self._inventory.set_money(self._inventory.get_money() + int(self._money_change))
            self._inventory.set_morale(self._inventory.get_morale() + int(self._morale_change))
            self._inventory.set_health(self._inventory.get_health() + int(self._health_change))
        else:
            if self._extra_change == 'Break':
                self._actions.set_travel_speed('Broken')
            if self._extra_change == 'Dysentery':
                self._inventory.set_status('Dysentery')
            self._extra_change = 'None'
            self.decision()
