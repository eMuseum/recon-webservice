from bottle import route, run, request, static_file, response, HTTPError
from os import path, makedirs, remove
from view import View
from upload import Upload
import neuralnet


"""Does the actual saving and processing of the upload

:param field_name: HTTP input name
:returns: ID of the recognized image
"""
def parse_upload(upload):
	# Save and recognize
	save_path = 'images/' + str(upload)
	upload.save(save_path, overwrite=True)
	return nn.recognize(save_path)


"""Performs the image saving after a POST event is received

:returns: Database ID of the recognized image
"""
@route('/android', method='POST')
def do_android_upload():
	upload = Upload('upload', ('.png','.jpg','.jpeg'), 3 * 1024 * 1024)
	if not upload.has_uploaded():
		return '-1'
	
	if not upload.check_upload_size():
		return '-1'
	
	if not upload.check_extension():
		return '-1'
	
	return str(parse_upload(upload))


"""Performs the image saving after a POST event is received

:returns: A complete template
"""
@route('/upload', method='POST')
def do_normal_upload():
	upload = Upload('upload', ('.png','.jpg','.jpeg'), 3 * 1024 * 1024)
	if not upload.has_uploaded():
		return View('no_upload').render()	
	
	if not upload.check_upload_size():
		return View('upload_size').render()
		
	if not upload.check_extension():
		return View('upload_extension').render()
	
	id = parse_upload(upload)
	if id == -1:
		return View('recognize_failed', { 'img' : str(upload) } ).render()
	
	return View('recognize', { 'id' : id, 'name' : nn.get_name_by_id(id), 'img' : str(upload) } ).render()



"""Webservice about page

:returns: Parsed template of the website
"""
@route('/about')
def about():
	return View('about').render()


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
	response.headers['Cache-Control'] = 'public, max-age=86400'
	return static_file(path, root='static')


"""Returns an image and deletes it

:returns: Image file
"""
@route('/images/<filename>', name='images')
def static(filename):
	file = static_file(filename, root='images')
	if not isinstance(file, HTTPError):
		remove('images/' + filename)
	
	return file
	

# Setup a few variables
nn = neuralnet.Neuralnet()

# Check if images directory exists, and if not create it
if not path.exists('images'):
	makedirs('images')

# Runs on a PasteServer, since it's multithreaded, thus allowing to serve more
# than one request and not blocking due to I/O operations performed by the
# neuralnet
run(host='0.0.0.0', port=8080, server='paste')
