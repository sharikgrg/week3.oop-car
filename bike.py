from vehicle import *
class Bike(Vehicle):
    def __init__(self, wheels, capacity, colour, year, gears, type, basket):
        super().__init__(wheels, capacity, colour, year)
        self.gears = gears
        self.handle_bar_type = type
        self.basket = basket

    def pedalling(self):
        return'paddlingggg'
    def wheely(self):
        return'weeeeeeeyyyyyyyyyy'
    def chain(self):
        return'kreek kreak'
    def making_sound(self):
        return'cccccreeaaaaaaaaaaaakkkkkkk'
    def bell(self, name):
        return'tring tring' + name
    def makeAsound(self):
        return 'pppeaaaakkkk'