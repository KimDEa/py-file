import time
from prettytable import PrettyTable

class Brew:
    def __init__(self):
        self.menu = [[1.5, 50, 18], [2.5, 30, 18, 50], [3, 30, 20, 60]]
        self.coins = {'quarter': 0.25, 'dime': 0.1, 'nickle': 0.05, 'pennies': 0.01}
        self.supplies = {"water": 300, "coffee": 250, "milk": 200}
        self.coins_detect = False
        self.supplies_detect = False
        self.pot = float(0)
        self.order = int(0)
    
    def coin_detect(self):
        total = float(0)
        while self.coins_detect is False:
            total += input("How many quarters($0.25) you want to insert?: ") * self.coins["quarter"]
            total += input("How many dime($0.1) you want to insert?: ") * self.coins["dime"]
            total += input("How many nickle($0.05) you want to insert?: ") * self.coins["nickle"]
            total += input("How many pennies($0.01) you want to insert?: ") * self.coins["pennies"]
            if total >= self.menu[self.order - 1][0]:
                print(f"Total: ${total:.2f}.")
                print(f"Here's your change: ${total - self.menu[self.order - 1][0]:.2f}.")
                self.pot += self.menu[self.order - 1][0]
                return self.coins_detect is True
            elif total < self.menu[self.order - 1][0]:
                print("Not enough money, please try again.")
                print(f"Here's your change: ${total:.2f}.")
                self.coins_detect = False
                n.machine()
    
    def supply_detect(self):
        if self.menu[self.order - 1][1] <= self.supplies["water"] and self.menu[self.order - 1][2] <= self.supplies["coffee"]:
            self.supplies["water"] -= self.menu[self.order - 1][1]
            self.supplies["coffee"] -= self.menu[self.order - 1][2]
            return self.supplies_detect is True
        elif self.menu[self.order - 1][1] <= self.supplies["water"] and self.menu[self.order - 1][2] <= self.supplies["coffee"] and self.menu[self.order - 1][3] <= self.supplies["milk"]:
            self.supplies["water"] -= self.menu[self.order - 1][1]
            self.supplies["coffee"] -= self.menu[self.order - 1][2]
            self.supplies["milk"] -= self.menu[self.order - 1][3]
            return self.supplies_detect is True
        else:
            print("Sorry, out of supplies.")
            return self.supplies_detect is False
    
    def supply_monitor(self):
        monitor = PrettyTable()
        monitor.title = "Supply Monitor"
        monitor.field_names = ["Items", "Quantity"]
        monitor.add_row(["Water", self.supplies["water"]])
        monitor.add_row(["Coffee bin", self.supplies["coffee"]])
        monitor.add_row(["Milk", self.supplies["milk"]])
        monitor.add_row(["Money", self.pot])
        monitor.align = 'c'
        monitor.float_format = '.2'
        return n.machine()
    
    def machine(self):
        screen = PrettyTable()
        screen.title = "Welcome!"
        screen.field_names = ["Coffee", "Price", "Order number"]
        screen.add_row(["Espresso", self.menu[0][0], 1])
        screen.add_row(["Latte", self.menu[1][0], 2])
        screen.add_row(["Cappuchino", self.menu[2][0], 3])
        screen.add_row(["Supply monitor", '"', 4])
        screen.align = 'c'
        screen.float_format = '.2'
        if n.coins_detect is True:
            if n.supplies_detect is True:
                print("Brewing.")
                time.sleep(1.5)
                print("Brewing..")
                time.sleep(1.5)
                print("Brewing...")
                time.sleep(1.5)
                print("Done!")
                n.machine()
            else:
                n.supplies_detect()
        else:
            n.coins_detect



if __name__ == '__main__':
    n = Brew()
    n.machine()
    