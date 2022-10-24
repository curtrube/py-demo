from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        return f"This car doesn't need a gas tank!"

    def get_remaining_miles(self):
        """Get the remaining miles before a recharge."""
        pass


my_tesla = ElectricCar("tesla", "model-X", "2022")
print(my_tesla.get_descriptive_name())
print(my_tesla.read_odometer())
print(my_tesla.fill_gas_tank())
