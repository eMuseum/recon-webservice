from bottle import route, run, template, request, os
from os import path, makedirs
import neuralnet
import autoincrement

"""Performs the image saving after a POST event is received

:returns: Database ID of the recognized image
"""
@route('/upload', method='POST')
def do_upload():
	# File fetching
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    ext = ext.lower()

	# Extension checking
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

	# Save and recognize
    save_path = 'images/' + str(image_index) + ext
    upload.save(save_path, overwrite=True)
    id = nn.recognize(save_path)

    return str(id)

"""Webservice index page

:returns: Parsed template of the website
"""
@route('/')
def index():
	return template('index')

image_index = autoincrement.Autoincrement(1000)
nn = neuralnet.Neuralnet()

# Check if images directory exists, and if not create it
if not path.exists('images'):
	makedirs('images')

# Runs on a PasteServer, since it's multithreaded, thus allowing to serve more
# than one request and not blocking due to I/O operations performed by the
# neuralnet
run(host='0.0.0.0', port=8080, server='paste')