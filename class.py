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
        self.happiness -= feed *5
    def drink(self, drink):
        self.water += drink
        self.energy += drink * 10
        self.happiness -= drink *10
    def play(self, play):
        self.happiness += play
        self.energy -= play
        self.food -= play / 5
        self.water -= play / 10


name = input("name?")                                
attributes = pet(name, 25, 50, 100, 100)
while attributes.food > 0 and attributes.water > 0 and attributes.energy > 0:
    if attributes.happiness < 1:
        print(f"{name} didn't wanna live anymore.")
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
        print("drank")
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