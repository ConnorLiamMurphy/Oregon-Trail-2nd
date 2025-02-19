from parameters import Character


class InventoryAndStats:
    """hold the inventory and player status values"""

    def __init__(self, food: int, ammo: int, clothes: int, parts: int, oxen: int,
                 medicine: int, money: int, morale: int, health: int, char: Character):
        """initialize the inventory values"""
        self._food = food
        self._ammo = ammo
        self._clothes = clothes
        self._parts = parts
        self._oxen = oxen
        self._medicine = medicine
        self._money = money
        self._morale = morale
        self._health = health
        self._status = 'Healthy'
        self._char = char

    def get_food(self):
        """get food value"""
        return self._food

    def get_ammo(self):
        """get ammo value"""
        return self._ammo

    def get_clothes(self):
        """get clothes value"""
        return self._clothes

    def get_parts(self):
        """get parts value"""
        return self._parts

    def get_oxen(self):
        """get oxen value"""
        return self._oxen

    def get_medicine(self):
        """get Medicine value"""
        return self._medicine

    def get_money(self):
        """get money value"""
        return self._money

    def get_morale(self):
        """get morale value"""
        return self._morale

    def get_health(self):
        """get health value"""
        return self._health

    def get_status(self):
        """get health value"""
        return self._status

    def set_food(self, food: int):
        """set food value"""
        self._food = food

    def set_ammo(self, ammo: int):
        """set ammo value"""
        if ammo <= 0:
            self._ammo = 0
        else:
            self._ammo = ammo

    def set_clothes(self, clothes: int):
        """set clothes value"""
        if clothes <= 0:
            self._clothes = 0
        else:
            self._clothes = clothes

    def set_parts(self, parts: int):
        """set parts value"""
        if parts <= 0:
            self._parts = 0
        else:
            self._parts = parts

    def set_oxen(self, oxen: int):
        """set oxen value"""
        if oxen <= 0:
            self._oxen = 0
        else:
            self._oxen = oxen

    def set_medicine(self, medicine: int):
        """set oxen value"""
        if medicine <= 0:
            self._medicine = 0
        else:
            self._medicine = medicine

    def set_money(self, money: int):
        """set money value"""
        if money <= 0:
            self._money = 0
        else:
            self._money = money

    def set_morale(self, morale: int):
        """set morale value"""
        self._morale = morale

    def set_health(self, health: int):
        """set health value"""
        if health > self._char.get_class_health():
            health = self._char.get_class_health()
        self._health = health

    def set_status(self, status: str):
        """set morale value"""
        self._status = status
