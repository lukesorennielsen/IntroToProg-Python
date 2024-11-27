class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 2

    def to_row(self):
        return f"motorcycle,{self.make},{self.model}\n"

    def __str__(self):
        return f"Motorcycle of make {self.make} and model {self.model}"


class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 4

    def to_row(self):
        return f"car,{self.make},{self.model}\n"

    def __str__(self):
        return f"Car of make {self.make} and model {self.model}"


if __name__ == "__main__":
    raise Exception("This class in not meant to be run")
