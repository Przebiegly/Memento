# grades.py
from student import Student
from memento import Memento

class Grades:
    #System ocen ucznia
    def __init__(self, student):
        self.student = student

    def __str__(self):
        return f"System ocen: {self.student}"

    def save_state_to_memento(self):
       #Zapisuje stan ocen ucznia w memento (z kopią listy)
        return Memento(self.student.get_grades().copy())  # Tworzymy kopię listy ocen

    def restore_state_from_memento(self, memento):
        #Przywraca stan ocen ucznia z memento
        self.student.set_grades(memento.get_grades())
