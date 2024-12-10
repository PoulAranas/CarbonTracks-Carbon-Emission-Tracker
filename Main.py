from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, mode):
        self.mode = mode

    @abstractmethod
    def calculate_emissions(self, distance):
        pass

    @abstractmethod
    def calculate_travel_time(self, distance):
        pass

    @abstractmethod
    def calculate_eco_score(self, distance):
        pass


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


class Route:
    def __init__(self, start, destination, distance):
        self.start = start
        self.destination = destination
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_details(self):
        return f"Route from {self.start} to {self.destination}, Distance: {self.distance} km"


def main():
    print("Welcone to CarbonTracks: The Carbon Emission Tracker!")
    print("Calculate emissions, travel time, and eco-score for different modes of transport.\n")

    while True:
        start = input("Enter the starting location: ")
        destination = input("Enter the destination: ")
        try:
            distance = float(input("Enter the distance in kilometers: "))
        except ValueError:
            print("Invalid distance! Please enter a numeric value.\n")
            continue

        route = Route(start, destination, distance)

        transports = [Bike(), Jeepney(), Car()]

        print("\n" + "=" * 50)
        print(route.get_details())
        print("=" * 50)

        for transport in transports:
            print(f"\nMode of Transport: {transport.mode}")
            print(f" - Emissions: {transport.calculate_emissions(route.get_distance()):.2f} kg CO2")
            print(f" - Travel Time: {transport.calculate_travel_time(route.get_distance()):.2f} minutes")
            print(f" - Eco-Score: {transport.calculate_eco_score(route.get_distance())}/100")

        print("\n" + "=" * 50)
        again = input("Do you want to calculate for another route? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nThank you for using CarbonTracks. Goodbye!")
            break


if __name__ == "__main__":
    main()
