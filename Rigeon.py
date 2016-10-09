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

	def getP1(self):
		return self.point1
	
	def getP2(self):
		return Point(self.point2.x,self.point1.y)
	
	def getP3(self):
		return self.point2

	def getP4(self):
		return Point(self.point1.x,self.point2.y)

	def doesRegionTouch(self,rigeon):
		return IsPointInTheRigeon(rigeon.point1) or IsPointInTheRigeon(rigeon.point2)

	def divideRigeon(self):

		vertical_line,horizontal_line = self.getLineLength()

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

	def getCompleteCommonLine(self,rigeon):
		
		# if self.point2.x == rigeon.point1.x and self.point1.y == rigeon.point1.y:
		# 	pass
		# elif self.point1.y == self.point2.y:
		# 	pass

		# return None
		pass


	def hasAnyCommonLine(self,rigeon):

		A = rigeon.point1.x >= self.point1.x and rigeon.point1.x <= self.point2.x   #in between x-axis
		B = rigeon.point2.x >= self.point1.x and rigeon.point2.x <= self.point2.x

		C = rigeon.point1.y == self.point2.y
		D = rigeon.point2.y == self.point1.y

		if A and B and C:
			return True
		elif A and B and D:
			return True



		A = rigeon.point1.y >= self.point1.y and rigeon.point1.y <= self.point2.y  #in between y-axis
		B = rigeon.point2.y >= self.point1.y and rigeon.point2.y <= self.point2.y

		C = rigeon.point1.x == self.point2.x
		D = rigeon.point2.x == self.point1.x

		if A and B and C:
			return True
		elif A and B and D:
			return True


		return False


	def hasCompleteCommonLine(self,rigeon):

		if self.getP2() == rigeon.getP1() and self.getP3() == rigeon.getP4():
			return True

		if rigeon.getP2() == self.getP1() and rigeon.getP3() == self.getP4():
			return True

		if self.getP4() == rigeon.getP1() and self.getP3() == rigeon.getP2():
			return True

		if rigeon.getP4() == self.getP1() and rigeon.getP3() == self.getP2():
			return True

		return False

	def getLineLength(self):
		vertical_line = int(10*(self.point2.x - self.point1.x))
		horizontal_line = int(10*(self.point2.y - self.point1.y))

		return vertical_line,horizontal_line

	def mergeRigeon(self,rigeon):

		#if it is true that two has complete common line

		point1 = None
		point2 = None

		if self.point1.x < rigeon.point1.x or self.point1.y < rigeon.point1.y:
			point1 = self.point1
			point2 = rigeon.point2
		elif self.point1.x > rigeon.point1.x or self.point1.y > rigeon.point1.y:
			point1 =  rigeon.point1
			point2 =  self.point2
		else :
			pass
			#identical rigeon
			return self

		return Rigeon(point1,point2)

	def getStrechDirection(self,target):
		
		mult = 1.0
		direc = None

		if self.getP1().x == target.getP3().x:
			mult = 0.5
			direc = 'x'

		elif self.getP3().x == target.getP1().x:
			mult = 2
			direc = 'x'

		elif self.getP3().y == target.getP1().y:
			mult = 2
			direc = 'y'

		elif self.getP1().y == target.getP3().y:
			mult = 0.5
			direc = 'y'


		return mult,direc



	def strechRigeon(self,target):

		mult,direc = self.getStrechDirection(target)
		print(mult,direc)

		vertical_line,horizontal_line = self.getLineLength()
		consumed_area = 0

		if direc == 'x':
			if mult < 1:
				consumed_area = vertical_line * int(10*abs(target.point1.x - self.point1.x))
				self.point1.x = target.point1.x
			else:
				consumed_area = vertical_line * int(10*abs(target.point2.x - self.point2.x))
				self.point2.x = target.point2.x
		elif direc == 'y':
			if mult < 1:
				consumed_area = horizontal_line * int(10*abs(target.point1.y - self.point1.y))
				self.point1.y = target.point1.y
			else:
				consumed_area = horizontal_line * int(10*abs(target.point2.y - self.point2.y))
				self.point2.y = target.point2.y


		self.node.setPoint(self.getMidlePoint()) 

		return consumed_area

	def getArea(self):
		vertical_line,horizontal_line = self.getLineLength()

		return vertical_line*horizontal_line



		