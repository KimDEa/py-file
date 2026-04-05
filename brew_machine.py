import time

"""Coffee_recipe
espresso
    price = 1.50
    water = 50
    coffee = 18
latte
    price = 2.50
    water = 200
    coffee = 24
    milk = 150
cappuccino
    price = 3
    water = 250
    coffee = 24
    milk = 100"""

class Brew:
    recipe = [[1.5, 50, 18],[2.50, 200, 24, 150],[3, 250, 24, 100]]#espresso, latte, cappuccino / price, water, coffee, milk
    coins = {'quarter': 0.25, 'dime': 0.1, 'nickle': 0.05, 'pennies': 0.01}
    supply = {'water': 300, 'coffee': 100, 'milk': 250}
    coin_detect = 0
    #order_status = 0
    #supply_detect_status = 0
    pot = 0
    pot_temp = 0
    order = int(0)
    
    def supplies(self):
        print("-supply list-")
        print(f"coffee bin - {Brew.supply['coffee']}g")
        print(f"water - {Brew.supply['water']}ml")
        print(f"milk - {Brew.supply['milk']}ml")
        print(f"money - ${Brew.pot:.2f}")
        if Brew.supply['coffee'] == 0:
            print("ran out of coffe bin, please refill it.")
        elif Brew.supply['water'] == 0:
            print("ran out of water, please refill it.")
        elif Brew.supply['milk'] == 0:
            print("ran out of milk, please refill it.")
    
    def supply_detect(self):
        if Brew.order == 1:
            if Brew.supply['water'] >= 50 and Brew.supply['coffee'] >= 18:
                return True
            else:
                return False
        elif Brew.order == 2:
            if Brew.supply['water'] >= 200 and Brew.supply['coffee'] >= 24 and Brew.supply['milk'] >= 150:
                return True
            else:
                return False
        elif Brew.order == 3:
            if Brew.supply['water'] >= 250 and Brew.supply['coffee'] >= 24 and Brew.supply['milk'] >= 100:
                return True
            else:
                return False
    
    def refill(self):
        n.supplies()
        while True:
            print("Welcome to suppliment refill system.")
            print()
            choose_supply = input("Choose suppliment you want to fill : ")
            if choose_supply == 'water':
                volume = int(input("Input volume: (ml) "))
                confirm = input("Are you sure? (y/n) ")
                if confirm == 'y':
                    Brew.supply['water'] += volume
                elif confirm == 'n':
                    continue
            elif choose_supply == 'coffee':
                volume = int(input("Input volume: (g) "))
                confirm = input("Are you sure? (y/n) ")
                if confirm == 'y':
                    Brew.supply['coffee'] += volume
                elif confirm == 'n':
                    continue
            elif choose_supply == 'milk':
                volume = int(input("Input volume: (ml) "))
                confirm = input("Are you sure? (y/n) ")
                if confirm == 'y':
                    Brew.supply['milk'] += volume
                elif confirm == 'n':
                    continue
            elif choose_supply == 'exit':
                n.machine()
            elif choose_supply == 'status':
                n.supplies()
    
    def machine(self):
        Brew.coin_detect = 0
        print("Welcome!")
        Brew.order = int(input("What would you like? 1)Espresso, 2)Latte, 3)Cappuccino, 4)Supply status. : "))
        if Brew.order == 4:
            n.supplies()
            n.machine()
        elif Brew.order == 8888:
            n.refill()
        while Brew.coin_detect == 0:
            total = 0
            total += float(input("How many quarters would you like to insert? : ")) * Brew.coins['quarter']
            total += float(input("How many dimes would you like to insert? : ")) * Brew.coins['dime']
            total += float(input("How many nickles would you like to insert? : ")) * Brew.coins['nickle']
            total += float(input("How many pennies would you like to insert? : ")) * Brew.coins['pennies']
            Brew.pot_temp = total
            if Brew.order == 1 and total >= Brew.recipe[0][0]:
                print(f"Your change: ${total - Brew.recipe[0][0]:.2f}")
                Brew.pot += Brew.recipe[0][0]
                Brew.coin_detect = 1
            elif Brew.order == 1 and total < Brew.recipe[0][0]:
                print(f"Total: ${Brew.pot_temp:.2f} / Price: $1.50")
                print("Not enough of coin, try again.")
                Brew.pot_temp = 0
                print("Coins are ejected.")
                n.machine()
            elif Brew.order == 2 and total >= Brew.recipe[1][0]:
                print(f"Your change: ${total - Brew.recipe[1][0]:.2f}")
                Brew.pot += Brew.recipe[1][0]
                Brew.coin_detect = 1
            elif Brew.order == 2 and total < Brew.recipe[1][0]:
                print(f"Total: ${Brew.pot_temp:.2f} / Price: $2.50")
                print("Not enough of coin, try again.")
                Brew.pot_temp = 0
                print("Coins are ejected.")
                n.machine()
            elif Brew.order == 3 and total >= Brew.recipe[2][0]:
                print(f"Your change: ${total - Brew.recipe[2][0]:.2f}")
                Brew.pot += Brew.recipe[2][0]
                Brew.coin_detect = 1
            elif Brew.order == 3 and total < Brew.recipe[2][0]:
                print(f"Total: ${Brew.pot_temp:.2f} / Price: $3")
                print("Not enough of coin, try again.")
                Brew.pot_temp = 0
                print("Coins are ejected.")
                n.machine()
        if Brew.order == 1 and n.supply_detect():
            #Brew.pot += Brew.pot_temp
            Brew.supply['water'] -= Brew.recipe[0][1]
            Brew.supply['coffee'] -= Brew.recipe[0][2]
            print("Brewing.")
            time.sleep(1.5)
            print("Brewing..")
            time.sleep(1.5)
            print("Brewing...")
            time.sleep(1.5)
            print("Done!")
            n.machine()
        elif Brew.order == 1 and not n.supply_detect():
            print("Sorry we ran out of supplies.")
            print(f"Your change: ${Brew.recipe[0][0]:.2f}")
            print("Coins are ejected.")
            Brew.pot -= Brew.recipe[0][0]
            n.machine()
        if Brew.order == 2 and n.supply_detect():
            #Brew.pot += Brew.pot_temp
            Brew.supply['water'] -= Brew.recipe[1][1]
            Brew.supply['coffee'] -= Brew.recipe[1][2]
            Brew.supply['milk'] -= Brew.recipe[1][3]
            print("Brewing.")
            time.sleep(1.5)
            print("Brewing..")
            time.sleep(1.5)
            print("Brewing...")
            time.sleep(1.5)
            print("Done!")
            n.machine()
        elif Brew.order == 2 and not n.supply_detect():
            print("Sorry we ran out of supplies.")
            print(f"Your change: ${Brew.recipe[1][0]:.2f}")
            print("Coins are ejected.")
            Brew.pot -= Brew.recipe[1][0]
            n.machine()
        if Brew.order == 3 and n.supply_detect():
            #Brew.pot += Brew.pot_temp
            Brew.supply['water'] -= Brew.recipe[2][1]
            Brew.supply['coffee'] -= Brew.recipe[2][2]
            Brew.supply['milk'] -= Brew.recipe[2][3]
            print("Brewing.")
            time.sleep(1.5)
            print("Brewing..")
            time.sleep(1.5)
            print("Brewing...")
            time.sleep(1.5)
            print("Done!")
            n.machine()
        elif Brew.order == 3 and not n.supply_detect():
            print("Sorry we ran out of supplies.")
            print(f"Your change: ${Brew.recipe[2][0]:.2f}")
            print("Coins are ejected.")
            Brew.pot -= Brew.recipe[2][0]
            n.machine()

if __name__ == "__main__":
    n = Brew()
    n.machine()
