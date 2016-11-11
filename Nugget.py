class Food:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'no'

    def eat(self):
        print("You ran out of food!")

class Nugget(Food):
    def __init__(self, name):
        Food.__init__(self, name)
        self.name += " nugget"

    def __str__(self):
        return 'oh bbg'

    def dip(self, sauce):
        print("mmmm " + sauce + " dip!")


food = Food('chocolate')
print(food.name)
print(food)
food.eat()

chkn = Nugget('Chicken')
print(chkn.name)
print(chkn)
chkn.dip('Plum')
chkn.eat()