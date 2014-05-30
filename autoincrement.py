
# Autoincrements an index until it reaches its max value
# in which case loops back to 0
class Autoincrement:
	"""Initializes the class

	:param max: Maximum value plus one until cycling
	:returns: object
	"""
	def __init__(self, max):
		self.__index = -1
		self.__max = max
	
	"""Increments internal counter by one.

	:returns: Incremented internal counter
	"""
	def __inc(self):
		self.__index = (self.__index + 1) % self.__max
		return self.__index

	"""Returns the internal counter previously incremented

	:returns: Internal counter as str
	"""
	def __str__(self):
		return str(self.__inc())
