class Food:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("You ran out of food!")

class Nugget(Food):
    def __init__(self, name):
        Food.__init__(self, name)
        self.name += " nugget"

    def dip(self, sauce):
        print("mmmm " + sauce + " dip!")


food = Food('chocolate')
print(food.name)
food.eat()

chkn = Nugget('Chicken')
print(chkn.name)
chkn.dip('Plum')
chkn.eat()