# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *
from CanView import *
from CanGraphicalView import *


class CanNetwork(object):
	"""docstring for CanNetwork"""
	def __init__(self):
		self.nodes = []
		self.node_dict = {}
		self.OneNodeInit()

	def OneNodeInit(self):
		point1 = Point(0,0)
		point2 = Point(1,1)

		TotalRigeon = Rigeon(point1,point2)
		a_node = CanNode('p')
		a_node.setRigeon(TotalRigeon)
		a_node.setStaringRigeon(TotalRigeon)
		self.registerNode(a_node)

	def reset(self):
		self.__init__()

	def addNode(self,name):

		try:
			if self.node_dict[name]:
				return False
		except:
			pass

		a_node = CanNode(name)
		r_node = self.nodes[randint(0,len(self.nodes)-1) ]

		r_node.insertNode(a_node)
		self.registerNode(a_node)

		return True


	def deletNode(self,name):
		
		try:
			node = self.node_dict[name]
			parent_node = node.getParent()
		except:
			print('Node deletion error!!!')
			return False

		if len(node.getChildren()) > 0:
			#find one children with complete common line, merge to it
			for child in node.getChildren():
				if node.getRigeon().hasCompleteCommonLine(child.getRigeon()):
					new_rigeon = node.getRigeon().mergeRigeon(child.getRigeon())  #merge rigeon
					#print("Common Line found with node = %s, rigeon = %s"% (child,new_rigeon))
					
					child.setRigeon(new_rigeon)
					child.adoptParentsChildrenAndRole() #and fix parent relation
					self.unregisterNode(node)
					
					return True


			#no children with complete common line?
			print('this case should not exist!!!')
			print('Entered in streching mode 1')

			left_area = node.getRigeon().getArea()

			#for child in node.getAllLowerLevelNode():
			for child in self.nodes:
				if child.name != node.name and node.getRigeon().hasAnyCommonLine(child.getRigeon()):
					print('>>')
					print(child)
					con_area = child.getRigeon().strechRigeon(node.getRigeon())
					left_area = left_area - con_area


			node.getChildren()[0].adoptParentsChildrenAndRole()
			self.unregisterNode(node)



		elif parent_node != None:
			#if complete common line exists, merge to parent
			#else things are critical
			if node.getRigeon().hasCompleteCommonLine(parent_node.getRigeon()):
				
				new_rigeon = node.getRigeon().mergeRigeon(parent_node.getRigeon())
				parent_node.setRigeon(new_rigeon)

				self.unregisterNode(node)
				return True
			else:
				pass # this is the shitty case
				#find if any sibling has complete common line
				
				for sibling in parent_node.getChildren():
					if sibling.name != node.name:
						if node.getRigeon().hasCompleteCommonLine(sibling.getRigeon()):

							print("sibling found = %s" %(sibling,))

							new_rigeon = node.getRigeon().mergeRigeon(sibling.getRigeon())
							sibling.setRigeon(new_rigeon)
							self.unregisterNode(node)
							return True


				# I'm fucked up here
				# try streching style
				print('Entered in streching mode 2')
				left_area = node.getRigeon().getArea()

				if node.getRigeon().hasAnyCommonLine(parent_node.getRigeon()):
					print('>>')
					print(parent_node)
					parent_node.getRigeon().strechRigeon(node.getRigeon())

				#for sibling in parent_node.getAllLowerLevelNode():
				for sibling in self.nodes:
					if sibling.name != node.name:
						if node.getRigeon().hasAnyCommonLine(sibling.getRigeon()):
							print('>>')
							print(sibling)
							con_area = sibling.getRigeon().strechRigeon(node.getRigeon())
							left_area = left_area - con_area

				self.unregisterNode(node)



		else:
			print('node has no Child or Parent')
			pass # Nothing to delete, only one node available here 



	def registerNode(self,node):
		self.nodes.append(node)
		self.node_dict[node.name] = node

	def unregisterNode(self,node):

		self.nodes.remove(node)
		self.node_dict[node.name] = None

		if node.getParent():
			node.getParent().removeChildren(node)

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

	def createSampleCAN(self):
		point1 = Point(0,0)
		point2 = Point(1,1)

		TotalRigeon = Rigeon(point1,point2)
		a_node = CanNode('p')
		a_node.setRigeon(TotalRigeon)
		self.registerNode(a_node)


