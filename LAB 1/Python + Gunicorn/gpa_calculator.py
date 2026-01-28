import tkinter as tk
from tkinter import messagebox

# Functions
def marks_to_gp(marks):
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 60:
        return 2.3
    elif marks >= 55:
        return 2.0
    elif marks >= 50:
        return 1.7
    else:
        return 0.0

def calculate_gpa():
    try:
        marks = [int(entry_marks[i].get()) for i in range(4)]
        credits = [int(entry_credits[i].get()) for i in range(4)]
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for marks and credit hours")
        return

    total_points = sum([marks_to_gp(marks[i]) * credits[i] for i in range(4)])
    total_credits = sum(credits)
    gpa = total_points / total_credits

    lbl_gpa_result.config(text=f"GPA: {gpa:.2f}")

def calculate_cgpa():
    try:
        prev_gpa_val = float(entry_prev_gpa.get())
        prev_cr_val = int(entry_prev_cr.get())
        current_gpa_val = float(entry_current_gpa.get())
        current_cr_val = int(entry_current_cr.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for previous/current GPA and credit hours")
        return

    cgpa = ((prev_gpa_val * prev_cr_val) + (current_gpa_val * current_cr_val)) / (prev_cr_val + current_cr_val)
    lbl_cgpa_result.config(text=f"CGPA: {cgpa:.2f}")

# GUI Setup
root = tk.Tk()
root.title("GPA & CGPA Calculator")
root.geometry("500x500")

# Course Input Labels
tk.Label(root, text="Courses:").grid(row=0, column=0, pady=5)
course_names = ["DS", "AI", "DB", "IS"]
entry_credits = []
entry_marks = []

# Credits and Marks Input
for i, course in enumerate(course_names):
    tk.Label(root, text=f"{course} Credit Hours:").grid(row=i+1, column=0, padx=5, pady=5, sticky='e')
    cr_entry = tk.Entry(root, width=5)
    cr_entry.grid(row=i+1, column=1, padx=5, pady=5)
    entry_credits.append(cr_entry)

    tk.Label(root, text=f"{course} Marks:").grid(row=i+1, column=2, padx=5, pady=5, sticky='e')
    mark_entry = tk.Entry(root, width=5)
    mark_entry.grid(row=i+1, column=3, padx=5, pady=5)
    entry_marks.append(mark_entry)

# GPA Button
btn_gpa = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
btn_gpa.grid(row=5, column=0, columnspan=2, pady=10)
lbl_gpa_result = tk.Label(root, text="GPA: ")
lbl_gpa_result.grid(row=5, column=2, columnspan=2)

# Previous and Current GPA/CR Inputs for CGPA
tk.Label(root, text="Previous GPA:").grid(row=6, column=0, pady=5)
entry_prev_gpa = tk.Entry(root, width=5)
entry_prev_gpa.grid(row=6, column=1)

tk.Label(root, text="Previous Credit Hours:").grid(row=6, column=2)
entry_prev_cr = tk.Entry(root, width=5)
entry_prev_cr.grid(row=6, column=3)

tk.Label(root, text="Current GPA:").grid(row=7, column=0, pady=5)
entry_current_gpa = tk.Entry(root, width=5)
entry_current_gpa.grid(row=7, column=1)

tk.Label(root, text="Current Credit Hours:").grid(row=7, column=2)
entry_current_cr = tk.Entry(root, width=5)
entry_current_cr.grid(row=7, column=3)

# CGPA Button
btn_cgpa = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa)
btn_cgpa.grid(row=8, column=0, columnspan=2, pady=10)
lbl_cgpa_result = tk.Label(root, text="CGPA: ")
lbl_cgpa_result.grid(row=8, column=2, columnspan=2)

root.mainloop()
