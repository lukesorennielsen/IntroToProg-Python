from data_classes import Vehicle, Car, Motorcycle
from processing_classes import DataProcessor
from io_classes import ScreenIO

# Verifying data classes and proper wheel numbers
v = Vehicle("VehicleMake", "VehicleModel")
assert v.make == "VehicleMake"
assert v.model == "VehicleModel"
c = Car("Honda", "Accord")
assert c.make == "Honda"
assert c.model == "Accord"
assert c.wheels == 4
m = Motorcycle("Honda", "CB1000R")
assert m.make == "Honda"
assert m.model == "CB1000R"
assert m.wheels == 2
assert c.wheels != m.wheels

# Making sure the data processor works by adding a new vehicle to our inventory
inventory = []
DataProcessor.add_vehicle(("car", "Toyota", "Corolla"), inventory)
assert inventory[0].make == "Toyota"
assert inventory[0].model == "Corolla"
assert inventory[0].wheels == 4
DataProcessor.add_vehicle(("motorcycle", "Honda", "Gold Wing Tour"), inventory)
assert inventory[1].make == "Honda"
assert inventory[1].model == "Gold Wing Tour"
assert inventory[1].wheels == 2

# Checking that our vehicles are printed out
ScreenIO.show_inventory(inventory)

# Checking that we can get a new vehicle info and add it to our inventory
vehicle_info = ScreenIO.get_vehicle_info()
DataProcessor.add_vehicle(vehicle_info, inventory)
assert len(inventory) == 3
