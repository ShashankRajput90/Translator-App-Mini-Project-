import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Simple Tkinter Example")
root.geometry("400x300")  # Set the window size

# Label to display some text
label = tk.Label(root, text="Welcome to Tkinter!", font=("Montserrat", 22))
label.pack(pady=35)  # Add vertical padding

# Function to handle button click
def on_button_click():
    messagebox.showinfo("Action", "Button clicked!")

# Button to trigger the function
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()
