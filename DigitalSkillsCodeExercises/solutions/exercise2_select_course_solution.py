# Learning objective: Add conditional logic "if statement"

AVAILABLE_COURSE = 'Course A'

def is_course_available(course_title):
    if AVAILABLE_COURSE == course_title:
        return True
    return False