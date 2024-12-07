import random
import PySimpleGUI as sg
from inventoryAndStats import InventoryAndStats


class TradeScenario:
    """create the trade scenario as an object."""
    def __init__(self, offer, cost, offer_description, cost_description):
        """create a Trade Scenario and
        assign the values to individual variables"""
        self._offer = offer
        self._cost = cost
        self._offer_description = offer_description
        self._cost_description = cost_description

    def get_offer(self):
        """get offer"""
        return self._offer

    def get_cost(self):
        """get cost"""
        return self._cost

    def get_offer_description(self):
        """get offer description"""
        return self._offer_description

    def get_cost_description(self):
        """get cost description"""
        return self._cost_description

    def __str__(self):
        return f"Offer: {self._offer_description} for {self._cost_description}"


def generate_trade():
    """house the possible trades and then return that trade."""
    trades = [
        TradeScenario("5 Food", "6 Weapon energy",
                      "Offer: 5 units of food", "Cost: 6 units of Weapon energy"),
        TradeScenario("10 Food", "1 Space Suit",
                      "Offer: 10 units of food", "Cost: 1 Space Suit"),
        TradeScenario("1 Engine", "85 Food",
                      "Offer: 1 engine", "Cost: 85 units of food"),
        TradeScenario("1 Medicine", "5 Food",
                      "Offer: 1 case of medicine", "Cost: 5 units of food"),
        TradeScenario("1 ship part", "35 Dollars",
                      "Offer: 1 ship part", "Cost: 35 dollars"),
        TradeScenario("1 Space Suit", "1 Medicine",
                      "Offer: 1 Space Suit", "Cost: 1 case of medicine"),
        TradeScenario("100 Weapon energy", "1 Engine",
                      "Offer: 100 units of Weapon energy", "Cost: 1 engine"),
        TradeScenario("30 Dollars", "30 Food",
                      "Offer: 30 Dollars", "Cost: 30 units of food"),
    ]
    return random.choice(trades)


