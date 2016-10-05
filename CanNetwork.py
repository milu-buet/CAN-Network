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
		self.node_dict_vh = {}

		self.canview = CanView(self)


	def addNode(self,name):
		a_node = CanNode(name)
		r_node = self.nodes[randint(0,len(self.nodes)-1) ]

		r_node.insertNode(a_node)
		self.registerNode(a_node)


	def registerNode(self,node):
		self.nodes.append(node)
		# point = node.getPoint()
		# try:
		# 	self.node_dict[point.x] 
		# except:
		# 	self.node_dict[point.x] = {}
		# self.node_dict[point.x][point.y] = node

		# vhpoint = node.getVHPoint()

		# try:
		# 	self.node_dict_vh[vhpoint.i]
		# except:
		# 	self.node_dict_vh[vhpoint.i] = {}

		
		# self.node_dict_vh[vhpoint.i][vhpoint.j] = node

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

		# b_node = CanNode('q')
		# a_node.insertNode(b_node)
		# self.registerNode(b_node)

		# b_node = CanNode('c')
		# a_node.insertNode(b_node)
		# self.registerNode(b_node)

