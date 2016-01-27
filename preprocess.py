import sys
import os
import re
class Preprocess:
	def __init__(self,pathlist):
		self.pathlist=pathlist
		self.stoplist=["subject:",":",",",".","the","of","and","to","a","an","for"] ##list of words that should be ignored
	def process(self):
		output=""
		for file_path in self.pathlist:
			##one directory
			file_out=open(file_path[file_path.rfind("/")+1:]+".out","w")
			file_out.write(str(len(os.listdir(file_path)))+"\n")
			for file_in_name in os.listdir(file_path):
				file_in=open(os.path.join(file_path,file_in_name))
				file_out.write(' '.join([self.check(word) for word in file_in.read().split()]))

	def check(self,word):
		word=word.lower();
		##if re.match('\d',word):
		##	print word
		if word in self.stoplist:
			return ""
		return word

	def output(self):
		return open(self.pathlist[0][self.pathlist[0].rfind("/")+1:]+".out","r").read()
if __name__ == '__main__':
	if len(sys.argv)==1:
		print "at least one class is requried(normally two actually)"
		sys.exit()
	p=Preprocess(sys.argv[1:])
	p.process()
	print p.output()