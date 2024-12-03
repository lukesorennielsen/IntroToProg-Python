from data_classes import Car, Motorcycle


class DataProcessor:
    @staticmethod
    def add_vehicle(vehicle_info, inventory):
        vehicle_type = vehicle_info[0]
        make = vehicle_info[1]
        model = vehicle_info[2]
        if vehicle_type == "car":
            inventory.append(Car(make, model))
        elif vehicle_type == "motorcycle":
            inventory.append(Motorcycle(make, model))
        else:
            raise Exception("Unknown vehicle type")


if __name__ == "__main__":
    raise Exception("This class in not meant to be run")
