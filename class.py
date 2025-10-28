class pet():
    def __init__(self, name, food, water, energy, dead):
        self.food = food
        self.name = name
        self.water = water
        self.energy = energy
        self.dead = dead
        print(f"{name} = food: {self.food} water: {self.water} energy: {self.energy}")
    def feed(self, feed):
        self.food += feed
        self.energy += feed * 4
        print(self.food)
    def drink(self, drink):
        self.water += drink
        self.energy += drink * 8
        print(self.water)
    def play(self, play):
        self.energy -= play
        self.food -= play % 4
        self.water -= play % 8
        print(self.energy)
    def dead(self):
        if self.food or self.water or self.energy == 0:
            self.dead == True
        else:
            self.dead == False
        


name = input("name?")
action = input("What do you want to do?")
attributes = pet(name, 25, 50, 100, False)
while attributes.dead is not True:
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
        print("DO SOMETHING")
print("your pet died")