import tkinter as tk
root = tk.Tk()
root.geometry("500x500")
root.title("First Tkinter UI")
label = tk.Label(root, text="Hello World!", font=('Arial',18))
label.pack(padx=20, pady=20)
textbox = tk.Text(root, font=('Arial', 16), background=('grey'), height=3)
textbox.pack()

myentry = tk.Entry(root)
myentry.pack(padx=10)

# button = tk.Button(root, text="Click me baby", font=('Arial', 18))
# button.pack(padx=5, pady=5)
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text='1', font=('Arial',18))
btn1.grid(row=0, column=0, sticky= tk.W + tk.E)



buttonFrame.pack()
root.mainloop()