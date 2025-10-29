class pet():
    def __init__(self, name, food, water, energy, dead):
        self.name = name
        self.food = food
        self.water = water
        self.energy = energy
        self.dead = dead
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
    def death(self):
        if self.food or self.water or self.energy < 1:
            self.dead == True
        


name = input("name?")
attributes = pet(name, 25, 50, 100, False)
while attributes.death() is not True:
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