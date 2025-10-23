# class pet():
#     def __init__(self, food):
#         self.food = food
#         return self.food
#     def feed(self, feed):
#         food += feed
#         return self.food
# pet.__init__(10)

def slots(q, x, y, z):
    quarters = q
    slots1 = x
    slots2 = y
    slots3 = z
    plays = 0
    while quarters != 0:
        if slots1 != 35 and quarters != 0:
            slots1 += 1
            quarters -= 1
            plays += 1
        elif slots1 == 35:
            quarters += 30
            slots1 -= 35
        if slots2 != 100 and quarters != 0:
            slots2 += 1
            quarters -= 1
            plays += 1
        elif slots2 == 100:
            quarters += 60
            slots2 -= 100
        if slots3 != 10 and quarters != 0:
            slots3 += 1
            quarters -= 1
            plays += 1
        elif slots3 == 10:
            quarters += 9
            slots3 -= 10
    print(f"Martha plays {plays} times before going broke.")

slots(77, 4, 9, 3)