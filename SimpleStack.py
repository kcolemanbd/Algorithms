# SimpleStack-in-Python
# Simple Stack Class written in Python

#  Created by Keith Coleman on 11/26/16.
#  Copyright © 2016 Keith Coleman. All rights reserved.
#

from System import *

class SimpleStack(object):
	def __init__(self, initialCapacity, nIncrement):
		self._nElements = 0
		self._nIncrement = nIncrement
		self._elements = Array.CreateInstance(Object, initialCapacity)

	def Push(self, element):
		if self._nElements == self._elements.Length:
			temp = Array.CreateInstance(Object, self._nElements + self._nIncrement)
			i = 0
			while i < self._nElements:
				temp[i] = self._elements[i]
				i += 1
			self._elements = temp
		self._elements[self._nElements] = element
		self._nElements += 1

	def Pop(self):
		if self.IsEmpty():
			return None
		else:
			element = self._elements[self._nElements - 1]
			self._nElements -= 1
			return element

	def Peek(self):
		if self.IsEmpty():
			return None
		else:
			return self._elements[self._nElements - 1]

	def IsEmpty(self):
		if self._nElements == 0:
			return True
		else:
			return False

	def get_Length(self):
		return self._nElements

	Length = property(fget=get_Length)
