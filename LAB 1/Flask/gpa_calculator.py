import tkinter as tk
from tkinter import messagebox

# Function to convert marks to grade points
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

# Function to calculate GPA and CGPA
def calculate_gpa_cgpa():
    try:
        # Get values from entries
        courses = [entry_courses[i].get() for i in range(4)]
        credit_hours = [int(entry_credits[i].get()) for i in range(4)]
        marks = [float(entry_marks[i].get()) for i in range(4)]
        
        # Calculate GPA
        total_points = 0
        total_credits = sum(credit_hours)
        for i in range(4):
            gp = marks_to_gp(marks[i])
            total_points += gp * credit_hours[i]
        gpa = total_points / total_credits
        
        # Ask user for previous GPA and credit hours
        prev_gpa = float(prev_gpa_entry.get())
        prev_cr_hours = float(prev_cr_entry.get())
        
        cgpa = ((prev_gpa * prev_cr_hours) + (gpa * total_credits)) / (prev_cr_hours + total_credits)
        
        # Show results
        messagebox.showinfo("Result", f"GPA: {round(gpa,2)}\nCGPA: {round(cgpa,2)}")
    except Exception as e:
        messagebox.showerror("Error", "Please enter valid numbers for all fields.")

# Create main window
root = tk.Tk()
root.title("GPA & CGPA Calculator")

# Course inputs
tk.Label(root, text="Course Name").grid(row=0, column=0)
tk.Label(root, text="Credit Hours").grid(row=0, column=1)
tk.Label(root, text="Obtained Marks").grid(row=0, column=2)

entry_courses = []
entry_credits = []
entry_marks = []

for i in range(4):
    e_course = tk.Entry(root)
    e_course.grid(row=i+1, column=0)
    entry_courses.append(e_course)
    
    e_credit = tk.Entry(root)
    e_credit.grid(row=i+1, column=1)
    entry_credits.append(e_credit)
    
    e_mark = tk.Entry(root)
    e_mark.grid(row=i+1, column=2)
    entry_marks.append(e_mark)

# Previous GPA and Credit Hours
tk.Label(root, text="Previous GPA:").grid(row=5, column=0)
prev_gpa_entry = tk.Entry(root)
prev_gpa_entry.grid(row=5, column=1)

tk.Label(root, text="Previous Credit Hours:").grid(row=6, column=0)
prev_cr_entry = tk.Entry(root)
prev_cr_entry.grid(row=6, column=1)

# Calculate button
calculate_btn = tk.Button(root, text="Calculate GPA & CGPA", command=calculate_gpa_cgpa)
calculate_btn.grid(row=7, column=0, columnspan=3, pady=10)

# Run the GUI loop
root.mainloop()
