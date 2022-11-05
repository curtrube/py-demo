import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test case for AnonymousSurvey class."""

    def setUp(self):
        """Create a survey and a set of responses for use in all the test methods."""
        question = "what is your favorite language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["english", "spanish", "french"]

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test if three responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
