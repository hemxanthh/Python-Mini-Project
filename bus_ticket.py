# Coolified Bus Ticket System with Colors, Tables, Emojis, and Senior Discount

from colorama import Fore, Style, init
from tabulate import tabulate
import pyfiglet
import time

init(autoreset=True)

buses = {
    "600F": {"route": "Electronic city to Banashankari", "fare": 120, "seats": 40},
    "410FA": {"route": "Kengeri To Yashwantpur", "fare": 100, "seats": 40},
    "80G": {"route": "Majestic to Laggere Bridge", "fare": 150, "seats": 40},
    "96G": {"route": "Majestic to Silk Board", "fare": 150, "seats": 40},
}
3
ADMIN_PASSWORD = "pythonproject"


def loading_effect():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")


def show_banner():
    banner = pyfiglet.figlet_format("Bus Booking")
    print(Fore.CYAN + banner)


def show_buses():
    print(Fore.YELLOW + "\n🚌 Available Buses:\n")
    table = []
    for bus_id, info in buses.items():
        table.append([bus_id, info['route'], f"₹{info['fare']}", info['seats']])
    headers = ["Bus ID", "Route", "Fare", "Seats"]
    print(tabulate(table, headers, tablefmt="fancy_grid"))


def book_ticket():
    bus_id = input(Fore.CYAN + "Enter Bus ID to book: ").strip()
    if bus_id not in buses:
        print(Fore.RED + "Invalid Bus ID. Please try again.")
        return

    name = input(Fore.CYAN + "Enter your name: ").strip()
    try:
        age = int(input(Fore.CYAN + "Enter your age: "))
        num_tickets = int(input(Fore.CYAN + "Enter number of tickets: "))
    except ValueError:
        print(Fore.RED + "Invalid input. Booking cancelled.")
        return

    available_seats = buses[bus_id]['seats']
    if num_tickets > available_seats:
        print(Fore.RED + f"Only {available_seats} seats available. Try booking fewer tickets.")
        return

    base_fare = buses[bus_id]['fare'] * num_tickets
    discount = 0.6 if age >= 60 else 0
    total_fare = int(base_fare * (1 - discount))
    buses[bus_id]['seats'] -= num_tickets

    loading_effect()
    print(Fore.GREEN + "\n🎟️ Ticket Booked Successfully!")
    print(Fore.BLUE + "-" * 40)
    print(Fore.CYAN + f"Passenger Name : {name}")
    print(Fore.CYAN + f"Bus ID         : {bus_id}")
    print(Fore.CYAN + f"Route          : {buses[bus_id]['route']}")
    print(Fore.CYAN + f"Tickets Booked : {num_tickets}")
    if discount:
        print(Fore.MAGENTA + "👴 Senior Citizen Discount Applied (60%)")
    print(Fore.CYAN + f"Total Fare     : ₹{total_fare}")
    print(Fore.BLUE + "-" * 40)


# ===== ADMIN PANEL =====

def admin_login():
    password = input(Fore.YELLOW + "Enter admin password: ")
    return password == ADMIN_PASSWORD


def add_bus():
    bus_id = input("Enter new Bus ID: ").strip()
    if bus_id in buses:
        print(Fore.RED + "Bus ID already exists.")
        return
    route = input("Enter route (e.g., City A to City B): ").strip()
    try:
        fare = int(input("Enter fare (₹): "))
        seats = int(input("Enter number of seats: "))
    except ValueError:
        print(Fore.RED + "Invalid input. Bus not added.")
        return

    buses[bus_id] = {"route": route, "fare": fare, "seats": seats}
    print(Fore.GREEN + f"✅ Bus {bus_id} added successfully!")


def edit_bus():
    bus_id = input("Enter Bus ID to edit: ").strip()
    if bus_id not in buses:
        print(Fore.RED + "Bus ID not found.")
        return

    print(f"Current Info: {buses[bus_id]}")
    try:
        new_fare = int(input("Enter new fare: "))
        new_seats = int(input("Enter new number of seats: "))
        buses[bus_id]["fare"] = new_fare
        buses[bus_id]["seats"] = new_seats
        print(Fore.GREEN + "✅ Bus details updated.")
    except ValueError:
        print(Fore.RED + "Invalid input.")


def delete_bus():
    bus_id = input("Enter Bus ID to delete: ").strip()
    if bus_id in buses:
        del buses[bus_id]
        print(Fore.GREEN + f"✅ Bus {bus_id} deleted.")
    else:
        print(Fore.RED + "Bus ID not found.")


def admin_panel():
    if not admin_login():
        print(Fore.RED + "❌ Access Denied. Incorrect password.")
        return

    while True:
        print(Fore.YELLOW + "\n--- Admin Panel ---")
        print("1. View All Buses")
        print("2. Add Bus")
        print("3. Edit Bus")
        print("4. Delete Bus")
        print("5. Exit Admin Panel")

        choice = input("Enter your choice: ")
        if choice == '1':
            show_buses()
        elif choice == '2':
            add_bus()
        elif choice == '3':
            edit_bus()
        elif choice == '4':
            delete_bus()
        elif choice == '5':
            break
        else:
            print(Fore.RED + "Invalid option.")


# ===== MAIN MENU =====

def main():
    show_banner()
    while True:
        print(Fore.YELLOW + "\n=== Main Menu ===")
        print("1. View Available Buses")
        print("2. Book Ticket")
        print("3. Admin Panel")
        print("4. Exit")
        choice = input(Fore.CYAN + "Enter your choice (1-4): ")

        if choice == '1':
            show_buses()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            admin_panel()
        elif choice == '4':
            print(Fore.GREEN + "\nThank you for using the Bus Ticket Booking System! 👋")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
