#This imports the tkinter "tool box" this contains
#all of the support material to make GUI elements
#by including "as tk" we are giving a short name to use.
import tkinter as tk


#Main window
root = tk.Tk() #Creates standard window
# Step one: construct the object: Build and configure it.
# Step two: Configure the object: Specify behavouir and settings (optional).
# Step three Pack the object: Put it in the window.
output = tk.Text (root,height = 10, width = 30) #Parameters are what are sent
# ordered parameters: The order I send the parameters matters. (COMMON)
# Named parameters: JavaScript and python specific
output.config(state = "disable", background = "blue")
output.grid(row = 0, column = 0, rowspan = 5)


#**********WIDGET 2,3,4 (Labels)************

labInput1 = tk.Label(root, text = "input 1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "input 2")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "input 3")
labInput3.grid(row = 7, column = 0)


#**********WIDGET 5,6 (Checkboxes)***********
#How do I track the checkbox state.
var1 = IntVar()
var2 = Intvar()


#What the named parameter variable does is binds the IntVar to the
#checkbox. If there is a change in the box, there is a change in the variable.
#This is called BINDING

c = Checkbutton(root, text="Expand", variable=var1)
cHC.grid(row = 0, column = 1)

c = Checkbutton(root, text="Expand", variable=var2)
cHC.grid(row = 1, column = 1)

#This is an event driven program
#Build a GUI
#Start it running
#Wait for "EVENT"

root.mainloop() #Starts the program.