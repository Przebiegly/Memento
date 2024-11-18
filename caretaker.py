from memento import Memento

class Caretaker:
    #Zarządza zapisami stanu ocen
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        #Dodaje memento do historii
        self.mementos.append(memento)

    def get_memento(self, index):
        #Pobiera memento na podstawie indeksu
        return self.mementos[index]
