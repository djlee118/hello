class Car(object):
    condition = "New"

    def __init__(self, color, model, mpg):
        self.color = color
        self.model = model
        self.mpg = mpg

    def display_car(self):
        return "This is a {0} {1} with {2} MPG.".format(self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, color, model, mpg, battery_type):
        Car.color = color
        Car.model = model
        Car.mpg = mpg
        self.battery_type = battery_type

    def display_car(self):
        return "This is a {0} {1} with {2} MPG, {3}.".format(self.color, self.model, self.mpg, self.battery_type)


my_car = Car("Red", "BMW", "300")
print(my_car.condition)
print(my_car.color, my_car.model, my_car.mpg)

print(my_car.display_car())
my_car.drive_car()
print(my_car.condition)


elec_my_car = ElectricCar("Blue", "KIA", "500", "Good")
print(elec_my_car.display_car())
elec_my_car.drive_car()
print(elec_my_car.condition)


