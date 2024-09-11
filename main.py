### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if self.machine_resources[ingredient] < ingredients[ingredient]: # compares ingrediesnts you have vs. required
                print(f"You do not have enough {ingredient} silly!")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        input("Please enter coins to pay: ")
        large_d = int(input("How many large dollar bills are you entering ($1): "))
        half_d = int(input("How many half dollar bills are you entering ($0.50): "))
        quarters = int(input("How many quarters are you entering ($0.25): "))
        nickels = int(input("How many nickels are you entering ($0.05): "))
        total = (large_d * 1) + (half_d * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("You do not have enough money. Please take your money back")
            return False
        elif coins > cost:
            change = round(coins-cost, 2)
            print(f"Take your change of {change}")
            return True
        else:
            print("Wow exact amount of money! There is $0.0 in change.")
            return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]
        print(f"{sandwich_size} is ready. Bon appetit!")

    def show_report(self):
        print("Resources:")
        for amount, ingredient in self.machine_resources.items():
            if ingredient == "bread" or ingredient == "ham":
                print(f"{ingredient}: {amount} slice(s)")
            else:
                print(f"{ingredient}: {amount} ounce(s)")

    def sandwich_cost(self, size):
        if size in ["small", "medium", "large"]:
            cost = recipes[size]["cost"]
            return cost
        elif size in ["off", "report"]:
            pass
        else:
            print("Please enter a valid entry")
            return None


### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)


while True:
    size = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    print(machine.sandwich_cost(size))


    if size == "off":
        print("Turning machine off")
        break
    elif size == "report":
        machine.show_report()
    elif size in ["small", "medium", "large"]:
        sandwich = recipes[size]
        if machine.check_resources(sandwich["ingredients"]):
            total_money = machine.process_coins()
            if machine.transaction_result(total_money, sandwich["cost"]):
                machine.make_sandwich(size, sandwich["ingredients"])
    else:
        print("Invalid Entry. Try again")

