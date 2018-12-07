import tkinter as tk



def submitClicked():
	print("Submit Clicked")
	
	try: #in try statement as soon something goes wrong we STOP and jump to except
		#if anything in here goes wrong go to the except section
		tempa = nameEntry.get() #Access value in tempn
		#print(tempn) #prints to screen
		#print(names)

		names.append(tempa) #add it to list
		tempb = float(valueEntry.get())
		#print(tempn)
		tempc = float(quantityEntry.get())
		#print(tempn)
		value.append(tempb)

		number.append(tempc)
	except:
		valueEntry.delete(0,tk.END)
		quantityEntry.delete(0,tk.END)
		print("dude, I said a float!")
	
	print(names)
	print(number)
	print(value)	
	#LOOP THROUGH NUMBER TO ACCESS EACH ELEMENT
	#EXAMPLE
	#	number = [2,4,5]
	#	value = [4,3,6]
	#
	# totalValue = 2 * 4 + 4 * 3 + 5 * 6
	# totalValue = number[0]*value[0]+number[1]*value[1]+number[2]*value[2]
	#What I observe is that we are sequentially moving through the list 0,1,2
	#Question: How do I do this regardless of list size
	#Answer: use a loop
	total = 0
	for i in range(0,len(number),1):	
		total = total + float(number[i]) * float(value[i])

	#Simple trace
	# total = 0
	# i = 0, 0 < 3, True
	# total = 0 + number[0]*value[0] = 0 + 2 * 4 = 8
	# i = 1, 1 < 3 True
	# total = 8 + number[1]*value[1] = 8 + 4 * 3 = 20
	# i = 2, 2 < 3 True
	# total = 20 + number[2]*value[2] =  20 + 5 * 6 = 20 + 30 = 50
	print(total)
	output.delete("1.0", tk.END)
	output.insert(tk.END,"Total portfolio value = "+str(total) + " CAD")

#Group Data Variables here!
names = [] #Names entered 
number = [] #NUMBER OWNED 
value = [] #VALUE AT TIME OF PURCHASE


'''
READING THE TABLE
names[0] = "Stock 1"
number[0] = 3
value [0] = 6

3 units of stock 1 valued at 6 dollars. 
Total value = number[0] * value[0]




'''

root = tk.Tk()


titleLabel = tk.Label(root, text = "Stock Manager")
titleLabel.grid(row = 0, column = 0, columnspan = 3)

#Output box is where we will display the stock information
output = tk.Text(root, background = "grey", height = 10, width = 50, font = ("Helvitica",16))
#output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 3)

nameLabel = tk.Label(root, text = "Name")
nameLabel.grid(row = 2, column = 0)

nameEntry = tk.Entry(root)
nameEntry.grid(row = 2,column = 1)

valueLabel = tk.Label(root, text = "Value")
valueLabel.grid(row = 3, column = 0)

valueEntry = tk.Entry(root)
valueEntry.grid(row = 3,column = 1)

quantityLabel = tk.Label(root, text = "Quantity")
quantityLabel.grid(row = 4, column = 0)

quantityEntry = tk.Entry(root)
quantityEntry.grid(row = 4,column = 1)

submitButton = tk.Button(root, text = "Submit", command = submitClicked)
submitButton.grid(row = 5, column = 0, columnspan = 3, sticky = "NESW")

removeButton = tk.Button(root, text = "Remove")
removeButton.grid(row = 6, column = 0, columnspan = 3, sticky = "NESW")

#portfolioLabel = tk.Label(root, text = "Portfolio Value")
#portfolioLabel.grid(row = 1, column = 0, columnspan = 3, sticky = "NESW")
#This is a label that I removed. I removed it because







root.mainloop()