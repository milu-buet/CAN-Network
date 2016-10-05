# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis

from __future__ import print_function
import math

class VHPoint(object):
	"""docstring for VHPoint"""
	def __init__(self, i,j):
		self.i = i
		self.j = j

	def adjust(self,dim):
		self.i = int(math.ceil(dim*self.i))
		self.j = int(math.ceil(dim*self.j))
		return self


	def __str__(self):
		return "(%s,%s)" % (self.i,self.j)