# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis

from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *

class Rigeon(object):
	"""docstring for Rigeon"""
	def __init__(self, point1,point2):
		self.point1 = point1
		self.point2 = point2
		self.node = None

	def __str__(self):
		return "%s %s" % (self.point1, self.point2)

	def setNode(self,node):
		self.node = node

	def getMidlePoint(self):
		x = round((self.point1.x+self.point2.x)/2.0,1)
		y = round((self.point1.y+self.point2.y)/2.0,1)
		return Point(x,y)

	def IsPointInTheRigeon(self,point):
		if point.x < self.point1.x or point.x > self.point2.x:
			return False
		if point.y < self.point1.y or point.y > self.point2.y:
			return False
		return True

	def divideRigeon(self):
		if randint(0,1) == 0:
			return self.divideRigeonVertically()
		return self.divideRigeonHorizontally()

	def divideRigeonVertically(self):
		x = round((self.point1.x+self.point2.x)/2.0,1)

		point3 = Point(x,self.point1.y)
		point4 = Point(x,self.point2.y)

		return Rigeon(self.point1,point4),Rigeon(point3,self.point2)


	def divideRigeonHorizontally(self):
		y = round((self.point1.y+self.point2.y)/2.0,1)

		point3 = Point(self.point1.x,y)
		point4 = Point(self.point2.x,y)

		return Rigeon(self.point1,point4),Rigeon(point3,self.point2)

	def getCommonLine(self,rigeon):
		pass

	def getLineLength(self):
		vertical_line = int(10*(self.point2.x - self.point1.x))
		horizontal_line = int(10*(self.point2.y - self.point1.y))

		return vertical_line,horizontal_line

	def loadLine(self,view,point1,point2):
		point1 = point1.getVH(1).adjust(10)
		point2 = point2.getVH(1).adjust(10)
		#print(point1.i,point1.j,point2.i,point2.j)
		
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
				

	def load(self,view):
		point1 = self.point1
		point2 = self.point2
		point3 = Point(self.point2.x,self.point1.y)
		point4 = Point(self.point1.x,self.point2.y)

		self.loadLine(view,point1,point3)
		self.loadLine(view,point3,point2)
		self.loadLine(view,point4,point2)
		self.loadLine(view,point1,point4)
		