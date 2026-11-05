import tkinter as tk
def on_click():
    print("Button clicked!")
root = tk.Tk() # To create basic windows
root.title("Simple Button Example") # To set the window title
root.geometry("300x200") # To set the size of the window
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=50)
root.mainloop()