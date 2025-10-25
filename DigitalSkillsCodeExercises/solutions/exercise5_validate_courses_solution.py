COURSES = ['English Course', 'Maths Course', 'History Course', 'Art Course', 'Science Course', 'Spanish Course',
           'French Course', 'Sport Course', 'Music Course']

def validate_courses(*course_subjects):
    course_matches = []

    for subject in course_subjects:
        if subject or is_valid_course_subject(subject):
            for course in COURSES:
                if course.startswith(subject):
                    course_matches.append(course)

    return course_matches

def is_valid_course_subject(subject):
    if ('English' == subject or 'Maths' == subject or 'History' == subject
            or 'Art' == subject or 'Science' == subject or 'Spanish' == subject
            or 'French' == subject or 'Sport' == subject or 'Music' == subject):
        return True

    return False