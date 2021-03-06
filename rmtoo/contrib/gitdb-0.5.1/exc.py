"""Module with common exceptions"""
from util import to_hex_sha

class ODBError(Exception):
	"""All errors thrown by the object database"""
	
class InvalidDBRoot(ODBError):
	"""Thrown if an object database cannot be initialized at the given path"""
	
class BadObject(ODBError):
	"""The object with the given SHA does not exist. Instantiate with the 
	failed sha"""
	
	def __str__(self):
		return "BadObject: %s" % to_hex_sha(self.args[0])

class AmbiguousObjectName(ODBError):
	"""Thrown if a possibly shortened name does not uniquely represent a single object
	in the database"""

class BadObjectType(ODBError):
	"""The object had an unsupported type"""

class UnsupportedOperation(ODBError):
	"""Thrown if the given operation cannot be supported by the object database"""
