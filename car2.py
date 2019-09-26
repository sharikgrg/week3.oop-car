from vehicle2 import *
class Car2(Vehicle2):
    def __init__(self, wheels, capacity, colour, make, model, plate):
        super().__init__(wheels, capacity, colour)
        self.make = make
        self.model = model
        self.plate = plate

    def make_sound(self):
        return 'Revving my car! Vroom'
    def play_music(self):
        return
    def accelerate(self):
        return 'vrom'
    pass
print('Proof of Inheritance')
print(Car2(2,3,'yello').make_sound())
print('proof og polymorphism')
print(Car2(2,4, 'blue').accelerate())
print(Vehicle2(2,4, 'blue').accelerate())