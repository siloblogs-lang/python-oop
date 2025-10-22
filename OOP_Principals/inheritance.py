class Vihicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vihicle is starting")

    def stop(self):
        print("Vehicle is stopping")

    
class Car(Vihicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)  
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vihicle):
    def __init__(self, brand, model, year,  number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

car = Car("Ford", "Focus", 2008, 5, 4)
bike = Bike("Indian", "Fast", 1967, 2)
print(car.__dict__)
