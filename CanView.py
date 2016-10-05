# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *
from CanNetwork import *


class CanView(object):
	"""docstring for CanView"""

	adjust = 10
	dim = 1

	def __init__(self, CanNetwork):
		self.CanNetwork = CanNetwork

		self.view = {}
		self.init_view()

	def init_view(self):
		for i in range(0,11):
			self.view[i] = {}
			for j in range(0,11):
				if i==0 or i==10 or j==0 or j==10:
					self.view[i][j] = '.'
				else:
					self.view[i][j] = ' '

	def show(self):
		self.init_view()
		self.loadView()
		for i in range(0,11):
			for j in range(0,11):
				print("%s "% (self.view[i][j],),end='')
				
			if i==10:	
				print("(1,0)",end='')	
			if i==0:
				print("(1,1)",end='')
			if i!=10:	
				print("")
		print("\n(0,0)")


	def loadView(self):
		
		for node in self.CanNetwork.nodes:
			self.loadNode(node)
			print(node.getPoint(),self.getVhPoint(node))

	def loadNode(self,node):

		self.loadRigeon(node.getRigeon())
		VHNodePoint =self.getVhPoint(node)
		nodeview = '%s%s'%('.',node,)
		self.view[VHNodePoint.i][VHNodePoint.j] = nodeview 

	def loadRigeon(self,rigeon):
		

		point1 = rigeon.point1
		point2 = rigeon.point2
		point3 = Point(rigeon.point2.x,rigeon.point1.y)
		point4 = Point(rigeon.point1.x,rigeon.point2.y)

		self.loadLine(point1,point3)
		self.loadLine(point3,point2)
		self.loadLine(point4,point2)
		self.loadLine(point1,point4)


	def loadLine(self,point1,point2):
		point1 = point1.getVH(1).adjust(10)
		point2 = point2.getVH(1).adjust(10)
		#print(point1.i,point1.j,point2.i,point2.j)

		view = self.view
		
		if point1.i == point2.i and point1.i<10:
			
			if point1.j <= point2.j:
				for k in range(point1.j,point2.j+1):
					if k<10:
						view[point1.i][k] = '.'
			else:
				for k in range(point2.j,point2.j+1):
					if k<10:
						view[point1.i][k] = '.'
				

		if point1.j == point2.j and point1.j<10:
 
 			if point1.i <= point2.i:
				for k in range(point1.i,point2.i+1):
					if k<10:
						view[k][point1.j] = '.'

			else:
				for k in range(point2.i,point1.i+1):
					if k<10:
						view[k][point1.j] = '.'	


	def getVhPoint(self,node):
		return node.getPoint().getVH(1).adjust(10)

