# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *
from CanNetwork import *
import time

try:  # import as appropriate for 2.x vs. 3.x
   from tkinter import *
except:
   from Tkinter import *



class CanGraphicalView(object):
	"""docstring for CanView"""

	adjust = 10
	dim = 1

	def __init__(self, CanNetwork, win, width ,height):
		self.CanNetwork = CanNetwork
		self.win = win
		self.width = width
		self.height = height
		self.panel_height = 150
		self.margin = 5

		self.canvas = Canvas(self.win, width=width, height=height - self.panel_height)
		self.canvas.pack()

		#self.control_canvas = Canvas(self.win, width=width, height=height - self.panel_height)
		#self.control_canvas.place(x=0,y=height - self.panel_height)


		self.CAN_DIM = self.height - self.panel_height - self.margin
		self.CAN_BEGIN = self.width/2 - self.CAN_DIM/2
		self.init_graphical_view()

		self.show()

	def init_graphical_view(self):


		#self.setBackground()
		self.setControlPanel()
		#self.exp()

		pass

	def exp(self):
		# p = PointG(500,0)
		# p.setFill("red")
		# p.draw(self.win)

		# c = Circle(PointG(500,50), 10)
		# c.draw(self.win)

		pass

	def setBackground(self):

		#p = Polygon(PointG(0,0), PointG(600,0), PointG(600,500),PointG(0,500))
		#p.setFill("red")
		#p.draw(self.win)
		pass

	def setControlPanel(self):
		panel_height = self.panel_height
		margin = self.margin

		self.addNodeTextBox = Entry(self.win)
		self.addNodeTextBox.insert(0,"New node name")
		self.addNodeTextBox.place(x=50,y=380)

		self.addNodeButton = Button(self.win, text="Add Node", command=self.addNodeButtonAction)
		self.addNodeButton.place(x=90,y=405)

		self.deleteNodeTextBox = Entry(self.win)
		self.deleteNodeTextBox.insert(0,"Node to delete")
		self.deleteNodeTextBox.place(x=260,y=380)

		self.deleteNodeButton = Button(self.win, text="Delete Node", command=self.deleteNodeButtonAction)
		self.deleteNodeButton.place(x=300,y=405)

		self.rP1NodeTextBox = Entry(self.win)
		#self.rP1NodeTextBox.insert(0,"start")
		self.rP1NodeTextBox.place(x=50,y=440)

		self.rP2NodeTextBox = Entry(self.win)
		#self.rP2NodeTextBox.insert(0,"end")
		self.rP2NodeTextBox.place(x=260,y=440)

		self.rButton = Button(self.win, text="Show Route", command=self.ShowRouteAction)
		self.rButton.place(x=180,y=465)

	
	def ShowRouteAction(self):
		
		p1 = self.rP1NodeTextBox.get()
		fromNode = self.CanNetwork.node_dict[p1]

		p2 = self.rP2NodeTextBox.get()
		toNode = self.CanNetwork.node_dict[p2]

		route = self.CanNetwork.findRoute(fromNode,toNode)

		if route:
			for i in range(0,len(route)-1):
				self.create_line(route[i],route[i+1])
			

	def create_line(self,node1,node2):
		p1 = node1.getPoint().getVHG(1).adjust(self.CAN_DIM).screenAdjust(self.CAN_BEGIN)
		p2 = node2.getPoint().getVHG(1).adjust(self.CAN_DIM).screenAdjust(self.CAN_BEGIN)
		print(p1,p2)
		self.canvas.create_line(p1.i, p1.j, p2.i, p2.j)



	def addNodeButtonAction(self):
		print("click!")
		name = self.addNodeTextBox.get()
		x,y = self.CanNetwork.getRandomPoint()
		targetnode = self.CanNetwork.lookUpNode(x,y)

		random_point = Point(x,y).getVHG(1).adjust(self.CAN_DIM).screenAdjust(self.CAN_BEGIN)
		ntext = self.canvas.create_text(random_point.i, random_point.j, text=name)
		self.CanNetwork.addNode(name,NodeFallsInTheRigeon = targetnode)

		#self.canvas.move(ntext, 300, 300)
		self.canvas.update()
		
		self.win.after(1500, self.reDraw())
		#self.reDraw()
		self.addNodeTextBox.delete(0, END)


	def deleteNodeButtonAction(self):
		print("click!")

		name = self.deleteNodeTextBox.get()
		self.CanNetwork.deletNode(name)
		self.reDraw()
		self.deleteNodeTextBox.delete(0, END)


	def show(self):
		self.loadView()


	def loadView(self):
		
		for node in self.CanNetwork.nodes:
			self.loadNode(node)
			#print(node.getPoint(),self.getVhPoint(node))
			print(node,node.getRigeon())

	def loadNode(self,node):

		self.loadRigeon(node.getRigeon())
		VHNodePoint =self.getVhPoint(node)
		#nodeview = '%s%s'%('.',node,)
		nodeview = node.name
		self.canvas.create_text(VHNodePoint.i, VHNodePoint.j, text=nodeview)

	def loadRigeon(self,rigeon):
		
		P1 = rigeon.getP2().getVHG(1).adjust(self.CAN_DIM).screenAdjust(self.CAN_BEGIN)
		P0 = rigeon.getP4().getVHG(1).adjust(self.CAN_DIM).screenAdjust(self.CAN_BEGIN)
		self.canvas.create_rectangle(P0.i, P0.j, P1.i, P1.j, fill="green")


	def getVhPoint(self,node):
		return node.getPoint().getVHG(1).adjust(self.CAN_DIM).screenAdjust(self.CAN_BEGIN)

	def reDraw(self):
		self.canvas.delete("all")
		self.loadView()


		

