# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis

from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *


class CanNode(object):
	"""docstring for CanNode"""
	def __init__(self,name):
		self.name = name
		self.children = []
		self.parent = None
		self.starting_rigeon = None
	def getname(self):
		return self.name
	def setRigeon(self,rigeon):
		self.rigeon = rigeon
		self.rigeon.setNode(self)
		self.setPoint(self.rigeon.getMidlePoint()) 

	def getRigeon(self):
		return self.rigeon

	def setStaringRigeon(self,rigeon):
		self.starting_rigeon = rigeon

	def getStartingRigeon():
		return self.starting_rigeon

	def setPoint(self,point):
		self.point = point

	def getPoint(self):
		return self.point

	def addChildren(self,node):
		self.children.append(node)

	def removeChildren(self,node):
		self.children.remove(node)

	def getChildren(self):
		return self.children

	def showChildren(self):
		for node in self.children:
			print(node)

	def addParent(self,node):
		self.parent = node

	def getParent(self):
		return self.parent 

	def adoptParentsChildrenAndRole(self):
		if self.parent != None:
			for child in self.parent.getChildren():
				if self != child:
					self.addChildren(child)
					child.addParent(self)

			self.parent = self.parent.parent


	def insertNode(self,node):

		vertical_line,horizontal_line = self.getRigeon().getLineLength()

		if vertical_line < horizontal_line:
			rigeon1,rigeon2 = self.getRigeon().divideRigeonHorizontally()

		elif vertical_line > horizontal_line:
			rigeon1,rigeon2 = self.getRigeon().divideRigeonVertically()

		else:
			if randint(0,1) == 0:
				rigeon1,rigeon2 = self.getRigeon().divideRigeonHorizontally()
			rigeon1,rigeon2 = self.getRigeon().divideRigeonVertically()

		
		#rigeon1,rigeon2 = self.getRigeon().divideRigeon()
		self.setRigeon(rigeon1)
		node.setRigeon(rigeon2)
		node.setStaringRigeon(rigeon2)

		self.addChildren(node)
		node.addParent(self)

		return self,node


	def __str__(self):
		return "%s%s"%(self.name,self.getPoint())


	# def getVHPoint(self):
	# 	return self.getPoint().getVH(1).adjust(10)


	def show(self):
		vertical_line,horizontal_line = self.getRigeon().getLineLength()
		print(vertical_line,horizontal_line)

		for i in range(0,horizontal_line):
			print('.   ',end='')
		print('')	
		print('')
		
		for i in range(0,vertical_line-2):
			print('.',end='')

			if i == (vertical_line-2)/2:
				for j in range(0,2*horizontal_line-8):
					print(' ',end='')

				print(".%s"%(self,),end='')

				for j in range(0,2*horizontal_line-9):
					print(' ',end='')
			else:
				for j in range(0,4*horizontal_line-6):
					print(' ',end='')

			print(' .')
			print('')
		
		for i in range(0,horizontal_line):
			print('.   ',end='')

		print('\n')
