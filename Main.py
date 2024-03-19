import csv
import datetime
from Truck import Truck
from Package import Package
from HashTable import HashTable
from Style import Style

# Initialize the snapshot dictionary
snapshots = {}

# Fill hash table with package information
packages_hashtable = HashTable()
with open('packages.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for package in readCSV:
            packID = int(package[0])
            packAddress = package[1]
            packCity = package[2]
            packState = package[3]
            packZip  = package[4]
            packDeadline = package[5]
            packWeightKilos = package[6]
            packPhase = Style.set_style("HUB", Style.RED)

            pack = Package(packID, packAddress, packCity, packState, packZip, packDeadline, packWeightKilos, packPhase)
            packages_hashtable.insert(packID, pack)

    Style.print_seperator()

# Create objects for all three trucks
# Parameters: capacity, speed, load, packages, mileage, address, depart_time, number, is_finished, time_spent
truck1 = Truck(16, 18, None, [29, 20, 22, 34, 14, 16, 40, 31, 1, 13, 15, 19, 21, 33, 24, 26], 0.0, "2587 Celestial Way",
                     datetime.timedelta(hours=8), 1, False, 0)
truck2 = Truck(16, 18, None, [39, 23, 36, 38, 18, 3, 37, 30, 35, 27], 0.0,
                     "2587 Celestial Way", datetime.timedelta(hours=8), 2, False, 0)
truck3 = Truck(16, 18, None, [7, 10, 12, 4, 17, 8, 32, 2, 5, 28, 9, 11, 25, 6], 0.0, "2587 Celestial Way",
                     datetime.timedelta(hours=9, minutes=32, seconds=41), 3, False, 0)

# Calculate the distance between two points
def calculate_distance(x, y):
        with open('distances.csv', 'r') as file:
                readCSV = list(csv.reader(file))
                distance = readCSV[x][y]
                # Check if distance is an empty string
                if distance == '':
                        # Swap x and y and try again
                        x, y = y, x
                        distance = readCSV[x][y]
                return float(distance)

# Determine how long it will take for a truck to travel a given distance
def calculate_delivery_time(Truck, distance):
        return distance / Truck.speed

# Return the address index from a given address string
def get_address(address):
    with open('addresses.csv', 'r') as file:
        readCSV = list(csv.reader(file))
        for row in readCSV:
            if address in row[2]:
                return int(row[0])
        # If address is not found, print an error message and return None
        print(f"Error: Address '{address}' not found in the CSV file.")
        return None

# Print current package information1
# Utilizes the style class to make the output more readable
def print_package_status(package, current_time):
    print(f"\tPackage {Style.set_style(package.ID, Style.PINK)} is {Style.set_style(package.phase, Style.RED)}"
            f" at {Style.format_time_string(current_time)}")

# Function to find the nearest time in snapshots
def find_nearest_time(user_datetime, snapshots):
    while user_datetime not in snapshots:
        user_datetime -= datetime.timedelta(seconds=1)
    return user_datetime

# Validate the entered time format and ensure it is at least 08:00:00
def validate_time(user_time):
    try:
        (h, m, s) = user_time.split(":")
        user_datetime = datetime.datetime(2023, 1, 1, int(h), int(m), int(s))
        if user_datetime.time() < datetime.time(8, 0, 0):
            raise ValueError("Entered time should be later than 07:59:59 because the first truck doesn't leave until 08:00:00")
        return user_datetime
    except ValueError as e:
        print(f"Invalid time format or {e}. Please enter a valid time.")
        exit()

def delivery(truck, packages_hashtable, snapshots):
    current_location = get_address(truck.address)
    total_delivery_time = 0
    # Control what time each Truck leaves the HUB. If they all leave at seperate times, the time lookup can have an easier implementation
    # This makes the time optimization poor, but the total mileage isn't effected
    if truck.number == 1:
        current_time = datetime.datetime(2023, 1, 1, 8, 0, 0)  # Truck 1 leaves @ 08:00:00 am
    if truck.number == 2:
        current_time = datetime.datetime(2023, 1, 1, 8, 0, 0)  # Truck 2 leaves @ 08:00:00 am
    if truck.number == 3:
        current_time = datetime.datetime(2023, 1, 1, 9, 32, 41)  # Truck 3 leaves @ 09:32:41 am

    print(f"TRUCK {truck.number} STATS:\n")

    while truck.packages:
        # Print which packages are being loaded onto each truck
        # This isn't part of the assignment requirements, I just thought it would look nice
        if current_location == 0:
            all_packages = ""  # Initialize as an empty string
            for index, package_id in enumerate(truck.packages):
                package = packages_hashtable.search(package_id)
                package.phase = Style.set_style("EN ROUTE", Style.ORANGE) # Set phase to EN ROUTE when the package is on the truck
                # Give the package an assigned truck
                assigned_truck_str = "Assigned truck: " + truck.get_number_string()
                package.assigned_truck = Style.set_style(assigned_truck_str, Style.YELLOW)

                # Add a comma and space if not the last package
                if index < len(truck.packages) - 1:
                    all_packages += Style.set_style(str(package_id), Style.PINK) + ", "
                else:
                    # Use "and" before the last package
                    all_packages += "and " + Style.set_style(str(package_id), Style.PINK)

            print(f"\tLoaded packages {all_packages} onto Truck {truck.number}\n")

            # Add a snapshot to the dictionary after packages become "EN ROUTE" (the key being the current time)
            snapshots[current_time] = {pkg_id: packages_hashtable.search(pkg_id).clone() for pkg_id in range(1, 41)}

        # Initialize an empty array for the distances
        distances = []

        for package_id in truck.packages:
            package = packages_hashtable.search(package_id)
            package_location = get_address(package.address)
            distance = calculate_distance(current_location, package_location)
            distances.append(distance)

        min_distance = min(distances)
        nearest_package_id = truck.packages[distances.index(min_distance)]

        # Retrieve the actual package object using the ID
        nearest_package = packages_hashtable.search(nearest_package_id)

        # Update current time
        current_time += datetime.timedelta(hours=calculate_delivery_time(truck, min_distance))

        # After 10:20:00 am, update the incorrect address/zip of package 9 before delivery
        # After package 12 is delivered, the time will be past 10:20:00 am and the driver can then focus on updating the address
        if nearest_package_id == 12:
            package = packages_hashtable.search(9)
            package.address = "7845 Justice Lane"
            package.zip = 28111
            package_number = Style.set_style("9", Style.PINK)
            print(f"\n\tPackage {package_number}'s incorrect address/zip has been updated appropriately!\n")

        # Update total delivery time
        total_delivery_time += calculate_delivery_time(truck, min_distance)

        # Update package status to "DELIVERED"
        nearest_package.phase = Style.set_style("DELIVERED", Style.GREEN)
        nearest_package.delivery_time = current_time

        # Add a snapshot to the dictionary after delivery (the key being the current time)
        snapshots[current_time] = {pkg_id: packages_hashtable.search(pkg_id).clone() for pkg_id in range(1, 41)}
        
        # Print package status after delivery
        print_package_status(nearest_package, current_time)

        # Update truck mileage
        truck.update_mileage(min_distance)

        # Update current location to the location of the last delivered package
        current_location = get_address(nearest_package.address)

        # Remove the delivered package from the truck's list
        truck.packages = [pkg_id for pkg_id in truck.packages if pkg_id != nearest_package_id]

        # Check if it's the last package and update mileage and time accordingly
        if not truck.packages:
            HUB_return_distance = calculate_distance(current_location, get_address("2587 Celestial Way"))
            truck.update_mileage(HUB_return_distance) # Update mileage
            current_time += datetime.timedelta(hours=calculate_delivery_time(truck, HUB_return_distance)) # Update current time
            # Update total delivery time
            total_delivery_time += calculate_delivery_time(truck, HUB_return_distance)
            truck.time_spent += total_delivery_time
            truck.is_finished = True
            red_HUB = Style.set_style("HUB", Style.RED)
            print(f"\n\tTruck {truck.number} has returned to the {red_HUB} for the day at {Style.format_time_string(current_time)}!")
    print()
    print(f"\tTruck {truck.number} mileage: {round(truck.mileage, 2)} miles\n")
    print(f"\tTruck {truck.number} time: {round(total_delivery_time, 2)} hours\n")

while True:
    # Prompt the user for input
    first_user_choice = input("CHOOSE ONE OF THE FOLLOWING: \n\n\t1. Start delivery simulation and package lookup \n\t2. Quit program \n\n" + Style.set_style("\tChoice: ", Style.ITALIC))

    # Check user input and perform corresponding action
    if first_user_choice == '1':
        Style.print_seperator()
        print()
        snapshots = {}

        # Truck 1 leaves right away
        delivery(truck1, packages_hashtable, snapshots)
        # Only let truck 2 leave the hub if truck 1 has finished their route
        if truck1.is_finished == True:
            delivery(truck2, packages_hashtable, snapshots)
        # Only let truck 3 leave the hub if the other two trucks have finished their route
        if truck1.is_finished == True and truck2.is_finished == True:
            delivery(truck3, packages_hashtable, snapshots)
        
        # Print total MILEAGE and TIME information for all trucks combined
        Style.print_seperator()
        print("TOTAL MILEAGE:")
        print("\n\t" + Style.set_style(round(truck1.mileage + truck2.mileage + truck3.mileage, 2), Style.UNDERLINE) + " miles")
        print("\nTOTAL TIME:")
        print("\n\t" + Style.set_style(round(truck1.time_spent + truck2.time_spent + truck3.time_spent, 2), Style.UNDERLINE) + " hours")
        Style.print_seperator()

        # Ask the user for a specific time for the lookup
        user_time = input("Enter a time to lookup the status of package(s). HH:MM:SS is the format: ")
        user_datetime = validate_time(user_time)
        (h, m, s) = user_time.split(":")

        # Convert user input to datetime
        user_datetime = datetime.datetime(2023, 1, 1, int(h), int(m), int(s))
        user_datetime_pre_snapshot = user_datetime # Save this value for future printing before it is updated in the next line

        # Find the nearest time in snapshots
        user_datetime = find_nearest_time(user_datetime, snapshots)

        # The user will be asked if they want to see the status of all packages or only one
        second_user_choice = input("\nCHOOSE ONE OF THE FOLLOWING: \n\n\t1. Single package lookup \n\t2. All packages lookup \n\n" + Style.set_style("\tChoice: ", Style.ITALIC))
        Style.print_seperator()

        # If the user chooses 1, they will need to enter a package ID
        if second_user_choice == '1':
            try:
                ID_input = input("Enter package ID (1-40): ")
                print()
                package_id = int(ID_input)
                # Print package information for a single package
                print(f"Here is the package information at {Style.format_time_string(user_datetime_pre_snapshot)}\n")
                if user_datetime in snapshots and package_id in snapshots[user_datetime]:
                    package = snapshots[user_datetime][package_id]
                    print(str(package))

            except ValueError:
                print("Entry invalid. Closing program.")
                exit()

        # If the user chooses 2, all package information will be printed
        elif second_user_choice == '2':
            # Print package information for all packages
            print(f"Here is the information for all packages at {Style.format_time_string(user_datetime_pre_snapshot)}\n")
            try:
                if user_datetime in snapshots:
                    for package_id in range(1, 41):
                        if package_id in snapshots[user_datetime]:
                            package = snapshots[user_datetime][package_id]
                            print(str(package))
                            # The line below makes the output a lot more readable. It is only commented out so that I can fit all look-up info in a single screenshot
                            # if package_id is not 40: print() # The last package doesn't need a blank line after it

            except ValueError:
                print("Entry invalid. Closing program.")
                exit()

        Style.print_seperator()
        break  # Exit the loop after successful simulation

    elif first_user_choice == '2':
        Style.print_seperator()
        break  # Exit the loop when the user wants to 'Quit program'

    else:
        print("\nInvalid input. Please enter 's' to start the simulation or 'q' to quit.\n") # Notify the user of input validation requirements