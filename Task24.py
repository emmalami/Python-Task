# Create an abstract class called Vehicle
# Create an abstract method called drive_direction()
# Create another class Car that inherits from Vehicle
# Create another class Plane that inherits from Vehicle
# Try running the program and fix the abstract method issues
# Optionally instantiate the Car and Plane method,
# then invoke the drive_direction() in each of the object instances.
# Hint: the drive_direction() method in your Car should print "Drive forward",
# while drive_direction() in your Plane class should print "Drive Upward"

import abc


class vehicle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drive_direction(self):
        pass


class car(vehicle):
    def drive_direction(self):
        return "Drive forward"


class plane(vehicle):
    def drive_direction(self):
        return "Drive upward"

car = car()
print(car.drive_direction())

plane = plane()
print(plane.drive_direction())