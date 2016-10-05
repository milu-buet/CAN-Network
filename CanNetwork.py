# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *
from CanView import *


class CanNetwork(object):
	"""docstring for CanNetwork"""
	def __init__(self):
		self.nodes = []
		self.node_dict = {}

		self.canview = CanView(self)
		self.OneNodeInit()

	def OneNodeInit(self):
		point1 = Point(0,0)
		point2 = Point(1,1)

		TotalRigeon = Rigeon(point1,point2)
		a_node = CanNode('p')
		a_node.setRigeon(TotalRigeon)
		self.registerNode(a_node)

	def reset(self):
		self.__init__()

	def addNode(self,name):
		a_node = CanNode(name)
		r_node = self.nodes[randint(0,len(self.nodes)-1) ]

		r_node.insertNode(a_node)
		self.registerNode(a_node)


	def deletNode(self,name):
		
		node = self.node_dict[name]
		parent_node = node.getParent()

	def registerNode(self,node):
		self.nodes.append(node)
		self.node_dict[node.name] = node

	def showNodes(self):
		for node in self.nodes:
			#print(node, node.getRigeon())
			node.show()
	def IsNodeAvailable(self,x,y):
		try:
			val = self.node_dict[x][y]
			return True
		except:
			return False

	def IsVHNodeAvailable(self,i,j):
		try:
			val = self.node_dict_vh[i][j]
			return True
		except:
			return False

	def show(self):
		self.canview.show()

	def createSampleCAN(self):
		point1 = Point(0,0)
		point2 = Point(1,1)

		TotalRigeon = Rigeon(point1,point2)
		a_node = CanNode('p')
		a_node.setRigeon(TotalRigeon)
		self.registerNode(a_node)


