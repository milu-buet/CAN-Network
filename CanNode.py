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
		self.neighbours = []
	def getname(self):
		return self.name
	def setRigeon(self,rigeon):
		self.rigeon = rigeon
		self.rigeon.setNode(self)
		self.setPoint(self.rigeon.getMidlePoint()) 

	def getRigeon(self):
		return self.rigeon

	def setPoint(self,point):
		self.point = point

	def getPoint(self):
		return self.point

	def addNeighbour(self,node):
		self.neighbours.append(node)

	def removeNeighbour(self,node):
		self.neighbours.remove(node)

	def showNeighbour(self):
		for node in self.neighbours:
			print(node)

	def insertNode(self,node):
		
		rigeon1,rigeon2 = self.getRigeon().divideRigeon()
		self.setRigeon(rigeon1)
		node.setRigeon(rigeon2)

		self.addNeighbour(node)
		node.addNeighbour(self)

		return self,node


	def __str__(self):
		return "%s%s"%(self.name,self.getPoint())


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

	def getVHPoint(self):
		return self.getPoint().getVH(1).adjust(10)

	def load(self,view):
		self.getRigeon().load(view)
		VHNodePoint = self.getVHPoint()
		nodeview = '%s%s'%('.',self,)
		view[VHNodePoint.i][VHNodePoint.j] = nodeview 
		#view[VHNodePoint.i][VHNodePoint.j] = "."
