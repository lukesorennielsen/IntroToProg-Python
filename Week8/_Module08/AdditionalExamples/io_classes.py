from data_classes import Car, Motorcycle


class FileIO:
    @staticmethod
    def load_inventory(file_name):
        inventory = []
        with open(file_name, "r") as file:
            for line in file:
                line.strip().split(",")
                if line[0] == "car":
                    inventory.append(Car(line[1], line[2]))
                elif line[0] == "motorcycle":
                    inventory.append(Motorcycle(line[1], line[2]))
                else:
                    print(f"Unknown type {line[0]}, skipping...")
        return inventory

    @staticmethod
    def save_inventory(file_name, vehicles):
        with open(file_name, "w") as file:
            for vehicle in vehicles:
                file.write(vehicle.write_row())
        return vehicles


class ScreenIO:
    @staticmethod
    def show_inventory(inventory):
        for vehicle in inventory:
            print(vehicle)

    @staticmethod
    def get_vehicle_info():
        vehicle_type = input("Which vehicle type? [car/motorcycle] ")
        make = input("Which make? ")
        model = input("Which model? ")
        return vehicle_type, make, model

    @staticmethod
    def print_menu():
        print("x to exit\n" "a to add a vehicle\n" "s to show inventory\n")

    @staticmethod
    def get_user_input():
        return input("Please input an option: ")


if __name__ == "__main__":
    raise Exception("This class in not meant to be run")
