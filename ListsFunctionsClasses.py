class vehicle:
    def __init__ (self, vehicle_type):
        self.vehicle_type = vehicle_type

class automobile(vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.vehicle_type}"
    
def main():
    car = "car"
    year = input("What is the year of the car: ")
    make = input("What is the make of the car: ")
    model = input("What is the model of the car: ")
    doors = input("How many doors does the car have(2 or 4): ")
    roof = input("What kind of roof does the car have(solid or sun roof): ")

    if doors not in ['2' or '4']:
        print("The car must have either 2 or 4 doors.")
        doors = input("How many doors does the car have(2 or 4): ")
    
    if roof not in ['solid' or 'sun roof']:
        print("You must type 'solid' or 'sun roof'")
        roof = input("What kind of roof does the carhave(solid or sun roof)")
    
    Car = automobile(car, year, make, model, doors, roof)
    print(Car)