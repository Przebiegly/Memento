class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def __str__(self):
        return f"Uczeń: {self.name}, Oceny: {', '.join(map(str, self.grades))}"

    def add_grade(self, grade): #Dodaje ocenę do listy
        self.grades.append(grade)

    def remove_grade(self, grade): #Usuwa ocenę z listy
        if grade in self.grades:
            self.grades.remove(grade)

    def set_grades(self, grades): #Ustawia oceny
        self.grades = grades

    def get_grades(self):
        return self.grades
