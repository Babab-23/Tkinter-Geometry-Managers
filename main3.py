import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        # Calculate age
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric date values.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Enter your Date of Birth", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Day").pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Label(root, text="Month").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Year").pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Button to calculate age
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run the application
root.mainloop()
