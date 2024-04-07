#Super class called vehicle, will have a subclass called automobile
class vehicle:
    def __init__ (self, vehicle_type):
        self.vehicle_type = vehicle_type
#Subclass called automobile, includes all attributes for car.
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
#Function for the input of the car details. Simply titled Car.
def Car():
    car = "car"
    year = input("What is the year of the car: ")
    make = input("What is the make of the car: ")
    model = input("What is the model of the car: ")
    doors = input("How many doors does the car have(2 or 4): ")
    roof = input("What kind of roof does the car have(solid or sun roof): ")
#If input for door is not 2 or 4
    if doors not in ['2' or '4']:
        print("The car must have either 2 or 4 doors.")
        doors = input("How many doors does the car have(2 or 4): ")
#If input for roof is not solid or sun
    if roof not in ['solid' or 'sun']:
        print("You must type 'solid' or 'sun'")
        roof = input("What kind of roof does the carhave(solid or sun roof)")
#Output car details
    car = automobile(car, year, make, model, doors, roof)
    print("\nCar details:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")


if __name__ == "__main__":
    Car()