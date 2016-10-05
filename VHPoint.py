# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis

from __future__ import print_function

class VHPoint(object):
	"""docstring for VHPoint"""
	def __init__(self, i,j):
		self.i = i
		self.j = j

	def Draw(self,view,char):
		view[i][j] = char

	def adjust(self,dim):
		self.i = int(dim*self.i)
		self.j = int(dim*self.j)

		return self