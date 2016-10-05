# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *
from CanNetwork import *

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
	CAN.createSampleCAN()
	#CAN.showNodes()

	print("Current CAN")
	CAN.show()
	
	while(True):
	
		print(s)
		x = int(input(""))
		if x == 1:
			name = input("New node name(example:'q')=")
			CAN.addNode(name)
		elif x==2:
			pass
		elif x==3:
			pass
		else:
			break

		CAN.show()

run_prog()
		

print('')
print('Ended....')
