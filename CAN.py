# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
print('Initializing....')

class Point(object):
	"""docstring for Point"""
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def getVH(self,dim):
		return VHPoint(dim-self.y,self.x)

	def __str__(self):
		return "(%s,%s)" % (self.x,self.y)

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
		
		

class Line(object):
	"""docstring for Line"""
	def __init__(self, point1,point2):
		self.point1 = point1
		self.point2 = point2
		


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
		

class CanDataNode(object):
	"""docstring for CanDataNode"""
	def __init__(self, point):
		self.point = point

	def function():
		pass
		



class CanNode(object):
	"""docstring for CanNode"""
	def __init__(self,name):
		self.name = name
		self.neighbours = []
	def getname(self):
		return self.name
	def setRigeon(self,rigeon):
		self.rigeon = rigeon
		self.rigeon.setNode(self)
		self.setPoint(self.rigeon.getMidlePoint()) 

	def getRigeon(self):
		return self.rigeon

	def setPoint(self,point):
		self.point = point

	def getPoint(self):
		return self.point

	def addNeighbour(self,node):
		self.neighbours.append(node)

	def removeNeighbour(self,node):
		self.neighbours.remove(node)

	def showNeighbour(self):
		for node in self.neighbours:
			print(node)

	def insertNode(self,node):
		
		rigeon1,rigeon2 = self.getRigeon().divideRigeon()
		self.setRigeon(rigeon1)
		node.setRigeon(rigeon2)

		self.addNeighbour(node)
		node.addNeighbour(self)

		return self,node


	def __str__(self):
		return "%s%s"%(self.name,self.getPoint())


	def show(self):
		vertical_line,horizontal_line = self.getRigeon().getLineLength()
		print(vertical_line,horizontal_line)

		for i in range(0,horizontal_line):
			print('.   ',end='')
		print('')	
		print('')
		
		for i in range(0,vertical_line-2):
			print('.',end='')

			if i == (vertical_line-2)/2:
				for j in range(0,2*horizontal_line-8):
					print(' ',end='')

				print(".%s"%(self,),end='')

				for j in range(0,2*horizontal_line-9):
					print(' ',end='')
			else:
				for j in range(0,4*horizontal_line-6):
					print(' ',end='')

			print(' .')
			print('')
		
		for i in range(0,horizontal_line):
			print('.   ',end='')

		print('\n')

	def getVHPoint(self):
		return self.getPoint().getVH(1).adjust(10)

	def load(self,view):
		self.getRigeon().load(view)
		VHNodePoint = self.getVHPoint()
		nodeview = '%s%s'%('.',self,)
		view[VHNodePoint.i][VHNodePoint.j] = nodeview 
		#view[VHNodePoint.i][VHNodePoint.j] = "."





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


# CAN = CanNetwork()
# CAN.createSampleCAN()
# #CAN.showNodes()
# CAN.showCAN2()


def run_prog():

	s = ''' 
	Action on CAN?
	1. Add node
	2. Delete node
	3. Reset CAN
	4. Exit
	Choice(1/2/3/4)?:
		'''

	CAN = CanNetwork()
	CAN.createSampleCAN()
	#CAN.showNodes()

	print("Current CAN")
	CAN.showCAN2()
	
	while(True):
	
		print(s)
		x = int(input(""))
		#print(x)

		if x == 1:
			name = input("New node name(example:'q')=")
			CAN.addNode(name)
		elif x==2:
			pass
		elif x==3:
			pass
		else:
			break

		CAN.showCAN2()

run_prog()
		

# point1 = Point(0,0)
# point2 = Point(1,1)
# a = Rigeon(point1,point2)
# b = CanNode("P")
# b.setRigeon(a)
# c = b.getPoint()
# abn = {c:b}
# print abn[c]
print('')
print('Ended....')
