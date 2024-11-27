import vehicle


class Motorcycle(vehicle.Vehicle):
    def __init__(self, make, model):
        # We must call the initializer of the super class
        super().__init__(make, model)
        # Set the number of wheels to 2
        self.wheels = 2
