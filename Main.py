# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *
from CanNetwork import *
from CanView import *
from CanGraphicalView import *

print('Initializing....')


def run_prog():

	s = ''' 
Action on CAN?
1. Add node
2. Delete node
3. Reset CAN
4. Exit
Choice(1/2/3/4)?:
		'''

	CAN = CanNetwork()
	canview = CanView(CAN)

	print("Current CAN")
	canview.show()
	
	while(True):
	
		print(s)
		x = int(input(""))
		if x == 1:
			name = input("New node name?(example:'q')=")
			result = CAN.addNode(name)

			if result:
				pass #node added successfully
			else:
				print('DUPLICATE NAME ERROR')

		elif x==2:
			name = input("Node to delete?(example:'q')=")
			CAN.deletNode(name)
		elif x==3:
			CAN.reset()
		else:
			break

		print("Current CAN")
		canview.show()

#run_prog()

width = 500
height = 500
console_mode = True

try:  # import as appropriate for 2.x vs. 3.x
   from tkinter import *
except:
	try:
   		from Tkinter import *
   	except:
   		pass
   		console_mode = True


def graphical_run_prog():
	#CAN = CanNetwork()
	#win = GraphWin("CAN Network", width, height)
	#m = CanGraphicalView(CAN,win,width,height)
	#win.getMouse() # Pause to view result
	#win.close()    # Close window when done

	root = Tk() 
	root.wm_title("CAN Network Simulation")
	root.geometry("500x500")
	root.resizable(width=False, height=False)

	CAN = CanNetwork()
	CanGraphicalView(CAN,root,width,height)

	root.mainloop()
	root.destroy()



if __name__ == "__main__":

	if console_mode:
		run_prog()
	else:
		graphical_run_prog()
	

print('')
print('Ended....')
