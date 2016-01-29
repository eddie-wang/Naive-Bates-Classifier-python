import cPickle
import sys
from  nbpreprocess import Preprocess
class Nbclassify:
	def __init__(self,mdoel_file):
		self.model_file=open(mdoel_file,"r")
		self.class_number = int(self.model_file.readline())
		self.p_classes=[]
		for x in xrange(self.class_number):
			self.p_classes.append(float(self.model_file.readline()))
		self.map=cPickle.load(self.model_file)
		self.p_unknown=cPickle.load(self.model_file)
		
	def classify(self,classify_file):
		content=Preprocess([]).singlefile(open(classify_file))
		result=0
		max_probability=-2**32
		for cur_class in range(self.class_number):
			cur_probability=self.p_classes[cur_class]
			for word in content.split():
				if word in self.map:
					cur_probability+=self.map[word][cur_class]
				else:
					cur_probability+=self.p_unknown[cur_class]
			if cur_probability>max_probability:
				max_probability=cur_probability
				result=cur_class
		return "spam" if result==0 else "ham" 
if __name__ == '__main__':
	if len(sys.argv)<3:
		print "there must be  one model file"
	nb=Nbclassify(sys.argv[1])
	nb.classify(sys.argv[2])