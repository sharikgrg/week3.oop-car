class Vehicle2():
    def __init__(self, wheels, capacity, colour):
        self.wheels = wheels
        self.capacity = capacity
        self.colour = colour

    def accelerate(self):
        return 'Vroooommmmmmmmm'
    def make_sound(self):
        return 'making noises##'

print(Vehicle2(2,3,'green'))