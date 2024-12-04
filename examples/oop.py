# from datetime import date
import datetime


class Vehicle:
    # Class attribute
    wheels = 4

    def __init__(self, color, brand, model=None):
        # print("inside __init__", self)
        # Instance attributes
        self.color = color
        self.make = brand
        self.model = model
        self.speed = 0

    def accelerate(self, increment):
        if increment <= 0:
            raise ValueError(f"Cannot accelerate with {increment}.")
        self.speed += increment

    def brake(self, decrement):
        if decrement <= 0:
            raise ValueError(f"Cannot brake with {decrement}.")
        self.speed -= decrement

    def display_speed(self):
        print("Current speed:", self.speed)


if __name__ == "__main__":
    # help(datetime)
    # print(dir(datetime))

    # dt = date(2000, 3, 4)
    dt = datetime.date(2000, 3, 4)  # datetime.date.__init__
    print(dt.year, datetime.date.max, dt.max)
    # dt.year = 2001

    my_car = Vehicle(color="green", brand="Dacia", model="Sandero")  # Vehicle.__init__
    your_car = Vehicle("white", "Audi")

    print(dir(my_car))
    print("Accessing object attributes:", my_car.color, my_car.wheels, my_car.speed)

    print(your_car.make, your_car.speed, your_car.model)
    your_car.speed += 20
    your_car.model = "Q3"
    print(your_car.make, your_car.speed, your_car.model)

    # Vehicle.wheels = 7
    print("Class attribute value:", Vehicle.wheels)
    # print(my_car, your_car)

    my_car.display_speed()
    my_car.accelerate(20)
    my_car.display_speed()
    my_car.brake(15)
    my_car.display_speed()

    try:
        my_car.accelerate(-1)
    except ValueError as ex:
        print(ex)
