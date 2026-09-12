class viehcle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print("Car brand is: ", self.brand)
        print("The viehcles max speed is:  ", self.max_speed, "km/h") 

class car(viehcle):
    def __init__(self, model, seats, brand, max_speed, fuel):
        self.model = model
        self.seats = seats
        self.fuel = fuel
        super().__init__(brand, max_speed)     

    def show_details(self):
        ("Car has a total seats of: ",self.seats)
        ("Car is a model, ",self.model)
        super().show_details()

    def fuel_type(self):
        print("The cars fuel type is: ", self.fuel)

car1 = car("corrola", 4, "Toyota", 240, "Petrol")
print(car1)

car1.show_details()
car1.fuel_type()        