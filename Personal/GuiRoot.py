import tkinter as tk #imports tkinter

root = tk.Tk() #creates a main window called root
root.title("GUI Button")


root.title("Main Window")

btn1 = tk.Button(root, text="Button 1")
#btn2 = tk.Button(root, text="Button 2")


#Last Step: Put element on main window
btn1.pack()
#btn2.pack()


root.mainloop() #displays the window and waits for action

#Event Driven Programming:  This is a style of programming where a program sits 
#and waits for you to do something. 

