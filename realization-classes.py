class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Reviewer(Person):
    def __str__(self):
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"

class Lecturer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        average_rating = self.average_rating()
        return (f"Имя: {self.first_name}\nФамилия: {self.last_name}\n"
                f"Средняя оценка за лекции: {average_rating:.1f}")

    def average_rating(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else 0

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def __str__(self):
        average_rating = self.average_rating()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.first_name}\nФамилия: {self.last_name}\n"
                f"Средняя оценка за домашние задания: {average_rating:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def average_rating(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    
reviewer1 = Reviewer('Ivan', 'Ivanov')
reviewer2 = Reviewer('Petr', 'Petrov')

lecturer1 = Lecturer('Anna', 'Smirnova')
lecturer2 = Lecturer('Igor', 'Sidorov')

student1 = Student('Elena', 'Kuznetsova')
student2 = Student('Oleg', 'Morozov')

student1.courses_in_progress.append('Python')
student1.finished_courses.append('Git')
student1.grades['Python'] = [9, 8, 10]

student2.courses_in_progress.append('Python')
student2.finished_courses.append('Git')
student2.grades['Python'] = [8, 7, 9]

lecturer1.courses_attached.append('Python')
lecturer1.grades['Python'] = [10, 9, 10]

lecturer2.courses_attached.append('Python')
lecturer2.grades['Python'] = [8, 9, 9]

def average_homework_grade(students, course_name):
    total_grade = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total_grade += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return total_grade / count if count else 0

def average_lecture_grade(lecturers, course_name):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grade += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    return total_grade / count if count else 0

print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

average_student_grade = average_homework_grade(students, 'Python')
average_lecturer_grade = average_lecture_grade(lecturers, 'Python')

print(f"Средняя оценка за домашние задания по курсу 'Python': {average_student_grade:.1f}")
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecturer_grade:.1f}")