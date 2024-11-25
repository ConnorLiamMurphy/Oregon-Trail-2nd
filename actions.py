import random
from encounters import Encounter
from landmarks import Landmark
from inventoryAndStats import InventoryAndStats


class Actions:
    """any functions that are necessary to perform an action will be run from here"""

    def __init__(self, distance: int, inventory: InventoryAndStats, travel_speed: str, rations: str, date: str):
        """initialize any necessary variables to do any actions"""
        self._distance = distance
        self._encountered = False
        self._inventory = inventory
        self._travel_speed = travel_speed
        self._rations = rations
        self._date = date
        # Set food consumption based on rations
        self._food_consumption = {
            'Light': 3,
            'Standard': 5,
            'Heavy': 8
        }
        self._speed = {
            'No Oxen': 1,
            'Broken': 1,
            'Slow': 5,
            'Moderate': 10,
            'Quick': 15
        }
        self._exact_leave_date = {
            'Mar': '03/01',
            'Apr': '04/01',
            'May': '05/01',
            'Jun': '06/01'
        }
        self._init_weather = {
            'Mar': 'chilly',
            'Apr': 'temperate',
            'May': 'warm',
            'Jun': 'warm'
        }
        self._daily_food_loss = self._food_consumption[self._rations]
        self._miles_per_day = self._speed[self._travel_speed]
        self._current_date = self._exact_leave_date[self._date]
        self._weather = self._init_weather[self._date]
        self._landmark = Landmark()

    def get_inventory(self):
        """get the current games inventory"""
        return self._inventory

    def get_distance(self):
        """get the distance from the final destination"""
        return self._distance

    def set_encountered(self, val: bool):
        """set whether you just encountered something"""
        self._encountered = val

    def set_rations(self, rations: str):
        """set your daily rations"""
        self._rations = rations
        self._daily_food_loss = self._food_consumption[rations]

    def set_travel_speed(self, travel_speed: str):
        """set how far you travel in a day"""
        self._travel_speed = travel_speed
        self._miles_per_day = self._speed[self._travel_speed]

    def get_rations(self):
        """get your daily rations"""
        return self._rations

    def get_daily_food_loss(self):
        """return the numeric amount of food you consume per day"""
        return self._daily_food_loss

    def get_travel_speed(self):
        """get how far you travel in a day"""
        return self._travel_speed

    def get_date(self):
        """get the current date"""
        return self._current_date

    def get_weather(self):
        """get the weather"""
        return self._weather

    def travel(self):
        """decrease distance by your travel speed and food by your ration amount
        then return either your distance, encounter or landmark."""
        self._distance -= self._miles_per_day
        self.increment_date()
        self._inventory.set_food(self._inventory.get_food() - self._daily_food_loss)
        if self._inventory.get_status() == 'Dysentery':
            self._inventory.set_health(self._inventory.get_health() - 1)
        if self._landmark.get_landmark(self._distance, self._miles_per_day):
            return self.get_location()
        if not self._encountered:
            if random.randint(1, 100) <= 5:
                _new_enc = Encounter(self._inventory, self)
                return _new_enc
        return self._distance

    def get_location(self):
        """get your current location's name"""
        _place, _add = self._landmark.get_landmark(self._distance, self._miles_per_day)
        self._distance += _add
        return _place

    def increment_date(self):
        """change the date for the day"""
        _num_of_days = {
            '01': '31',
            '02': '28',
            '03': '31',
            '04': '30',
            '05': '31',
            '06': '30',
            '07': '31',
            '08': '31',
            '09': '30',
            '10': '31',
            '11': '30',
            '12': '31',
        }
        _month_weather = {
            '01': ['Cold', 'Chilly'],
            '02': ['Cold', 'Chilly'],
            '03': ['Chilly', 'Temperate'],
            '04': ['Chilly', 'Temperate', 'Warm'],
            '05': ['Chilly', 'Temperate', 'Warm'],
            '06': ['Temperate', 'Warm', 'Hot'],
            '07': ['Warm', 'Hot'],
            '08': ['Warm', 'Hot'],
            '09': ['Temperate', 'Warm'],
            '10': ['Chilly', 'Temperate'],
            '11': ['Chilly', 'Temperate'],
            '12': ['Cold', 'Chilly', 'Temperate'],
        }
        if self._current_date[3] == '0':
            if self._current_date[4] == '9':
                self._current_date = self._current_date[0:3] + str(int(self._current_date[4]) + 1)
            else:
                self._current_date = self._current_date[0:4] + str(int(self._current_date[4]) + 1)
        else:
            if _num_of_days[self._current_date[0:2]] == self._current_date[3:5]:
                if self._current_date[0] == '0':
                    if self._current_date[1] == '9':
                        self._current_date = str(int(self._current_date[1]) + 1) + '/01'
                    else:
                        self._current_date = self._current_date[0] + str(int(self._current_date[1]) + 1) + '/01'
                else:
                    if self._current_date[0:2] == '12':
                        self._current_date = '01/01'
                    else:
                        self._current_date = str(int(self._current_date[1]) + 1) + '/01'
            else:
                self._current_date = self._current_date[0:3] + str(int(self._current_date[3:5]) + 1)

        self._weather = random.choice(_month_weather[self._current_date[0:2]])
