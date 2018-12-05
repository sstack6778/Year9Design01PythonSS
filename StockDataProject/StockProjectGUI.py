import tkinter as tk


#**************Values
stockList = ["GOOGL","AAPL","FB"]



root = tk.Tk()

#1. Construct object
#2. Configure the object
#3. Pack the object (put it in window)

output = tk.Text(root,height = 10, width = 50)

#Ordered parameters: the order of the parameters is important
#Named parameters: Unique to JavaScript and Python

output.config(state = "disable", background = "red")
output.grid(row = 0, column = 0, rowspan = 20)


#Putting in the widgets


labInput1 = tk.Label(root, text = "Stock Manager")
labInput1.grid(row = 0, column = 0)


entrStock = tk.Entry(root)
entrStock.grid(row = 0, column = 1)

entrStock = tk.Entry(root)
entrStock.grid(row = 1, column = 1)

entrStock = tk.Entry(root)
entrStock.grid(row = 2, column = 1)

entrStock = tk.Entry(root)
entrStock.grid(row = 0, column = 2)

entrStock = tk.Entry(root)
entrStock.grid(row = 1, column = 2)

entrStock = tk.Entry(root)
entrStock.grid(row = 2, column = 2)

entrStock = tk.Entry(root)
entrStock.grid(row = 2, column = 3)

entrStock = tk.Entry(root)
entrStock.grid(row = 1, column = 3)

entrStock = tk.Entry(root)
entrStock.grid(row = 0, column = 3)

entrStock = tk.Entry(root)
entrStock.grid(row = 1, column = 3)

entrStock = tk.Entry(root)
entrStock.grid(row = 2, column = 3)

entrStock = tk.Entry(root)
entrStock.grid(row = 3, column = 3)

root.mainloop()