# from datetime import date
import datetime


class InvalidSpeedChange(ValueError):
    pass


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

    def accelerate(self, increment):
        self.validate_speed_change(increment)
        self.speed += increment

    def brake(self, decrement):
        self.validate_speed_change(decrement)
        self.speed -= decrement

    @staticmethod
    def validate_speed_change(value):
        if value <= 0:
            raise InvalidSpeedChange(f"Cannot change speed by {value}")

    def display_speed(self):
        print("Current speed:", self.speed)

    def __str__(self):
        return f"{self.__class__.__name__} object <{self.make} {self.model}>"


class Car(Vehicle):
    wheels = 4

    def __init__(self, color, make, model, fuel_type):
        super().__init__(color, make, model)
        self.fuel_type = fuel_type

    def display_speed(self):
        print(f"I am {self.make} {self.model}")
        super().display_speed()

    def honk_horn(self):
        print("Beep beep!")


if __name__ == "__main__":
    # help(datetime)
    # print(dir(datetime))

    # dt = date(2000, 3, 4)
    dt = datetime.date(2000, 3, 4)  # datetime.date.__init__
    print(dt.year, datetime.date.max, dt.max)

    my_vehicle = Vehicle(color="green", brand="Dacia", model="Sandero")
    your_vehicle = Vehicle("white", "Audi")

    print(dir(my_vehicle))
    print("Accessing object attributes:", my_vehicle.color, my_vehicle.wheels,
          my_vehicle.speed)

    print(your_vehicle.make, your_vehicle.speed, your_vehicle.model)
    your_vehicle.speed += 20
    your_vehicle.model = "Q3"
    print(your_vehicle.make, your_vehicle.speed, your_vehicle.model)

    # Vehicle.wheels = 7
    print("Class attribute value:", Vehicle.wheels)
    # print(my_car, your_car)

    my_vehicle.display_speed()
    my_vehicle.accelerate(20)
    my_vehicle.display_speed()
    my_vehicle.brake(15)
    my_vehicle.display_speed()

    try:
        my_vehicle.accelerate(-1)
    except InvalidSpeedChange as ex:
        print(ex)

    my_car = Car("white", "Dacia", "Logan", "gasoline")
    print(type(my_car))
    print(my_car.fuel_type)
    my_car.accelerate(100)
    my_car.display_speed()
    my_car.honk_horn()

    print(my_vehicle, my_car)
