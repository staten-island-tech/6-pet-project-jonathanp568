class pet():
    def __init__(self, name, food, water, energy):
        self.name = name
        self.food = food
        self.water = water
        self.energy = energy
    def feed(self, feed):
        self.food += feed
        self.energy += feed * 4
    def drink(self, drink):
        self.water += drink
        self.energy += drink * 8
    def play(self, play):
        self.energy -= play
        self.food -= play % 4
        self.water -= play % 8


name = input("name?")                                
attributes = pet(name, 25, 50, 100)
while attributes.food or attributes.water or attributes.energy == 0:
    action = input("What do you want to do?")
    if action == "feed":
        amount = input("how much?")
        amount = int(amount)
        attributes.feed(amount)
        print("fed")
    elif action == "drink":
        amount = input("how much?")
        amount = int(amount)
        attributes.drink(amount)
        print("hydrated")
    elif action == "play":
        amount = input("how long?")
        amount = int(amount)
        attributes.play(amount)
        print(f"{amount} minutes played")
    elif action == "view":
        print(attributes.__dict__)
    else:
        print("invalid")
print(f"{name} died")