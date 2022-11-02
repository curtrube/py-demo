import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test's for name_function.py"""

    def test_first_last_name(self):
        """Do names like Jim Smith work?"""
        formatted_name = get_formatted_name("jim", "smith")
        self.assertEqual(formatted_name, "Jim Smith")

    def test_first_middle_last_name(self):
        """Do middle names work? Like John Jacob Smith."""
        formatted_name = get_formatted_name(
            first_name="john", middle_name="jacob", last_name="smith"
        )
        self.assertEqual(formatted_name, "John Jacob Smith")


if __name__ == "__main__":
    unittest.main()
