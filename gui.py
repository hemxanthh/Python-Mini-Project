import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

buses = {
    "600F": {"route": "Electronic city to Banashankari", "fare": 120, "seats": 40},
    "410FA": {"route": "Kengeri To Yashwantpur", "fare": 100, "seats": 40},
    "80G": {"route": "Majestic to Laggere Bridge", "fare": 150, "seats": 40},
    "96G": {"route": "Majestic to Silk Board", "fare": 150, "seats": 40},
}

def book_ticket():
    bus_id = bus_id_entry.get()
    name = name_entry.get()
    try:
        age = int(age_entry.get())
        tickets = int(ticket_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid age and ticket number.")
        return

    if bus_id not in buses:
        messagebox.showerror("Error", "Invalid Bus ID")
        return

    bus = buses[bus_id]
    if tickets > bus["seats"]:
        messagebox.showerror("Error", f"Only {bus['seats']} seats available.")
        return

    # Apply discount
    fare = bus["fare"] * tickets
    if age >= 60:
        fare = int(fare * 0.4)  # 60% discount
        discount_note = " (60% Senior Discount Applied)"
    else:
        discount_note = ""

    # Update seat count
    buses[bus_id]["seats"] -= tickets

    # Calculate ETA
    start_time = datetime.strptime(bus["start_time"], "%H:%M")
    eta = (start_time + timedelta(hours=bus["duration"])).strftime("%H:%M")

    msg = (
        f"Ticket Booked for {name}!\n\n"
        f"Route: {bus['source']} to {bus['destination']}\n"
        f"Start Time: {bus['start_time']} | ETA: {eta}\n"
        f"Tickets: {tickets}\n"
        f"Total Fare: ₹{fare}{discount_note}"
    )
    messagebox.showinfo("Success", msg)

# Show buses function
def show_buses():
    info = ""
    for bid, bus in buses.items():
        info += f"Bus {bid}: {bus['route']} | Fare: ₹{bus['fare']} | Seats: {bus['seats']}\n"
    messagebox.showinfo("Available Buses", info)

# GUI Setup
root = tk.Tk()
root.title("Bus Ticket Booking System")
root.geometry("400x350")

tk.Label(root, text="Bus ID:").pack()
bus_id_entry = tk.Entry(root)
bus_id_entry.pack()

tk.Label(root, text="Your Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Your Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Number of Tickets:").pack()
ticket_entry = tk.Entry(root)
ticket_entry.pack()

tk.Button(root, text="Book Ticket", command=book_ticket).pack(pady=10)
tk.Button(root, text="View Available Buses", command=show_buses).pack()

root.mainloop()
