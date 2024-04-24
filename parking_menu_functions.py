from car_manager import TextCarManager

class Parking_menu_services:
    def parking_menu(self, car_manager):
        while True:
            print("\n1. Add a car")
            print("2. Remove a car")
            print("3. Show list of cars")
            print("4. Edit car information")
            print("5. Return to the main menu")
            choice = input("Select an action (1-5): ")
            if choice == '1':
                license_plate = input("Enter the car's license plate: ")
                brand = input("Enter the car's brand: ")
                car_manager.add_car(license_plate, brand)
            elif choice == '2':
                license_plate = input("Enter the car's license plate to remove: ")
                car_manager.remove_car(license_plate)
            elif choice == '3':
                car_manager.list_cars()
            elif choice == '4':
                old_license_plate = input("Enter the license plate number of the car to edit: ")
                new_license_plate = input("Enter the new license plate number of the car: ")
                brand = input("Enter the new brand of the car: ")
                car_manager.edit_car(old_license_plate, new_license_plate, brand)
            elif choice == '5':
                break
            else:
                print("Invalid input, please try again.")
