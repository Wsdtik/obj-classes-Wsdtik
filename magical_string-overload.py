class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Reviewer(Person):
    def __str__(self):
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"

class Lecturer(Person):
    def __init__(self, first_name, last_name, average_rating):
        super().__init__(first_name, last_name)
        self.average_rating = average_rating

    def __str__(self):
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: {self.average_rating}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_rating < other.average_rating

class Student(Person):
    def __init__(self, first_name, last_name, average_rating, courses_in_progress, finished_courses):
        super().__init__(first_name, last_name)
        self.average_rating = average_rating
        self.courses_in_progress = courses_in_progress
        self.finished_courses = finished_courses

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.first_name}\nФамилия: {self.last_name}\n"
                f"Средняя оценка за домашние задания: {self.average_rating}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating < other.average_rating

some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)

some_lecturer = Lecturer('Some', 'Buddy', 9.9)
print(some_lecturer)

some_student = Student('Ruoy', 'Eman', 9.9, ['Python', 'Git'], ['Введение в программирование'])
print(some_student)
