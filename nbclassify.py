import cPickle
class Nbclassify:
	def __init__(self,files):
		self.model_file=open(files[0])
		self.classify_file=open(files[1])
		self.map={}
	def classify():
		preprocess = Preprocess(self.classify_file)
		preprocess.process()
		content=Preprocess.output():
		class_number = int(self.model_file.readline())
		p_classes=[]
		for x in xrange(class_number):
			p_classes.append(float(self.model_file.readline()))
		self.map=cPickle.load(self.model_file.read())
		result=0
		max_probability=0.0
		for cur_class in range(class_number):
			cur_probability=p_classes[cur_class]
			for word in content.split():
				cur_probability+=map[word][cur_class]
			if cur_probability>max_probability:
				max_probability=cur_probability
				result=cur_class
	return result

if __name__ == '__main__':
	if len(sys.argv)<3:
		print "there must be at least one classify file and one model file"
	nb=Nbclassify(sys.argv[1:])
	nb.classify()