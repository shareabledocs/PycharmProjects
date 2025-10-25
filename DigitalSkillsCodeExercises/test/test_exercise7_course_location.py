from unittest import TestCase
from src.exercise7_course_location import is_course_in_location

class Evaluate(TestCase):

    def test_is_course_in_location(self):
        self.assertEqual(True, is_course_in_location('English Course', 'Location A'),"English Course is offered in Location A")
        self.assertEqual(False, is_course_in_location('English Course', 'Location B'),"English Course is not offered in Location B")
        self.assertEqual(False, is_course_in_location('English Course', 'Location C'),"English Course is not offered in Location C")
        self.assertEqual(False, is_course_in_location('English Course', 'Location D'),"English Course is not offered in Location D")
        self.assertEqual(False, is_course_in_location('English Course', 'Location E'),"English Course is not offered in Location E")
        self.assertEqual(False, is_course_in_location('English Course', 'Location F'),"English Course is not offered in Location F")
        self.assertEqual(False, is_course_in_location('English Course', 'Location G'),"English Course is not offered in Location G")
        self.assertEqual(False, is_course_in_location('English Course', 'Location H'),"English Course is not offered in Location H")
        self.assertEqual(False, is_course_in_location('English Course', 'Location I'),"English Course is not offered in Location I")
        self.assertEqual(True, is_course_in_location('Maths Course', 'Location B'), "Maths Course is offered in Location B")
        self.assertEqual(True, is_course_in_location('History Course', 'Location C'), "French Course is offered in Location C")
        self.assertEqual(True, is_course_in_location('Art Course', 'Location D'), "French Course is offered in Location D")
        self.assertEqual(True, is_course_in_location('Science Course', 'Location E'), "French Course is offered in Location E")
        self.assertEqual(True, is_course_in_location('Spanish Course', 'Location F'), "French Course is offered in Location F")
        self.assertEqual(True, is_course_in_location('French Course', 'Location G'), "French Course is offered in Location G")
        self.assertEqual(True, is_course_in_location('Sport Course', 'Location H'), "French Course is offered in Location H")
        self.assertEqual(True, is_course_in_location('Music Course', 'Location I'), "French Course is offered in Location I")