#Coffee Machine.

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
    coffee = 100 #grams
    water = 300 #milliliters
    milk = 200 #milliliters
    penny = 0.01
    nickle = 0.05
    dime = 0.10
    quarter = 0.25
    money_jar = 0
    recipe = [[1.50, 50, 18], [2.50, 200, 24, 150], [3, 250, 24, 100]]

    def __init__(self):
        self.money_jar_temp = 0
        self.order_status = 1
        self.coin_status = 1
        self.order = None

    def info(self):
        print("-Suppliment Status-")
        print(f" Coffee - {Brew.coffee}")
        print(f" Water - {Brew.water}")
        print(f" Milk - {Brew.milk}")
        print(f" Deposit - ${Brew.money_jar:.2f}")
    
    def supplies(self):
        water = Brew.water
        coffee = Brew.coffee
        milk = Brew.milk
        recipe = Brew.recipe
        if self.order == 'a':
            if water < recipe[0][1]:
                print("Sorry there is not enough water.")
                return False
            elif coffee < recipe[0][2]:
                print("Sorry there is not enough coffee bin")
                return (print(), False)
            elif water >= recipe[0][1] or coffee >= recipe[0][2]:
                return True
        elif self.order == 'b':
            if water < recipe[1][1]:
                print("Sorry there is not enough water.")
                return (print(), False)
            elif coffee < recipe[1][2]:
                print("Sorry there is not enough coffee bin.")
                return (print(), False)
            elif milk < recipe[1][3]:
                print("Sorry there is not enough milk.")
                return (print(), False)
            elif water >= recipe[1][1] or coffee >= recipe[1][2] or milk >= recipe[1][3]:
                return True
        elif self.order == 'c':
            if water < recipe[2][1]:
                print("Sorry there is not enough water.")
                return (print(), False)
            elif coffee < recipe[2][2]:
                print("Sorry there is not enough coffee bin.")
                return (print(), False)
            elif milk < recipe[2][3]:
                print("Sorry there is not enough milk.")
                return (print(), False)
            elif water >= recipe[2][1] or coffee >= recipe[2][2] or milk >= recipe[2][3]:
                return True
        else:
            return None
    
    def fill_it(self):
        what = input("What would you want to fill it? (w)-water, (c)-coffee, (m)-milk. : ")
        how_much = int(input("How much would you want to fill it? : "))
        if what == 'w':
            Brew.water += how_much
            return n.info()
        elif what == 'c':
            Brew.coffee += how_much
            return n.info()
        elif what == 'm':
            Brew.milk += how_much
            return n.info()

    def coffee_machine(self):
        #recipe = [[1.50, 50, 18], [2.50, 200, 24, 150], [3, 250, 24, 100]]
        recipe = Brew.recipe
        self.coin_status = 1
        print("(a)Espresso - $1.50, (b)Latte - $2.50, (c)Cappuccino - $3", sep= '\n')
        self.order = input("What would you like? ('a'(espresso), 'b'(latte), 'c'(cappuccino), 'd'(report)), 'e'(fill supplies): ")
        if self.order == 'd':
            n.info()
            n.coffee_machine()
        elif self.order == 'e':
            n.fill_it()
            n.coffee_machine()
        elif self.order == 'off':
            time.sleep(3)
            return print("Machine off.")
        else:
            while self.order_status:
                if self.coin_status:
                    total = self.money_jar_temp
                    print("Please insert coins")
                    total += int(input("How many quarters($0.25)?: ")) * Brew.quarter
                    print(f"total - ${total:.2f}")
                    total += int(input("How many dimes($0.10)?: ")) * Brew.dime
                    print(f"total - ${total:.2f}")
                    total += int(input("How many nickles($0.05)?: ")) * Brew.nickle
                    print(f"total - ${total:.2f}")
                    total += int(input("How many pennies($0.01)?: ")) * Brew.penny
                    print(f"total - ${total:.2f}")
                    self.money_jar_temp += total
                    self.coin_status = 0
                elif not self.coin_status:
                    if self.order == 'a':
                        if self.money_jar_temp > recipe[0][0]:
                            change = total - recipe[0][0]
                            print(f"Here is ${change:.2f} in change.")
                            Brew.money_jar += recipe[0][0]
                            if n.supplies():
                                print("Brewing.")
                                time.sleep(1.5)
                                print("Brewing..")
                                time.sleep(1.5)
                                print("Brewing...")
                                time.sleep(1.5)
                                print("Your drink is dispensed.")
                                Brew.coffee -= recipe[0][2]
                                Brew.water -= recipe[0][1]
                                self.money_jar_temp = 0
                                n.coffee_machine()
                            elif not n.supplies():
                                #print("Not enough of supplies to make coffee, out of order.")
                                print(f"Here's your change: ${total - change}.")
                                Brew.money_jar -= recipe[0][0]
                                n.info()
                                n.coffee_machine()
                        elif self.money_jar_temp < recipe[0][0]:
                            print(f"Sorry that's not enough money, Money refunded - ${self.money_jar_temp:.2f}")
                            n.coffee_machine()
                        elif self.money_jar_temp == recipe[0][0]:
                            if not n.supplies():
                                #print("Not enough of supplies to make coffee, out of order.")
                                print(f"Here's your change: ${recipe[0][0]}.")
                                #Brew.money_jar -= recipe[0][0]
                                n.info()
                                n.coffee_machine()
                            elif n.supplies():
                                print("Brewing.")
                                time.sleep(1.5)
                                print("Brewing..")
                                time.sleep(1.5)
                                print("Brewing...")
                                time.sleep(1.5)
                                print("Your drink is dispensed.")
                                Brew.coffee -= recipe[0][2]
                                Brew.water -= recipe[0][1]
                                Brew.money_jar += recipe[0][0]
                                self.money_jar_temp = 0
                                n.coffee_machine()
                    elif self.order == 'b':
                        if self.money_jar_temp > recipe[1][0]:
                            change = total - recipe[1][0]
                            print(f"Here is ${change:.2f} in change.")
                            Brew.money_jar += recipe[1][0]
                            if n.supplies():
                                print("Brewing.")
                                time.sleep(1.5)
                                print("Brewing..")
                                time.sleep(1.5)
                                print("Brewing...")
                                time.sleep(1.5)
                                print("Your drink is dispensed.")
                                Brew.water -= recipe[1][1]
                                Brew.coffee -= recipe[1][2]
                                Brew.milk -= recipe[1][3]
                                self.money_jar_temp = 0
                                n.coffee_machine()
                            elif not n.supplies():
                                #print("Not enough of supplies to make coffee, out of order.")
                                print(f"Here's your change: ${total - change}.")
                                Brew.money_jar -= recipe[1][0]
                                n.info()
                                n.coffee_machine()
                        elif self.money_jar_temp < recipe[1][0]:
                            print(f"Sorry that's not enough money, Money refunded - ${self.money_jar_temp:.2f}")
                            n.coffee_machine()
                        elif self.money_jar_temp == recipe[1][0]:
                            if not n.supplies():
                                #print("Not enough of supplies to make coffee, out of order.")
                                print(f"Here's your change: ${recipe[1][0]}.")
                                #Brew.money_jar -= recipe[1][0]
                                n.info()
                                n.coffee_machine()
                            elif n.supplies():
                                print("Brewing.")
                                time.sleep(1.5)
                                print("Brewing..")
                                time.sleep(1.5)
                                print("Brewing...")
                                time.sleep(1.5)
                                print("Your drink is dispensed.")
                                Brew.water -= recipe[1][1]
                                Brew.coffee -= recipe[1][2]
                                Brew.milk -= recipe[1][3]
                                Brew.money_jar += recipe[1][0]
                                self.money_jar_temp = 0
                                n.coffee_machine()
                    elif self.order == 'c':
                        if self.money_jar_temp > recipe[2][0]:
                            change = total - recipe[2][0]
                            print(f"Here is ${change:.2f} in change.")
                            Brew.money_jar += recipe[2][0]
                            if n.supplies():
                                print("Brewing.")
                                time.sleep(1.5)
                                print("Brewing..")
                                time.sleep(1.5)
                                print("Brewing...")
                                time.sleep(1.5)
                                print("Your drink is dispensed.")
                                Brew.water -= recipe[2][1]
                                Brew.coffee -= recipe[2][2]
                                Brew.milk -= recipe[2][3]
                                self.money_jar_temp = 0
                                n.coffee_machine()
                            elif not n.supplies():
                                #print("Not enough of supplies to make coffee, out of order.")
                                print(f"Here's your change: ${total - change}.")
                                Brew.money_jar -= recipe[2][0]
                                n.info()
                                n.coffee_machine()
                        elif self.money_jar_temp < recipe[2][0]:
                            print(f"Sorry that's not enough money, Money refunded - ${self.money_jar_temp:.2f}")
                            n.coffee_machine()
                        elif self.money_jar_temp == recipe[2][0]:
                            if not n.supplies():
                                #print("Not enough of supplies to make coffee, out of order.")
                                print(f"Here's your change: ${recipe[2][0]}.")
                                #Brew.money_jar -= recipe[2][0]
                                n.info()
                                n.coffee_machine()
                            elif n.supplies():
                                print("Brewing.")
                                time.sleep(1.5)
                                print("Brewing..")
                                time.sleep(1.5)
                                print("Brewing...")
                                time.sleep(1.5)
                                print("Your drink is dispensed.")
                                Brew.water -= recipe[2][1]
                                Brew.coffee -= recipe[2][2]
                                Brew.milk -= recipe[2][3]
                                Brew.money_jar += recipe[2][0]
                                self.money_jar_temp = 0
                                n.coffee_machine()

if __name__ == "__main__":
    n = Brew()
    n.coffee_machine()