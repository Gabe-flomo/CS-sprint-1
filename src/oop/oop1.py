# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:pass
# Parent
    
class FlightVehicle:pass
# Parent
    
class Starship:pass
# Parent

class GroundVehicle(Vehicle):pass
# Child of Vehicle
    
class Airplane(FlightVehicle):pass
# Child of flightvehicle

class Car(GroundVehicle):pass
# Child of ground vehicle

class Motorcycle(GroundVehicle):pass
# Child of ground vehicle


