import unittest
from src.exercise1_sort_courses import sort_courses_ascending_alphabetical_order

class TestCaseSortCourses(unittest.TestCase):
    def test_sort_courses(self):
        courses = ['Course A', 'Course B', 'Course C', 'Course D', 'Course E']

        self.assertEqual(courses, sort_courses_ascending_alphabetical_order(),
                         "Courses should be in alphabetical order")