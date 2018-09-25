import tkinter as tk

def onclick(args):
	if args == 1:
		print ("Button clicked 1")
	

def alsoonclick(args):
	if args == 2:
		print ("Button clicked 2")


root = tk.Tk()
root.title("GUI Button")

#Creating an Element
btn1 = tk.Button(root, text="Button 1", command=lambda:onclick(1))
btn2 = tk.Button(root, text="Button 2", command=lambda:alsoonclick(2))


#Putting element on a main window
btn1.pack()
btn2.pack()

root.mainloop()
