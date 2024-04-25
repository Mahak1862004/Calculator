import tkinter as tk

def button_click(value):
    if value == "=":
        calculate()
    elif value == "Clear":
        clear()
    else:
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear", padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
