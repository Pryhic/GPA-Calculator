import csv, os
import tkinter as tk
from tkinter import Frame, Entry, Label, messagebox



def calculate_gpa(year: str, grades: list[str]) -> float:
    '''Calculate the GPA of a year of classes in school
    

    Grabs value from input box for the year of school
    
    Grabs values from input boxes for grabs in each class
    
    returns:
        GPA for the year

    '''
 
    if not year.isdigit() or not (1 <= int(year) <= 12):
        raise ValueError("Year must be a number between 1 and 12.")
    
    gpa_list = []
    total_gpa = 0
        
    for grade in grades:
        grade = int(grade)
        if not (0 <= grade <= 130):
            raise ValueError("Grades must be between 0 and 130.")
        if grade >= 90:
            gpa_list.append(4)
            total_gpa+=4
        elif grade >= 80 and grade < 90:
            gpa_list.append(3)
            total_gpa+=3
        elif grade >= 70 and grade < 80:
            gpa_list.append(2)
            total_gpa+=2
        elif grade >= 60 and grade < 70:
            gpa_list.append(1)
            total_gpa+=1
        elif grade < 60:
            gpa_list.append(0)
            total_gpa+=0
            
                

    if gpa_list:
        return round(total_gpa/len(gpa_list), 2)
    else:
        raise ValueError("No grades entered.")
        
def to_csv(year: str, gpa: float)-> None:
    '''
    Grabs the year and GPA of that year and sends it to a csv file.
    
    returns:
        year, gpa to a file, after checking for duplicates and acting accordingly
    
    '''
    filename = 'gpafile.csv'
    existing_file_data = []
    updated = False
    
    
    if os.path.exists(filename) == True:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            existing_file_data = list(reader)
    
    for i in existing_file_data:
        if i and i[0] == year:
            i[1] = str(gpa)
            updated = True
            break
    if updated == False:
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
