from io_classes import ScreenIO as screen
from processing_classes import DataProcessor as dp

if __name__ == "__main__":
    user_input = None
    inventory = []
    while user_input != "x":
        screen.print_menu()
        user_input = screen.get_user_input()
        if user_input == "a":
            vehicle_info = screen.get_vehicle_info()
            dp.add_vehicle(vehicle_info, inventory)
        elif user_input == "s":
            screen.show_inventory(inventory)
