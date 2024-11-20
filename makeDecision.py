from encounters import Encounter
import csv


class Decision:
    """change values of a given encounter instance based on user input"""
    _DECISIONS = []

    @staticmethod
    def _load_decisions():
        """load decisions from the decisions file and append them to the _DECISIONS list"""
        with open('./decisions', 'r') as f:
            _reader = csv.reader(f)
            for row in _reader:
                Decision._DECISIONS.append(row)

    def __init__(self, encounter: Encounter, kb_input: int):
        """create a decision with the changes to the encounter passed in based on the input given"""
        Decision._load_decisions()
        self._kb_input = kb_input
        self._encounter = encounter
        self._valid = True
        self._changes = ""
        self._diff_food = 0
        self._diff_ammo = 0
        self._diff_clothes = 0
        self._diff_parts = 0
        self._diff_medicine = 0
        self._diff_oxen = 0
        self._diff_money = 0
        self._diff_morale = 0
        self._diff_health = 0

        for i in Decision._DECISIONS:
            if i[0] == self._encounter.get_original_name() and i[1] == kb_input:
                self._changes = i
        if not self._changes:
            self._valid = False
        else:
            self._diff_food = self._changes[2]
            self._diff_ammo = self._changes[3]
            self._diff_clothes = self._changes[4]
            self._diff_parts = self._changes[5]
            self._diff_medicine = self._changes[6]
            self._diff_oxen = self._changes[7]
            self._diff_money = self._changes[8]
            self._diff_morale = self._changes[9]
            self._diff_health = self._changes[10]

    def make_decision(self):
        """change the values of the encounter then call the encounters method to finalize the encounter"""
        if self._valid:
            self._encounter.set_food_change(
                int(self._encounter.get_food_change()) + int(self._diff_food))
            self._encounter.set_ammo_change(
                int(self._encounter.get_ammo_change()) + int(self._diff_ammo))
            self._encounter.set_clothes_change(
                int(self._encounter.get_clothes_change()) + int(self._diff_clothes))
            self._encounter.set_parts_change(
                int(self._encounter.get_parts_change()) + int(self._diff_parts))
            self._encounter.set_medicine_change(
                int(self._encounter.get_medicine_change()) + int(self._diff_medicine))
            self._encounter.set_oxen_change(
                int(self._encounter.get_oxen_change()) + int(self._diff_oxen))
            self._encounter.set_money_change(
                int(self._encounter.get_money_change()) + int(self._diff_money))
            self._encounter.set_morale_change(
                int(self._encounter.get_morale_change()) + int(self._diff_morale))
            self._encounter.set_health_change(
                int(self._encounter.get_health_change()) + int(self._diff_health))
            self._encounter.decision()
        return self._valid
