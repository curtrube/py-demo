"""A class that can be used to model a car."""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 27_567

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Return the car's current odometer reading"""
        return f"has {self.odometer} miles."

    def update_odometer(self, miles):
        """Update the odometer with current mileage"""
        self.odometer = miles


class Battery:
    """A simple attempt to model an electric car battery."""

    def __init__(self, battery_size=75):
        """Initialize the battery attributes."""
        self.battery_size = battery_size

    def describe_battery_size(self):
        return f"This car has a {self.battery_size}-kWh battery"


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        return f"This car doesn't need a gas tank!"

    def get_remaining_miles(self):
        """Get the remaining miles before a recharge."""
        pass
