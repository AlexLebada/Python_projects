import tkinter as tk
from tkinter import messagebox
import re

def performMath():
    global new_value
    global previous
    # Get the user input and update the variable
    new_value = input_entry.get()
    calculated_value = re.sub('[a-zA-Z,.:()" "]', '', new_value)
    if previous ==0:
        previous = eval(calculated_value)
    else:
        previous = eval(str(previous)+calculated_value)

    if previous:
        variable_to_display.set(f"Variable Value: {previous}")
        input_entry.delete(0, tk.END)  # Clear the entry field after updating

def stopMath():
    global  run
    run = False
    root.quit()
    show_msg()

def show_msg():
    messagebox.showinfo("Message", "Goodbye")

previous = 0
new_value = 0
# continue calculation
run = True

# Create window
root = tk.Tk()
root.title("My calculator")
root.geometry("400x200")

# Variable to display (use StringVar for dynamic updates)
variable_to_display = tk.StringVar()
variable_to_display.set("Result: Insert values")

# Add a label to display the variable
label = tk.Label(root,
    textvariable=variable_to_display,
    font=("Arial", 14),
    bg="lightblue",
    fg="black",
    width=40,
    height=2,
    anchor="center",)
label.pack(pady=10)


# field user input
input_entry = tk.Entry(root,font=("Arial", 12), width=30)
input_entry.pack(pady=10)

# Add a button to update display
button = tk.Button(root, text="Enter", command=performMath, font=("Arial", 12))
button.pack(side="left",pady=10, padx=50)
button = tk.Button(root, text="Quit", command=stopMath, font=("Arial", 12) )
button.pack(side="right",padx = 100, pady=10 )

# loop
while run:
    root.mainloop()