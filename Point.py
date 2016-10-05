# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis

from VHPoint import VHPoint

class Point(object):
	"""docstring for Point"""
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def getVH(self,dim):
		return VHPoint(dim-self.y,self.x)

	def __str__(self):
		return "(%s,%s)" % (self.x,self.y)


class Line(object):
	"""docstring for Line"""
	def __init__(self, point1,point2):
		self.point1 = point1
		self.point2 = point2