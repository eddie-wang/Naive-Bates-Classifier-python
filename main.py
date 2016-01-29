import sys
import os
from  nbpreprocess import Preprocess
from  nbclassify import Nbclassify
from nbtraing import Nbtraing
if __name__=="__main__":
	##read a direcotry and use nb classify and evaluate the result using f-measure
	p=Preprocess(sys.argv[1:3])
	p.process()
	nbtraing=Nbtraing(sys.argv[1:3])
	nbtraing.train()
	classifier=Nbclassify("nb.model");
	test_path=sys.argv[3]
	tp=0;fp=0;fn=0;
	for f in os.listdir(test_path):
		result=classifier.classify(os.path.join(test_path,f))
		origin="spam" if "spm" in f else "ham"
		if origin==result=="spam": tp+=1
		if origin=="ham" and result=="spam":fp+=1
		if origin=="spam" and result=="ham":fn+=1

	p=float(tp)/(tp+fp)
	r=float(tp)/(tp+fn)
	print 2*p*r/(r+p)