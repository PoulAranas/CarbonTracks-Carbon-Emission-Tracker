import tkinter as tk
from tkinter import messagebox

class Transport:
    def __init__(self, mode):
        self.mode = mode

    def calculate_emissions(self, distance):
        raise NotImplementedError

    def calculate_travel_time(self, distance):
        raise NotImplementedError

    def calculate_eco_score(self, distance):
        raise NotImplementedError

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

class TransportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transport Emissions and Eco-Score Calculator")
        self.root.geometry("600x500")
        self.root.configure(bg="#006400")

        self.input_panel = tk.Frame(self.root, bg="#006400")
        self.input_panel.pack(pady=20)

        self.start_label = tk.Label(self.input_panel, text="Starting Location:", bg="#006400", fg="white")
        self.start_label.grid(row=0, column=0, padx=10, pady=5)
        self.start_field = tk.Entry(self.input_panel)
        self.start_field.grid(row=0, column=1, padx=10, pady=5)

        self.destination_label = tk.Label(self.input_panel, text="Destination:", bg="#006400", fg="white")
        self.destination_label.grid(row=1, column=0, padx=10, pady=5)
        self.destination_field = tk.Entry(self.input_panel)
        self.destination_field.grid(row=1, column=1, padx=10, pady=5)

        self.distance_label = tk.Label(self.input_panel, text="Distance (km):", bg="#006400", fg="white")
        self.distance_label.grid(row=2, column=0, padx=10, pady=5)
        self.distance_field = tk.Entry(self.input_panel)
        self.distance_field.grid(row=2, column=1, padx=10, pady=5)

        self.result_panel = tk.Frame(self.root, bg="#006400")
        self.result_panel.pack(pady=20)

        self.result_text = tk.Text(self.result_panel, height=10, width=50, bg="white", fg="black")
        self.result_text.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate, bg="#228B22", font=("Arial", 12, "bold"))
        self.calculate_button.pack(pady=10)

    def calculate(self):
        try:
            start = self.start_field.get()
            destination = self.destination_field.get()
            distance = float(self.distance_field.get())

            route = Route(start, destination, distance)

            bike = Bike()
            jeepney = Jeepney()
            car = Car()

            transports = [bike, jeepney, car]
            result = route.get_details() + "\n\n"

            for transport in transports:
                result += f"{transport.mode}\n"
                result += f"Emissions: {transport.calculate_emissions(route.get_distance())} kg CO2\n"
                result += f"Travel Time: {transport.calculate_travel_time(route.get_distance())} minutes\n"
                result += f"Eco-Score: {transport.calculate_eco_score(route.get_distance())}\n\n"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid distance.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransportApp(root)
    root.mainloop()
