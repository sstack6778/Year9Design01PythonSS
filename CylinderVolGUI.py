import tkinter as tk

root = tk.Tk() #creates the window
root.title("Volume of a Cylinder") #configures the window


labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()


btn = tk.Button (root, text="Submit")


output = tk.Text (root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.pack()




root.mainloop()