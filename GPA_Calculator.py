import csv, os
import tkinter as tk
from tkinter import messagebox


def generate_class_inputs():
    '''
    Acquires the inputs for how many classes, their grades in the classes, and what grade they are in.
    
    returns:
        A number of input boxes capable of taking all the grade inputs.
        
    '''
    # Clear any existing fields
    for widget in class_frame.winfo_children():
        widget.destroy()

    try:
        num_classes = int(num_classes_entry.get())
        if not (1 <= num_classes <= 8):
            raise ValueError("Number of classes must be between 1 and 8.")

        for i in range(num_classes):
            label = tk.Label(class_frame, text=f"Class {i + 1} Grade (%):")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(class_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry.insert(0, "0")
            grade_entries.append(entry)
    except ValueError:
        messagebox.showerror("Input Error", 'Please only input a digit between 1 and 12.')

def calculate_gpa():
    '''Calculate the GPA of a year of classes in school
    

    Grabs value from input box for the year of school
    
    Grabs values from input boxes for grabs in each class
    
    returns:
        GPA for the year

    '''
    try:
        year = grade_entry.get().strip()
        grades = []
        total_gpa = 0
        if not year.isdigit() or not (1 <= int(year) <= 12):
            raise ValueError("Year must be a number between 1 and 12.")
        
        
        for entry in grade_entries:
            grade = int(entry.get())
            if not (0 <= grade <= 130):
                raise ValueError("Grades must be between 0 and 130.")
            if grade >= 90:
                grades.append(4)
                total_gpa+=4
            elif grade >= 80 and grade < 90:
                grades.append(3)
                total_gpa+=3
            elif grade >= 70 and grade < 80:
                grades.append(2)
                total_gpa+=2
            elif grade >= 60 and grade < 70:
                grades.append(1)
                total_gpa+=1
            elif grade < 60:
                grades.append(0)
                total_gpa+=0
                

        if grades:
            gpa = total_gpa / len(grades)
            messagebox.showinfo("GPA Calculation", f"Your GPA for the year is: {gpa:.2f}")
            to_csv(year,gpa)
        else:
            raise ValueError("No grades entered.")

    except ValueError as f:
        messagebox.showerror("Input Error", str(f))
        
def to_csv(year, gpa):
    '''
    Grabs the year and GPA of that year and sends it to a csv file.
    
    returns:
        year, gpa to a file, after checking for duplicates and acting accordingly
    
    '''
    filename = 'gpafile.csv'
    existing_file_data = []
    is_fixed = False
    
    
    if os.path.exists(filename) == True:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            existing_file_data = list(reader)
    
    for i in existing_file_data:
        if i and i[0] == year:
            i[1] = gpa
            is_fixed = True
            break
    if is_fixed == False:
        existing_file_data.append([year, gpa])
        
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(existing_file_data)
    
    
    
def clear_all():
    '''
    Allows all boxes and progress to be wiped by pressing
    the clear button
    '''
    grade_entry.delete(0, tk.END)
    grade_entry.insert(0, "")
    num_classes_entry.delete(0, tk.END)
    num_classes_entry.insert(0, "")
    for widget in class_frame.winfo_children():
        widget.destroy()
    grade_entries.clear()

# Make the core window
root = tk.Tk()
root.title("GPA Calculator")
root.geometry("300x400")

# Boxes for year and num of classes
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Year of School (1-12):").grid(row=0, column=0, padx=5, pady=5)
grade_entry = tk.Entry(input_frame)
grade_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="# of Classes (1-8):").grid(row=1, column=0, padx=5, pady=5)
num_classes_entry = tk.Entry(input_frame)
num_classes_entry.grid(row=1, column=1, padx=5, pady=5)

# Frame for class text box input fields
class_frame = tk.Frame(root)
class_frame.pack(pady=10)

# class count, calculate, clear button things
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

grade_entries = []

generate_button = tk.Button(button_frame, text="Confirm Class Count", command=generate_class_inputs)
generate_button.pack(side=tk.LEFT, padx=10)

calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_gpa)
calculate_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_all)
clear_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()