from vehicle2 import *
class Car2(Vehicle2):
    def __init__(self, wheels, capacity, colour, make, model, plate):
        super().__init__(wheels, capacity, colour)
        self.make = make
        self.model = model
        self.plate = plate
        self._accidents = 0 # visibility is limited
        self.__miles = 0 # visibility and access is restricted

    def make_sound(self):
        return 'Revving my car! Vroom'
    def play_music(self):
        return
    def accelerate(self):
        self.__increase_miles()
        return 'vrom'

    def set_miles(self): # getter
        return self.__miles

    def show_miles(self, miles): # setter- to check some security stuff befor checking
        self.__miles = miles
        return 'miles set to' + miles

    def increase__miles(self):
        self.__miles +=100
        return
    pass
