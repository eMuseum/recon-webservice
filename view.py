from bottle import template, default_app

class View(object):
	# Default arguments that get passed to the template
	template_arguments = { 'get_url' : default_app().get_url }

	"""Initializes a View object, used to make the use of templates easier"""
	def __init__(self, template, args = {}):
		self.template = template
		self.args = self.template_arguments
		self.add_arguments(args)
	
	
	"""Renders the given template, including header and footer with
		the previously given arguments
		
	:returns: Rendered view
	"""
	def render(self):
		header = template('header', self.args)
		body = template(self.template, self.args)
		footer = template('footer', self.args)
		return header + body + footer

	
	"""Renders the view by converting when converting to string
	
	:returns: Rendered view
	"""
	def __str__(self):
		return self.render()
	

	"""Add arguments for the template
	
	:param args: Additional arguments
	"""
	def add_arguments(self, args):
		self.args.update(args)
		