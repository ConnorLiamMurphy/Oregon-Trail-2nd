import random
import PySimpleGUI as sg
from inventoryAndStats import InventoryAndStats


class TradeScenario:
    def __init__(self, offer, cost, offer_description, cost_description):
        self.offer = offer
        self.cost = cost
        self.offer_description = offer_description
        self.cost_description = cost_description

    def __str__(self):
        return f"Offer: {self.offer_description} for {self.cost_description}"

def generate_trade():
    trades = [
        TradeScenario("5 Food", "2 Health", "Offer: 5 units of food", "Cost: 2 units of health"),
        TradeScenario("10 Food", "3 Morale", "Offer: 10 units of food", "Cost: 3 morale"),
        TradeScenario("2 Health", "5 Food", "Offer: 2 units of health", "Cost: 5 units of food"),
        TradeScenario("3 Morale", "4 Food", "Offer: 3 morale", "Cost: 4 units of food"),            TradeScenario("1 Health", "10 Food", "Offer: 1 unit of health", "Cost: 10 units of food"),
         TradeScenario("2 Morale", "5 Health", "Offer: 2 morale", "Cost: 5 units of health"),
        TradeScenario("7 Food", "2 Morale", "Offer: 7 units of food", "Cost: 2 morale"),
        TradeScenario("15 Food", "5 Health", "Offer: 15 units of food", "Cost: 5 units of health"),
        ]
    return random.choice(trades)

def initiate_trade(_inv:InventoryAndStats):

    trade_scenario = generate_trade()
    layout = [
        [sg.Text("A traveler approaches and offers you a trade!", font=('Helvetica', 16))],
        [sg.Text(f"{trade_scenario.offer_description}", font=('Helvetica', 14))],
        [sg.Text(f"{trade_scenario.cost_description}", font=('Helvetica', 14))],
        [sg.Text(
            f"Your current inventory: Food = {_inv.get_food()}, Health = {_inv.get_health()}, Morale = {_inv.get_morale()}",
            font=('Helvetica', 12))],
        [sg.Button("Accept Trade", size=(12, 2), font=('Helvetica', 16)),
         sg.Button("Decline Trade", size=(12, 2), font=('Helvetica', 16))]
    ]

    trade_window = sg.Window("Trade with Traveler", layout, size=(400, 300))

    # Event loop
    while True:
        event, _ = trade_window.read()

        if event == sg.WINDOW_CLOSED or event == "Decline Trade":
            trade_window.close()
            return None  # If declined, no trade happens

        elif event == "Accept Trade":
            # Check if the player has enough inventory for the trade
            if _inv.get_food() >= int(trade_scenario.cost.split(" ")[0]) and \
                    _inv.get_health() >= int(trade_scenario.cost.split(" ")[2]) and \
                    _inv.get_morale() >= int(trade_scenario.cost.split(" ")[4]):

                # Accept the trade, update inventory
                _inv.set_food(_inv.get_food() - int(trade_scenario.cost.split(" ")[0]))
                _inv.set_health(_inv.get_health() - int(trade_scenario.cost.split(" ")[2]))
                _inv.set_morale(_inv.get_morale() - int(trade_scenario.cost.split(" ")[4]))
                print(f"Trade Accepted! You lost {trade_scenario.cost} but gained {trade_scenario.offer}.")

                # Add the offer items to the inventory
                _inv.set_food(_inv.get_food() + int(trade_scenario.offer.split(" ")[0]))
                _inv.set_health(_inv.get_health() + int(trade_scenario.offer.split(" ")[2]))
                _inv.set_morale(_inv.get_morale() + int(trade_scenario.offer.split(" ")[4]))

                trade_window.close()
                return "Trade completed!"  # Return trade result
            else:
                # Not enough inventory for the trade
                sg.popup("You do not have enough resources for this trade!")
                trade_window.close()
                return None