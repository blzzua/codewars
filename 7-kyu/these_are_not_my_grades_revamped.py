# https://www.codewars.com/kata/5956d127a817c7c51b000026

class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades
    
    def add_grade(self, grade):
        self.grades = self.grades + [grade]
    
    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

