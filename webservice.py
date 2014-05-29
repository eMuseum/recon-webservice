from bottle import route, run, request, os, static_file
from os import path, makedirs, SEEK_END, SEEK_SET
from view import View
import neuralnet
import autoincrement


"""Checks if a file was uploaded

:param field_name: HTTP input name
:returns: True if it was uploaded
"""
def has_uploaded(field_name):
	return request.files.get(field_name) != None


"""Tests whether the uploaded file is within max size
Must be called after a successful has_uploaded

:param field_name: HTTP input name
:returns: True if it does not exceed
"""
def check_upload_size(field_name, max_size):
	file = request.files.get(field_name).file
	file.seek(0, SEEK_END)
	result = file.tell() < max_size
	file.seek(0, SEEK_SET)
	return result
	

"""Does the actual saving and processing of the upload

:param field_name: HTTP input name
:returns: ID of the recognized image
"""
def parse_upload(field_name):
	# File fetching
	upload = request.files.get(field_name)
	name, ext = os.path.splitext(upload.filename)
	ext = ext.lower()

	# Extension checking
	if ext not in ('.png','.jpg','.jpeg'):
		return 'File extension not allowed.'

	# Save and recognize
	save_path = 'images/' + str(image_index) + ext
	upload.save(save_path, overwrite=True)
	return nn.recognize(save_path)


"""Performs the image saving after a POST event is received

:returns: Database ID of the recognized image
"""
@route('/android', method='POST')
def do_android_upload():
	if not has_uploaded('upload'):
		return '-1'
	
	if not check_upload_size('upload', 3 * 1024 * 1024):
		return '-1'
	
	return str(parse_upload('upload'))


"""Performs the image saving after a POST event is received

:returns: A complete template
"""
@route('/upload', method='POST')
def do_normal_upload():
	if not has_uploaded('upload'):
		return View('no_upload').render()	
	
	if not check_upload_size('upload', 3 * 1024 * 1024):	
		return View('upload_size').render()		
	
	id = parse_upload('upload')
	return View('recognize', { 'id' : id, 'name' : nn.get_name_by_id(id) } ).render()



"""Webservice index page

:returns: Parsed template of the website
"""
@route('/')
def index():
	return View('index').render()


"""Returns an static file, such as CSS files, JS and fonts

:returns: Static file
"""
@route('/static/:path#.+#', name='static')
def static(path):
	return static_file(path, root='static')
	

# Setup a few variables
image_index = autoincrement.Autoincrement(1000)
nn = neuralnet.Neuralnet()

# Check if images directory exists, and if not create it
if not path.exists('images'):
	makedirs('images')

# Runs on a PasteServer, since it's multithreaded, thus allowing to serve more
# than one request and not blocking due to I/O operations performed by the
# neuralnet
run(host='0.0.0.0', port=8080, server='paste')
