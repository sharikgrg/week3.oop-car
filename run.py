from vehicle import *
from bike import *
from car import *

print("-----Vehicular test---------")
vehicle = Vehicle(4, 4, 'yellow', 2019)
print(vehicle.brake())
print(f' It has {vehicle.wheels} wheels')
print(vehicle.makeAsound())
print('                              ')
print("-----Bike test---------")
print('                              ')
bike = Bike('buzz', 2, 1, 'red', 2016, 2, 'road')
print(f' your bike colour is {bike.colour}')
print(f'There are {bike.wheels} wheels in your bike')
print(f' It was manufactured on {vehicle.year}')
print(bike.making_sound())
print('                              ')
print("-----Car test---------")
print('                              ')
car = Car( 4, 4, 'red', 2019, 'ferri', 'ly19', False)
print(f' your car colour is {car.colour}')
print(f'There are {bike.wheels} wheels in your car')
print(car.makeAsound())