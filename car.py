from vehicle import *
class Car(Vehicle):
    def __init__(self, wheels, capacity, colour, year, brand, plate, airbag):
        super().__init__(wheels, capacity, colour, year)
        self.brand = brand
        self.plate = plate
        self.airbag = airbag

    def music(self, sing):
        return'boom boom poww!!!' + sing
    def horn(self):
        return'Beep Beep'
    def lock(self):
        return'tik tik'
    def wiper(self):
        return'sheakkkk sheakkk'
    def windows_moving(self):
        return'chiiiiiiiiii'
    def ignition(self):
        return'vroom'
    def makeAsound(self):
        return 'bammmm'