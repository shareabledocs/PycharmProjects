from unittest import TestCase
from src.exercise2_select_course import is_course_available

class Evaluate(TestCase):
    def test_select_course(self):
        self.assertEqual(False, is_course_available(""),"")
        self.assertEqual(False, is_course_available(None),"None")
        self.assertEqual(True, is_course_available("Course A"), "Course A")
        self.assertEqual(False, is_course_available("Course B"),"Course B")
        self.assertEqual(False, is_course_available("Course C"),"Course  C")
        self.assertEqual(False, is_course_available("Course D"),"Course  D")
        self.assertEqual(False, is_course_available("Course E"),"Course  E")