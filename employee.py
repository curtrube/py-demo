class Employee:
    """Simple class to model an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=""):
        """Give an employee a salary raise."""
        if raise_amount:
            self.annual_salary += raise_amount
        else:
            self.annual_salary += 5000
