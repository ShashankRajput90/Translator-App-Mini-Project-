import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont

# Initialize the main application window
root = tk.Tk()
root.title("Simple Tkinter Example")
root.geometry("400x200")  # Set the window size

# Label to display some text
custom_font = tkFont.Font(family="E:/Github/Translator App (Mini Project)/TranslatorApp/Quicksand/staticQuicksand-SemiBold.ttf", size=22)
label = tk.Label(root, text="Welcome to Tkinterface !", font=custom_font)
label.pack(pady=40)  # Add vertical padding

# Function to handle button click
def on_button_click():
    messagebox.showinfo("Action", "Button clicked!")

# Button to trigger the function
button = ttk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()


