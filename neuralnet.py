import numpy as np

# Make sure that caffe is on the python path:
caffe_root = '/usr/local/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

try:
   import cPickle as pickle
except:
   import pickle
  
class Neuralnet:
	imagesIDs = [6,3,4,14,1,2,16,7,9,10,8,13,11,15,5,12]
	imagesNames = ["Guernica","El abside de san clemente","El dormitorio de arles","Paisage catalan","ciencia y caridad", "condensation cube","retrat de la tia pepa","la masia","la minotauromaquia","la noche estrellada","las meninas","la ultima cena","la persistencia de la memoria","port alguer","el gran masturbador","la tentacion de san antonio"]

	def __init__(self):
		m = np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy')
		m = m[:, :227, :227]

		self.net = caffe.Classifier(caffe_root + 'models/bvlc_reference_caffenet/deploy.prototxt',
                                        caffe_root + 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel',
                                        mean=m,
                                        channel_swap=(2,1,0),
                                        raw_scale=255,
                                        image_dims=(256,256))

		with open(caffe_root + 'data/pis_12/clf', 'rb') as handle:
			self.clf = pickle.load(handle)
		
		
	def recognize(self, filePath):
		# Get features from image
		image = caffe.io.load_image(filePath)
		scores = self.net.predict([image])
		feat = self.net.blobs['fc7'].data[4]
		
		# Get prediction
		feat = feat.flatten()
		y = self.clf.predict(feat)[0]
		
		# Class -1 is used as error / can't predict
		if y == -1:
			return -1;
		
		return self.imagesIDs[y]

	"""Given an ID, returns the name"
	
	:param id: Image ID
	:returns: Image name
	"""
	def get_name_by_id(self, id):
		return self.imagesNames[self.imagesIDs.index(id)]
