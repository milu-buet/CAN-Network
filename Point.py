# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis

from __future__ import print_function
from VHPoint import VHPoint
import math

class Point(object):
	"""docstring for Point"""
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		if isinstance(other, Point):
			return abs(self.x - other.x) < 0.1 and abs(self.y - other.y) < 0.1

		return NotImplemented

	def getVH(self,dim):
		return VHPoint(dim-self.y,self.x)

	def getVHG(self,dim):
		return VHPoint(self.x,dim-self.y)

	def clone(self):
		return Point(self.x,self.y)

	def __str__(self):
		return "(%s,%s)" % (self.x,self.y)


class Line(object):
	"""docstring for Line"""
	def __init__(self, point1,point2):
		self.point1 = point1
		self.point2 = point2