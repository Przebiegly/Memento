class Memento:
    #Klasa przechowująca stan ocen
    def __init__(self, grades):
        self.grades = grades

    def get_grades(self):
        return self.grades
