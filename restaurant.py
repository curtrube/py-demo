class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"The {self.restaurant_name.title()} restaurant serves {self.cuisine_type} food."

    def open_restaurant(self):
        return (
            f"The {self.restaurant_name.title()} restaurant is now open for business!"
        )


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "cookie-dough"]

    def display_flavors(self):
        return f"Avaiable ice cream flavors: {self.flavors}"


dairy_queen = IceCreamStand("dairy queen", "fast food")
print(dairy_queen.describe_restaurant())
print(dairy_queen.open_restaurant())
print(dairy_queen.display_flavors())
