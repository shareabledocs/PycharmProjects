from unittest import TestCase
from src.exercise5_validate_courses import validate_courses

class Evaluate(TestCase):

    def test_validate_courses(self):
        self.assertEqual(['English Course', 'Maths Course', 'Music Course'],
                         validate_courses('English', 'Maths', 'Music'),
                         "There should be 3 courses returned: English Course, Maths Course, Music Course")
        self.assertEqual([], validate_courses(), "There should be 0 courses returned")
        self.assertEqual([], validate_courses(''),"There should be 0 courses returned")
        self.assertEqual([], validate_courses('Geography'),"There should be 0 courses returned")
        self.assertEqual([], validate_courses('invalid area'), "There should be 0 courses returned")