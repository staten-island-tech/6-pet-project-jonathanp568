class pet():
    def __init__(self, name, food, water, energy, happiness):
        self.name = name
        self.food = food
        self.water = water
        self.energy = energy
        self.happiness = happiness
    def feed(self, feed):
        self.food += feed
        self.energy += feed * 5
        self.happiness -= feed * 2
    def drink(self, drink):
        self.water += drink
        self.energy += drink * 5
        self.happiness -= drink * 1
    def play(self, play):
        self.happiness += play
        self.energy -= play
        self.food -= play / 10
        self.water -= play / 20
    def start(food, water, energy, happiness):
        name = input("name?")
        attributes = pet(name, food, water, energy, happiness)    
        days = 0
        while attributes.food > 0 and attributes.water > 0 and attributes.energy > 0:
            days += 1
            print(f"{days} days passed")
            attributes.food -= 2
            attributes.water -= 4
            attributes.energy += 5
            attributes.happiness -= 10
            if attributes.happiness < 1:
                print(f"{name} didn't want to live anymore.")
                break
            if attributes.food < 1 or attributes.water < 1 or attributes.energy < 1:
                print(f"{name} died")
                break
            if attributes.food > 25:
                print(f"{name} is full.")
                attributes.food = 25
            if attributes.water > 50:
                print(f"{name} is hydrated.")
                attributes.water = 50
            if attributes.energy > 100:
                print(f"{name} is energized.")
                attributes.energy = 100
            if attributes.happiness > 100:
                print(f"{name} is happy.")
                attributes.happiness = 100
            actions = 0
            while actions < 2:
                action = input("what do you want to do? you could feed, drink, play, or view.")
                if action == "view":
                    print(attributes.__dict__)
                elif action == "feed":
                    amount = input("how much?")
                    while amount.islower() or amount.isupper() or not amount.isdigit():
                        if amount.islower() or amount.isupper() or not amount.isdigit():
                            amount = input("invalid, how much?")
                        else:
                            amount = int(amount)
                    amount = int(amount)
                    attributes.feed(amount)
                    print(f"fed {amount} food")
                    actions += 1
                elif action == "drink":
                    amount = input("how much?")
                    while amount.islower() or amount.isupper() or not amount.isdigit():
                        if amount.islower() or amount.isupper() or not amount.isdigit():
                            amount = input("invalid, how much?")
                        else:
                            amount = int(amount)
                    amount = int(amount)
                    attributes.drink(amount)
                    print(f"drank {amount} water")
                    actions += 1
                elif action == "play":
                    amount = input("how much?")
                    while amount.islower() or amount.isupper() or not amount.isdigit():
                        if amount.islower() or amount.isupper() or not amount.isdigit():
                            amount = input("invalid, how much?")
                        else:
                            amount = int(amount)
                    amount = int(amount)
                    attributes.play(amount)
                    print(f"{amount} minutes played")
                    actions += 1
                else:
                    print("invalid")
                if attributes.food > 25:
                    print(f"{name} is full.")
                    attributes.food = 25
                if attributes.water > 50:
                    print(f"{name} is hydrated.")
                    attributes.water = 50
                if attributes.energy > 100:
                    print(f"{name} is energized.")
                    attributes.energy = 100
                if attributes.happiness > 100:
                    print(f"{name} is happy.")
                    attributes.happiness = 100
                if attributes.happiness < 1:
                    print(f"{name} didn't want to live anymore.")
                    break
                if attributes.food < 1 or attributes.water < 1 or attributes.energy < 1:
                    print(f"{name} died")
                    break
pet.start(25, 50, 100, 100) 