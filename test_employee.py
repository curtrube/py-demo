import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for Employee class."""

    def setUp(self):
        self.my_employee = Employee("jim", "smith", 100_000)

    def test_give_default_raise(self):
        """Test giving an employee a default raise."""
        self.my_employee.give_raise()
        self.assertEqual(105_000, self.my_employee.annual_salary)

    def test_give_custom_raise(self):
        """Test giving and employee a custom raise amount."""
        self.my_employee.give_raise(1000)
        self.assertEqual(101_000, self.my_employee.annual_salary)


if __name__ == "__main__":
    unittest.main()
