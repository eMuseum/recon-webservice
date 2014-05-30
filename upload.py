from bottle import request
from os import path, makedirs, SEEK_END, SEEK_SET
from time import time
import autoincrement

class Upload:
	index = autoincrement.Autoincrement(100)

	def __init__(self, field_name, extensions, max_size):
		self.file_upload = request.files.get(field_name)
		self.extensions = extensions
		self.max_size = max_size
		self.hash_name = ''
		
		if self.file_upload != None:
			self.name, ext = path.splitext(self.file_upload.filename)
			self.ext = ext.lower()
		else:
			self.name, self.ext = '', ''
	
	"""Checks if a file was uploaded

	:returns: True if it was uploaded
	"""
	def has_uploaded(self):
		return self.file_upload != None


	"""Tests whether the uploaded file is within max size
	Must be called after a successful has_uploaded

	:returns: True if it does not exceed
	"""
	def check_upload_size(self):
		file = self.file_upload.file
		file.seek(0, SEEK_END)
		result = file.tell() < self.max_size
		file.seek(0, SEEK_SET)
		return result
	
	
	"""Tests whether the uploaded file extension is in the
		extensions whitelist

	:returns: True if extension is valid
	"""
	def check_extension(self):
		# Extension checking
		return self.ext in self.extensions
	
	
	"""Returns a unique hash of the file as string
	
	:returns: Unique hash
	"""
	def __str__(self):
		if self.hash_name == '':
			self.hash_name = str(time()) + self.name + str(Upload.index) + self.ext
		return self.hash_name
	

	"""Saves the upload"""
	def save(self, *args, **kwargs):
		return self.file_upload.save(*args, **kwargs)
