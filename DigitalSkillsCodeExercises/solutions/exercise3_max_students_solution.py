def calculate_max_number_students(total_courses, students_per_class):
    counter = 0

    for idx in range(0, total_courses):
        counter = counter + students_per_class

    return counter