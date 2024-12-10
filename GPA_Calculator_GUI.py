import tkinter as tk
from tkinter import messagebox
from GPA_Calculator import generate_class_inputs, calculate_gpa, to_csv



def generate_class_inputs():
    '''
    Acquires the inputs for how many classes, their grades in the classes, and what grade they are in.
    
    returns:
        A number of input boxes capable of taking all the grade inputs.
        
    '''
    # Clear any existing class input fields
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