# Learning objective: Match values from two arrays and return an array with distinct values

COURSES = ['English Course', 'Maths Course', 'History Course', 'Art Course', 'Science Course',
           'Spanish Course', 'French Course', 'Sport Course', 'Music Course']

# Note: The asterisk is the Python syntax for variable length arguments
# Example: validate_courses(English, Art, French)
def validate_courses(*course_subjects):

    course_matches = []

    # Return an array containing the courses that match course subjects passed as arguments
    # Hint:
    #   iterate subjects
    #       if valid subject
    #       and course starts with subject area
    #       add course to array

    return course_matches

# You might want to call this function to validate a course subject
def is_valid_course_subject(subject):
    if ('English' == subject or 'Maths' == subject or 'History' == subject
            or 'Art' == subject or 'Science' == subject or 'Spanish' == subject
            or 'French' == subject or 'Sport' == subject or 'Music' == subject):
        return True

    return False