import numpy as np

# Make sure that caffe is on the python path:
caffe_root = '/usr/local/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe
import caffe.imagenet

try:
   import cPickle as pickle
except:
   import pickle
  
class Neuralnet:
	imagesIDs = [-1,6,3,4,14,1,2,16,7,9,10,8,13,11,15,5,12]
	imagesNames = ["","Guernica","El abside de san clemente","El dormitorio de arles","Paisage catalan","ciencia y caridad", "condensation cube","retrat de la tia pepa","la masia","la minotauromaquia","la noche estrellada","las meninas","la ultima cena","la persistencia de la memoria","port alguer","el gran masturbador","la tentacion de san antonio"]

	def __init__(self):
		self.net = caffe.imagenet.ImageNetClassifier(caffe_root + 'examples/imagenet/imagenet_deploy.prototxt',
                                        caffe_root + 'examples/imagenet/caffe_reference_imagenet_model')
		self.net.caffenet.set_phase_test()
		self.net.caffenet.set_mode_cpu()

		with open(caffe_root + 'data/pis_12/clf', 'rb') as handle:
			self.clf = pickle.load(handle)
		
		
	def recognize(self, filePath):
		# Get features from image
		scores = self.net.predict(filePath)
		feat = self.net.caffenet.blobs['fc6'].data[4]
		
		# Get prediction
		feat = feat.flatten()
		y = self.clf.predict(feat)[0]
		#p = clf.predict_proba(feat)[0]
		return self.imagesIDs[y]
