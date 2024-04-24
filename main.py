from main_menu_functions import Main_menu_services
from parking_menu_functions import Parking_menu_services
from car_manager import CarManager

def main_menu():

    main_menu_methods = Main_menu_services()
    parking_menu_open = Parking_menu_services()

    while True:
        print("\n1. Create a parking space")
        print("2. Select a parking space")
        print("3. List all parking spaces")
        print("4. Delete a parking space")
        print("5. Search for a car by license plate")
        print("6. Exit the program")
        choice = input("Select an action (1-6): ")
        if choice == '1':
            main_menu_methods.create_parking()
        elif choice == '2':
            parking_name, car_manager = main_menu_methods.select_parking()
            if car_manager:
                parking_menu_open.parking_menu(car_manager)
        elif choice == '3':
            main_menu_methods.list_parkings()
        elif choice == '4':
            main_menu_methods.delete_parking()
        elif choice == '5':
            main_menu_methods.search_car()
        elif choice == '6':
            break
        else:
            print("Invalid input, please try again.")

if __name__ == '__main__':
    main_menu()
