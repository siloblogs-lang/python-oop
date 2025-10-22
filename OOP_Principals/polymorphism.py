# Ugly code
class Car:
    def __init__(self, brand, model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

    def start_car(self):
        print("Car is starting")

    def stop_car(self):
        print("Car is stopping")

class Motorcycle:
    def __init__(self, brand, model, year, number_of_wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_wheels = number_of_wheels

    def start_bike(self):
        print("Motorcycle started")

    def stop_bike(self):
        print("Motorcycle is stopping")

vehicles = [
    Car("Ford", "Focus", 2009, 4),
    Motorcycle("Honda", "Ninja", 2009, 2)
]

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_car()
        vehicle.stop_car()
    elif isinstance(vehicle, Motorcycle): 
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a valid vihecle")