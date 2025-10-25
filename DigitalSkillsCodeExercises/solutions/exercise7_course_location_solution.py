COURSES = {'English Course': 'Location A',
           'Maths Course': 'Location B',
           'History Course': 'Location C',
           'Art Course': 'Location D',
           'Science Course': 'Location E',
           'Spanish Course': 'Location F',
           'French Course': 'Location G',
           'Sport Course': 'Location H',
           'Music Course': 'Location I'}

def is_course_in_location(course_name, location):
    if COURSES[course_name] == location:
        return True

    return False