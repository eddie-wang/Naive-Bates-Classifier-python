import cPickle
import sys
from  nbpreprocess import Preprocess
class Nbclassify:
	def __init__(self,files):
		self.model_file=open(files[0])
		self.classify_file=open(files[1])
		self.map={}
		self.p_unknown=[]
	def classify(self):
		 
		content=Preprocess([]).singlefile(self.classify_file);
		class_number = int(self.model_file.readline())
		p_classes=[]
		for x in xrange(class_number):
			p_classes.append(float(self.model_file.readline()))
		self.p_unknown=cPickle.load(self.model_file)
		self.map=cPickle.load(self.model_file)
		result=0
		max_probability=-2**32
		print max_probability
		for cur_class in range(class_number):
			cur_probability=p_classes[cur_class]
			for word in content.split():
				if word in self.map:
					cur_probability+=self.map[word][cur_class]
				else:
					cur_probability+=self.p_unknown[cur_class]
			print cur_probability
			if cur_probability>max_probability:
				max_probability=cur_probability
				result=cur_class
		print result
		return result

if __name__ == '__main__':
	if len(sys.argv)<3:
		print "there must be at least one classify file and one model file"
	nb=Nbclassify(sys.argv[1:])
	nb.classify()