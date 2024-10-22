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
your_car.moves()

#more classes

class Airplane(Vehicle):
    def __init__(self, make, model,faa_id):
        # wont need this because its inherited
        # self.make = make
        # self.model = model

        super().__init__(make, model)
        self.faa_id = faa_id

        

    def moves(self):
        print("Flies along.")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along.")

class GolfCart(Vehicle):
    pass

cesna = Airplane("Cesna", "Skyhawk", "FA-12345")
mack = Truck("Caterpillar", "DAF")
cesna = Airplane("Yamaha", "DC100")

cesna.get_make_model()
cesna.moves()
print("")

mack.get_make_model()
mack.moves()
print("")

GolfCart.get_make_model()
GolfCart.moves()
print("")
        
