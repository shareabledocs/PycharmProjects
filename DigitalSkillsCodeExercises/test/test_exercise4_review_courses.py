from unittest import TestCase
from src.exercise4_review_courses import review_courses

class Evaluate(TestCase):
    def test_review_courses(self):
        self.assertEqual(200, review_courses(100), "Courses reviewed should equal 200")
        self.assertEqual(400, review_courses(200), "Courses reviewed should equal 400")