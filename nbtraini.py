import sys
import cPickle
import math
class Nbtrain:
	def __init__(self,files):
		self.file_out=open(files[-1],"w")
		self.map={}
		self.number_of_class=len(files)-1
		self.number_of_word_in_class=[0 for x in range(self.number_of_class)]
		self.number_of_document_in_class=[0 for x in range(self.number_of_class)]
		self.number_of_total_doc=0;
		self.file_in_names=files[:-1]

	def train(self):
		for index,file_in_name in enumerate(self.file_in_names):
			file_in= open(file_in_name)
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
		self.file_out.write(str(self.number_of_class))
		print self.number_of_class
		for n in self.number_of_document_in_class:
			print n,self.number_of_total_doc
			self.file_out.write(str(math.log(float(n)/self.number_of_total_doc)))
		for k,v in self.map.items():
			for index in range(len(v)):
				print k,v[index],self.number_of_word_in_class[index]
				v[index]=math.log(float(v[index])/self.number_of_word_in_class[index])
		self.file_out.write(cPickle.dumps(self.map))
	def smooth(self):
		##here i choose the add one method to smooth the training data
		word_num=len(self.map)
		self.number_of_word_in_class=map(lambda x:x+word_num , self.number_of_word_in_class)

		for k,v in self.map.items():
			self.map[k]=map(lambda x:x+1 ,v)
        


if __name__ == '__main__':
	if len(sys.argv)<3:
		print "there must be at least one input file and one output file"
	nbtrain=Nbtrain(sys.argv[1:])
	nbtrain.train()