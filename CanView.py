# Author: Md Lutfar Rahman
# Phd in CS, University of Memphis
from __future__ import print_function
from random import randint
from Point import *
from VHPoint import *
from Rigeon import *
from CanNode import *
from CanNetwork import *


class CanView(object):
	"""docstring for CanView"""
	def __init__(self, CanNetwork):
		self.CanNetwork = CanNetwork
