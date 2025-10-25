from unittest import TestCase
from src.exercise3_max_students import calculate_max_number_students

class Evaluate(TestCase):

    def test_calculate_max_number_students(self):
        self.assertEqual(200, calculate_max_number_students(10, 20),
                         "Counter should equal 200")