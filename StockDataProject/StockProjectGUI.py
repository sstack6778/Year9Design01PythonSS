import tkinter as tk


root = tk.Tk()

#1. Construct object
#2. Configure the object
#3. Pack the object (put it in window)

output = tk.Text(root,height = 30, width = 50)

#Ordered parameters: the order of the parameters is important
#Named parameters: Unique to JavaScript and Python

output.config(state = "disable", background = "white")
output.config(row = 0, column = 1)


#Putting in the widgets


labInput1 = tk.Label(root, text = "Stock Manager")
labInput1.grid(row = 0, column = 1)





root.mainloop()