from unittest import TestCase
from src.exercise6_course_budget import is_course_within_budget

class Evaluate(TestCase):

    def test_is_course_within_budget(self):
        self.assertEqual(True, is_course_within_budget(0, 1000), "Course budget should be <= 1000")
        self.assertEqual(True, is_course_within_budget(500, 1000), "Course budget should be <= 1000")
        self.assertEqual(True, is_course_within_budget(1000, 1000), "Course budget should be <= 1000")
        self.assertEqual(False, is_course_within_budget(1001, 1000), "Course budget should be <= 1000")