from abc import ABC, abstractmethod

# Calculates key metrics like environmental impact, travel time, and eco-score for a given route. 
# By utilizing OOP principles like abstraction, encapsulation, inheritance, and polymorphism, 
# this code promotes flexibility, reusability, and maintainability.  
# The code structure allows for easy expansion, as new transport modes can be added without significant 
# changes to the existing system.


# the transport class __init__ self, mode is used in order to calculates key metrics like environmental impact,
# travel time, and eco-score for a given route. Each transport type whether a bike, jeepney, or a car, is represented 
# as a class that shares common behaviors but also has its own specific implementation of methods for calculating 
# emissions, travel time, and eco-scores.
class Transport(ABC): #abststraction
    def __init__(self, mode):
        self.mode = mode

    @abstractmethod
    def calculate_emissions(self, distance): #defined but not unimplemented, forcing any subclass to provide its specific logic
        pass

    @abstractmethod
    def calculate_travel_time(self, distance):
        pass

    @abstractmethod
    def calculate_eco_score(self, distance):
        pass

#all modes of transport uses inheritance 
class Bike(Transport):
    def __init__(self):
        super().__init__("Bike")

    def calculate_emissions(self, distance):
        return 0

    def calculate_travel_time(self, distance):
        return (distance / 15) * 60

    def calculate_eco_score(self, distance):
        return 100 


class Jeepney(Transport):
    def __init__(self):
        super().__init__("Jeepney")

    def calculate_emissions(self, distance):
        return 17 * distance / 1000

    def calculate_travel_time(self, distance):
        return (distance / 16) * 60

    def calculate_eco_score(self, distance):
        return int(100 - self.calculate_emissions(distance) * 200)


class Car(Transport):
    def __init__(self):
        super().__init__("Car")

    def calculate_emissions(self, distance):
        return distance * 0.15

    def calculate_travel_time(self, distance):
        return (distance / 60) * 60

    def calculate_eco_score(self, distance):
        return int(100 - self.calculate_emissions(distance) * 50)

#This class encapsulates information about the route and provides methods to access and present that information
class Route:
    def __init__(self, start, destination, distance):
        self.start = start
        self.destination = destination
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_details(self):
        return f"Route from {self.start} to {self.destination}, Distance: {self.distance} km"


#This is the main function and its the starting point of the program, this is where the user interacts with the system 
#to input details about a route and see the results based on different modes of transport
def main():
    start = input("Enter the starting location: ")
    destination = input("Enter the destination: ")
    distance = float(input("Enter the distance in kilometers: "))

    route = Route(start, destination, distance)

    bike = Bike()
    jeepney = Jeepney()
    car = Car()

    print(route.get_details())

    #Polymorphism 
    #Loops through different transport modes and calling methods
    transports = [bike, jeepney, car]
    for transport in transports:
        print(f"{transport.mode} emissions: {transport.calculate_emissions(route.get_distance())} kg CO2")
        print(f"{transport.mode} travel time: {transport.calculate_travel_time(route.get_distance())} minutes")
        print(f"{transport.mode} eco-score: {transport.calculate_eco_score(route.get_distance())}")

#used to ensure that a certain code is only executed when the script is run directly, 
#rather than when it is imported as a module in another script
if __name__ == "__main__":
    main()

