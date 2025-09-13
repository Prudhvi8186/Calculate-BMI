import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt

DATA_FILE = "bmi_data.csv"


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi():
    try:
        username = username_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not username:
            raise ValueError("Username cannot be empty.")
        if weight <= 0 or height <= 0:
            raise ValueError("Positive numbers only.")

        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        save_data(username, bmi)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


def save_data(username, bmi):
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, f"{bmi:.2f}"])


def show_graph():
    if not os.path.exists(DATA_FILE):
        messagebox.showerror("Error", "No data found.")
        return
    
    username = username_entry.get().strip()
    bmis = []
    
    with open(DATA_FILE) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                bmis.append(float(row[1]))
    
    if bmis:
        plt.plot(range(1, len(bmis) + 1), bmis, marker="o", linestyle="-", color="b")
        plt.title(f"{username}'s BMI Trend")
        plt.xlabel("Entry Number")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("No Data", "No entries for this user.")


root = tk.Tk()
root.title("BMI Calculator with History")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Height (m):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Show Graph", command=show_graph).grid(row=4, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
