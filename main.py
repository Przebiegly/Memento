from student import Student
from grades import Grades
from caretaker import Caretaker

def main():
    # Tworzymy ucznia
    student = Student("Jan Kowalski")
    grades_system = Grades(student)

    # Tworzymy Caretaker, który będzie przechowywał mementa
    caretaker = Caretaker()

    print("Początkowy stan ocen:")
    print(grades_system)

    # Zapisujemy początkowy stan ocen
    caretaker.add_memento(grades_system.save_state_to_memento())

    # Dodajemy oceny
    student.add_grade(5)
    student.add_grade(4)
    student.add_grade(3)

    print("\nPo dodaniu ocen:")
    print(grades_system)

    # Zapisujemy stan po dodaniu ocen
    caretaker.add_memento(grades_system.save_state_to_memento())

    # Usuwamy ocenę
    student.remove_grade(3)

    print("\nPo usunięciu jednej oceny:")
    print(grades_system)

    # Zapisujemy stan po usunięciu oceny
    caretaker.add_memento(grades_system.save_state_to_memento())

    # Przywracamy stan ocen z pierwszego zapisu (początkowy stan)
    grades_system.restore_state_from_memento(caretaker.get_memento(0))

    print("\nPo przywróceniu początkowego stanu ocen:")
    print(grades_system)

if __name__ == "__main__":
    main()
