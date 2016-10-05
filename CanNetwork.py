# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *





class CanNetwork(object):
	"""docstring for CanNetwork"""
	def __init__(self):
		self.nodes = []
		self.node_dict = {}
		self.node_dict_vh = {}
		self.init_view()
		
	def init_view(self):
		self.view = {}
		self.final_view = {}
		for i in range(0,11):
			self.view[i] = {}
			for j in range(0,11):
				if i==0 or i==10 or j==0 or j==10:
					self.view[i][j] = '.'
				else:
					self.view[i][j] = ' '

	def loadNodeIntoView(self):
		for node in self.nodes:
			node.load(self.view)



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

	def addNode(self,name):
		a_node = CanNode(name)
		r_node = self.nodes[randint(0,len(self.nodes)-1) ]

		r_node.insertNode(a_node)
		self.registerNode(a_node)



	def registerNode(self,node):
		self.nodes.append(node)
		point = node.getPoint()
		try:
			self.node_dict[point.x] 
		except:
			self.node_dict[point.x] = {}
		self.node_dict[point.x][point.y] = node

		vhpoint = node.getVHPoint()

		try:
			self.node_dict_vh[vhpoint.i]
		except:
			self.node_dict_vh[vhpoint.i] = {}

		
		self.node_dict_vh[vhpoint.i][vhpoint.j] = node

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


	def showCAN(self):
		self.init_view()
		self.loadNodeIntoView()
		for i in range(0,11):
			for j in range(0,11):
				print("%s   "% (self.view[i][j],),end='')
				
			if i==10:	
				print("(1,0)",end='')	
			if i==0:
				print("(1,1)",end='')
			if i!=10:	
				print("\n")
		print("\n(0,0)")

	def showCAN2(self):
		self.init_view()
		self.loadNodeIntoView()
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