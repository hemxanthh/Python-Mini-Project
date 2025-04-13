import tkinter as tk
from tkinter import messagebox

def launch_gui():
    root = tk.Tk()
    root.title("Bus Ticket Booking System")
    root.geometry("400x400")

    def gui_show_buses():
        info = ""
        for bus_id, info_dict in buses.items():
            info += f"{bus_id}: {info_dict['route']} | Fare: ₹{info_dict['fare']} | Seats: {info_dict['seats']}\n"
        messagebox.showinfo("Available Buses", info)

    def gui_book_ticket():
        bus_id = bus_id_entry.get().strip()
        name = name_entry.get().strip()
        try:
            tickets = int(ticket_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid ticket number.")
            return

        if bus_id not in buses:
            messagebox.showerror("Error", "Invalid Bus ID")
            return

        bus = buses[bus_id]
        if tickets > bus["seats"]:
            messagebox.showerror("Error", f"Only {bus['seats']} seats available.")
            return

        total = tickets * bus["fare"]
        buses[bus_id]["seats"] -= tickets

        messagebox.showinfo("Success",
            f"🎫 Ticket booked for {name}!\n"
            f"Route: {bus['route']}\n"
            f"Tickets: {tickets}\n"
            f"Total Fare: ₹{total}"
        )

    # GUI layout
    tk.Label(root, text="Bus ID:").pack()
    bus_id_entry = tk.Entry(root)
    bus_id_entry.pack()

    tk.Label(root, text="Your Name:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Number of Tickets:").pack()
    ticket_entry = tk.Entry(root)
    ticket_entry.pack()

    tk.Button(root, text="Book Ticket", command=gui_book_ticket).pack(pady=10)
    tk.Button(root, text="View Buses", command=gui_show_buses).pack(pady=5)

    root.mainloop()
import tkinter as tk
from tkinter import messagebox

def launch_gui():
    root = tk.Tk()
    root.title("Bus Ticket Booking System")
    root.geometry("400x400")

    def gui_show_buses():
        info = ""
        for bus_id, info_dict in buses.items():
            info += f"{bus_id}: {info_dict['route']} | Fare: ₹{info_dict['fare']} | Seats: {info_dict['seats']}\n"
        messagebox.showinfo("Available Buses", info)

    def gui_book_ticket():
        bus_id = bus_id_entry.get().strip()
        name = name_entry.get().strip()
        try:
            tickets = int(ticket_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid ticket number.")
            return

        if bus_id not in buses:
            messagebox.showerror("Error", "Invalid Bus ID")
            return

        bus = buses[bus_id]
        if tickets > bus["seats"]:
            messagebox.showerror("Error", f"Only {bus['seats']} seats available.")
            return

        total = tickets * bus["fare"]
        buses[bus_id]["seats"] -= tickets

        messagebox.showinfo("Success",
            f"🎫 Ticket booked for {name}!\n"
            f"Route: {bus['route']}\n"
            f"Tickets: {tickets}\n"
            f"Total Fare: ₹{total}"
        )

    # GUI layout
    tk.Label(root, text="Bus ID:").pack()
    bus_id_entry = tk.Entry(root)
    bus_id_entry.pack()

    tk.Label(root, text="Your Name:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Number of Tickets:").pack()
    ticket_entry = tk.Entry(root)
    ticket_entry.pack()

    tk.Button(root, text="Book Ticket", command=gui_book_ticket).pack(pady=10)
    tk.Button(root, text="View Buses", command=gui_show_buses).pack(pady=5)

    root.mainloop()
