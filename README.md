# 📦 Package Delivery Pathfinding Algorithm
Package delivery pathfinding program that utilizes the nearest neighbor algorithm and hash table data structure.

# ❓ Scenario

Starlight Industries Delivery Service (SIDS) is facing challenges with consistent on-time package deliveries for their Daily Local Deliveries (DLD). The Celestial City DLD route operates with three trucks, two drivers, and typically handles 40 packages daily. Each package comes with specific criteria and delivery requirements.

Your task is to develop an optimal route and delivery distribution solution. You need to create an algorithm, implement it in code, and present a solution where all 40 packages are delivered on time while minimizing the total mileage across all trucks. Delivery locations are marked on the "addresses.csv" and inter-location distances are provided in the "distances.csv".

Key considerations:
- Adhere to specific delivery times for each package.
- Account for potential real-time changes in delivery requirements.
- Enable supervisors to track delivery progress of any package and the corresponding package details.
- Design the solution to be adaptable for use in multiple cities where Starlight Industries operates.

# 💭 Assumptions

1. Truck capacity: Maximum 16 packages per truck.
2. Average speed: Trucks travel at 18 miles per hour.
3. Fuel: Trucks have unlimited fuel and don't need to stop for refueling.
4. Drivers: Each driver remains with the same truck throughout its service.
5. Operating hours: Drivers depart from the hub at 8:00 a.m. with loaded trucks. They can return to the hub for more packages if needed. The workday ends when all 40 packages are delivered.
6. Delivery time: Package delivery is instantaneous (factored into the average truck speed).
7. Package notes: Each package may have up to one special note.
8. Address correction: The incorrect delivery address for package #9 (Maplewood Juvenile Court) will be updated at 10:20 a.m. The correct address is 7845 Justice Lane, Maplewood, FZ 28111.
9. Package ID: Each package has a unique ID with no collisions.
10. No additional assumptions are permitted.

# 📝 Requirements

A. Identify the algorithm that will be used to create a program to deliver the packages and meets all requirements specified in the scenario.

B. Write a core algorithm overview, using the sample given, in which you do the following:

    1. Comment using pseudocode to show the logic of the algorithm applied to this software solution.
    2. Apply programming models to the scenario.
    3. Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
    4. Discuss the ability of your solution to adapt to a changing market and to scalability.
    5. Discuss the efficiency and maintainability of the software.
    6. Discuss the self-adjusting data structures chosen and their strengths and weaknesses based on the scenario.

C. Write an original code to solve and to meet the requirements of lowest mileage usage and having all packages delivered on time.

    1. Create a comment within the first line of your code that includes your first name, last name, and student ID.
    2. Include comments at each block of code to explain the process and flow of the coding.

D. Identify a data structure that can be used with your chosen algorithm to store the package data.

    1. Explain how your data structure includes the relationship between the data points you are storing.

    Note: Do NOT use any existing data structures. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment.

E. Develop a hash table, without using any additional libraries or classes, with an insertion function that takes the following components as input and inserts the components into the hash table:

    • package ID number
    • delivery address
    • delivery deadline
    • delivery city
    • delivery zip code
    • package weight
    • delivery status (e.g., delivered, in route)

F. Develop a look-up function that takes the following components as input and returns the corresponding data elements:

    • package ID number
    • delivery address
    • delivery deadline
    • delivery city
    • delivery zip code
    • package weight
    • delivery status (e.g., delivered, in route)

G. Provide an interface for the insert and look-up functions to view the status of any package at any time. This function should return all information about each package, including delivery status.

# 🔎 Output Preview
![terminal_preview](https://github.com/drewmarsh/package-delivery-pathfinding-algorithm/assets/78824781/1cff66d0-a264-4724-ac7a-7cbb711fc6bb)

