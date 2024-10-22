# A class is a blueprint for creating objects
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    # method that uses the properties
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

# Objects
my_car = Vehicle("Tesla", "Model 3")

print(my_car.make)
print("")

print(my_car.model)
print("")

my_car.moves()
print("")

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves();