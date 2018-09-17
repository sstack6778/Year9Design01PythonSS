import tkinter as tk

def clicked(*args):

	print("clicked")

root = tk.Tk()


btn1 = tk.Button(root, text="BTN 1", command = clicked)

btn1.pack()

root.mainloop();

