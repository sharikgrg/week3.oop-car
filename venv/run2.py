from car2 import *

vehicle_example = Vehicle2(2,4, 'blue')
car_example = Car2(2,3,'yellow', 'xc2', 'hatchback', 'ln09')

print('--------------------------')

print('Proof of Inheritance')
print(car_example.make_sound())

print ('-------------------------')

print('proof og polymorphism')
print(Car2(2,4, 'blue', 'xc2', 'hatchback', 'ln09').accelerate())
print(vehicle_example.accelerate())

print('----------------------')

print('Playing with encapsulation')
print(car_example.wheels)
print(car_example._accidents)
# print(car_example.__miles) # doesn't run because __

print(car_example.show_miles()) ## only showing as the method got defined