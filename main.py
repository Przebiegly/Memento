class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def create_memento(self):
        return CarBackup(self.brand, self.model, self.year)

    def restore(self, memento):
        self.brand = memento.brand
        self.model = memento.model
        self.year = memento.year

    def __str__(self):
        return f"Car(Brand: {self.brand}, Model: {self.model}, Year: {self.year})"


class CarBackup:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Caretaker:
    def __init__(self):
        self.snapshots = []

    def add_memento(self, memento):
        self.snapshots.append(memento)

    def get_memento(self, index):
        if 0 <= index < len(self.snapshots):
            return self.snapshots[index]
        return None

    def list_snapshots(self):
        if not self.snapshots:
            print("Brak zapisanych snapów.")
            return
        for i, snapshot in enumerate(self.snapshots):
            print(f"Snap {i}: {snapshot}")


# Przykład użycia
if __name__ == "__main__":

    car = Car("Toyota", "Corolla", 2020)
    print(car)

    caretaker = Caretaker()

    caretaker.add_memento(car.create_memento())

    # Zmiana
    car.brand = "Honda"
    car.model = "Civic"
    car.year = 2022
    print(car)

    caretaker.add_memento(car.create_memento())

    # Zmiana
    car.brand = "Ford"
    car.model = "Focus"
    car.year = 2021
    print(car)

    caretaker.add_memento(car.create_memento())

    print("\nHistoria snapów:")
    caretaker.list_snapshots()

    print("\nPrzywracanie stanu do Snap 1:")
    car.restore(caretaker.get_memento(0))
    print(car)

    print("\nPrzywracanie stanu do Snap 2:")
    car.restore(caretaker.get_memento(1))
    print(car)
