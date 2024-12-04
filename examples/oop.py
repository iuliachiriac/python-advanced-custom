# from datetime import date
import datetime


class Vehicle:
    # Class attribute
    wheels = 0

    def __init__(self, color, brand, model=None):
        # print("inside __init__", self)
        # Instance attributes
        self.color = color
        self.make = brand
        self.model = model
        self.speed = 0


# help(datetime)
# print(dir(datetime))

# dt = date(2000, 3, 4)
dt = datetime.date(2000, 3, 4)  # datetime.date.__init__
print(dt.year)
# dt.year = 2001

my_car = Vehicle(color="green", brand="Dacia", model="Sandero")  # Vehicle.__init__
your_car = Vehicle("white", "Audi")

print(dir(my_car))
print("Accessing object attributes:", my_car.color, my_car.wheels)


# print(my_car, your_car)
