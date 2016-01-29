import sys
import cPickle
import math
class Nbtraing:
	def __init__(self,files):
		self.file_out=open("nb.model","w")
		self.map={}
		self.number_of_class=len(files)
		self.number_of_word_in_class=[0 for x in range(self.number_of_class)]
		self.number_of_document_in_class=[0 for x in range(self.number_of_class)]
		self.number_of_total_doc=0;
		self.file_in_names=files

	def train(self):
		for index,file_in_name in enumerate(self.file_in_names):
			file_in= open(file_in_name+".out")
			self.number_of_document_in_class[index]=int(file_in.readline());
			self.number_of_total_doc+=self.number_of_document_in_class[index];
			for word in file_in.read().split():
				if not self.map.get(word):
					self.map[word]=[0 for x in range(self.number_of_class)]
				self.map[word][index]+=1
				self.number_of_word_in_class[index]+=1
		self.smooth()
		self.output()
		
	def output(self):
		self.file_out.write(str(self.number_of_class)+"\n")
		##print self.number_of_class
		for n in self.number_of_document_in_class:
			##print n,self.number_of_total_doc
			self.file_out.write(str(math.log(float(n)/self.number_of_total_doc))+"\n")
		for k,v in self.map.items():
			for index in range(len(v)):
				v[index]=math.log(float(v[index])/self.number_of_word_in_class[index])
		self.unknown()
		self.file_out.write(cPickle.dumps(self.map))
		self.file_out.write(cPickle.dumps(self.number_of_word_in_class))
		self.file_out.close()
	def smooth(self):
		##here i choose the add one method to smooth the training data
		word_num=len(self.map)
		self.number_of_word_in_class=map(lambda x:x+word_num , self.number_of_word_in_class)

		for k,v in self.map.items():
			self.map[k]=map(lambda x:x+1 ,v)
	def unknown(self):
		self.number_of_word_in_class=[ math.log(1.0/(x+1)) for x in self.number_of_word_in_class]

if __name__ == '__main__':
	if len(sys.argv)<3:
		print "there must be at least one input file and one output file"
	nbtraing=Nbtraing(sys.argv[1:])
	nbtraing.train()