def initiate_trade(_inv: InventoryAndStats):
    """Send the trade scenario to the GUI"""
    trade_scenario = generate_trade()
    layout = [
        [sg.Text("A traveler approaches and offers you a trade!", font=('Helvetica', 16))],
        [sg.Text(f"{trade_scenario.get_offer_description()}", font=('Helvetica', 14))],
        [sg.Text(f"{trade_scenario.get_cost_description()}", font=('Helvetica', 14))],
        [sg.Button("Accept Trade", size=(12, 2), font=('Helvetica', 16)),
         sg.Button("Decline Trade", size=(12, 2), font=('Helvetica', 16))]
    ]

    trade_window = sg.Window("Trade with Traveler", layout, size=(500, 300))

    # Event loop
    while True:
        event, _ = trade_window.read()

        if event == sg.WINDOW_CLOSED or event == "Decline Trade":
            trade_window.close()
            return None  # If declined, no trade happens

        elif event == "Accept Trade":
            # Check if the player has enough inventory for the trade
            if trade_scenario.get_cost().split(" ")[1] == 'Food':
                if _inv.get_food() >= int(trade_scenario.get_cost().split(" ")[0]):
                    # Accept the trade, update inventory
                    _inv.set_food(_inv.get_food() - int(trade_scenario.get_cost().split(" ")[0]))
                else:
                    # Not enough inventory for the trade
                    sg.popup("You do not have enough resources for this trade!")
                    trade_window.close()
                    return None
            elif trade_scenario.get_cost().split(" ")[1] == 'Weapon':
                if _inv.get_ammo() >= int(trade_scenario.get_cost().split(" ")[0]):
                    # Accept the trade, update inventory
                    _inv.set_ammo(_inv.get_ammo() - int(trade_scenario.get_cost().split(" ")[0]))
                else:
                    # Not enough inventory for the trade
                    sg.popup("You do not have enough resources for this trade!")
                    trade_window.close()
                    return None
            elif trade_scenario.get_cost().split(" ")[1] == 'Space':
                if _inv.get_clothes() >= int(trade_scenario.get_cost().split(" ")[0]):
                    # Accept the trade, update inventory
                    _inv.set_clothes(_inv.get_clothes() - int(trade_scenario.get_cost().split(" ")[0]))
                else:
                    # Not enough inventory for the trade
                    sg.popup("You do not have enough resources for this trade!")
                    trade_window.close()
                    return None
            elif trade_scenario.get_cost().split(" ")[1] == 'Ship':
                if _inv.get_parts() >= int(trade_scenario.get_cost().split(" ")[0]):
                    # Accept the trade, update inventory
                    _inv.set_parts(_inv.get_parts() - int(trade_scenario.get_cost().split(" ")[0]))
                else:
                    # Not enough inventory for the trade
                    sg.popup("You do not have enough resources for this trade!")
                    trade_window.close()
                    return None
            elif trade_scenario.get_cost().split(" ")[1] == 'Engine':
                if _inv.get_oxen() >= int(trade_scenario.get_cost().split(" ")[0]):
                    # Accept the trade, update inventory
                    _inv.set_oxen(_inv.get_oxen() - int(trade_scenario.get_cost().split(" ")[0]))
                else:
                    # Not enough inventory for the trade
                    sg.popup("You do not have enough resources for this trade!")
                    trade_window.close()
                    return None
            elif trade_scenario.get_cost().split(" ")[1] == 'Medicine':
                if _inv.get_medicine() >= int(trade_scenario.get_cost().split(" ")[0]):
                    # Accept the trade, update inventory
                    _inv.set_medicine(_inv.get_medicine() - int(trade_scenario.get_cost().split(" ")[0]))
                else:
                    # Not enough inventory for the trade
                    sg.popup("You do not have enough resources for this trade!")
                    trade_window.close()
                    return None
            elif trade_scenario.get_cost().split(" ")[1] == 'Dollars':
                if _inv.get_money() >= int(trade_scenario.get_cost().split(" ")[0]):
                    # Accept the trade, update inventory
                    _inv.set_money(_inv.get_money() - int(trade_scenario.get_cost().split(" ")[0]))
                else:
                    # Not enough inventory for the trade
                    sg.popup("You do not have enough resources for this trade!")
                    trade_window.close()
                    return None
            if trade_scenario.get_offer().split(" ")[1] == 'Dollars':
                _inv.set_money(_inv.get_money() + int(trade_scenario.get_offer().split(" ")[0]))
            if trade_scenario.get_offer().split(" ")[1] == 'Food':
                _inv.set_food(_inv.get_food() + int(trade_scenario.get_offer().split(" ")[0]))
            if trade_scenario.get_offer().split(" ")[1] == 'Ship':
                _inv.set_parts(_inv.get_parts() + int(trade_scenario.get_offer().split(" ")[0]))
            if trade_scenario.get_offer().split(" ")[1] == 'Engine':
                _inv.set_oxen(_inv.get_oxen() + int(trade_scenario.get_offer().split(" ")[0]))
            if trade_scenario.get_offer().split(" ")[1] == 'Weapon':
                _inv.set_ammo(_inv.get_ammo() + int(trade_scenario.get_offer().split(" ")[0]))
            if trade_scenario.get_offer().split(" ")[1] == 'Space':
                _inv.set_clothes(_inv.get_clothes() + int(trade_scenario.get_offer().split(" ")[0]))
            if trade_scenario.get_offer().split(" ")[1] == 'Medicine':
                _inv.set_medicine(_inv.get_medicine() + int(trade_scenario.get_offer().split(" ")[0]))
            sg.popup(f"Trade Accepted! You lost {trade_scenario.get_cost()} "
                     f"but gained {trade_scenario.get_offer()}.")
            trade_window.close()
            return "Trade completed!"  # Return trade result
