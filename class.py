class pet():
    def __init__(self, name, food, water):
        self.food = food
        self.name = name
        self.water = water
    def feed(self, feed):
        self.food += feed
        print(self.food)
    def feed(self, drink):
        self.water += drink
        print(self.water)
attributes = pet("i", 10, 10)
attributes.feed(10)