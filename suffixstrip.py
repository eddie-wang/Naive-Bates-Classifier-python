"""
Implementation of suffix stripping algorithms 
Reference :http://tartarus.org/martin/PorterStemmer/def.txt
Author: Xiaohui Wang
"""
import sys
class suffixstrip:
	def __init__(self,word):
		self.word=word

	def isVowel(self,index):
		if self.word[index]=='a' or self.word[index]=='e' or self.word[index]=='i' or self.word[index]=='o'or self.word[index]=='u':
			return True
		if self.word[index]=='y' and index>0 and isConsonant(self.word[index-1]):
			return True

		return False
	def isConsonant(self,index):
		return not self.isVowel(index)
	def m(self,end):
		result=0
		i=self.getC(0,end)
		while True:
			i=self.getV(i,end)
			if i>=len(self.word)+end: break
			i=self.getC(i,end)
			result+=1
		return result

	def getC(self,i,end):
		while i<len(self.word)+end and self.isConsonant(i):
			i+=1
		return i
	def getV(self,i,end):
		while i<len(self.word)+end and self.isVowel(i):
			i+=1
		return i

	def containVowel(self,end):
		for i in range(len(self.word)+end):
			if self.isVowel(i):
				return True
		return False

	def endsDoubleConstant(self):
		return self.isConsonant(-1) and self.isConsonant(-2)

	def endCvc(self,end):
		return self.isConsonant(-1+end) and (self.word[-1+end] in ["w","x","y"]) and self.isVowel(-2+end) and self.isConsonant(-3+end)

	def step1ab(self):
		"""
		step1ab() gets rid of plurals and -ed or -ing.

		Step 1a

		SSES -> SS                         caresses  ->  caress
		IES  -> I                          ponies    ->  poni
										   ties      ->  ti
		SS   -> SS                         caress    ->  caress
		S    ->                            cats      ->  cat

		Step 1b

		(m>0) EED -> EE                    feed      ->  feed
										   agreed    ->  agree
		(*v*) ED  ->                       plastered ->  plaster
										   bled      ->  bled
		(*v*) ING ->                       motoring  ->  motor
										   sing      ->  sing
		"""

		if self.word.endswith("sses") or  self.word.endswith("ies"):
			self.word=self.word[:-2]
		elif self.word[-1]=='s' and self.word[-2]!='s':
			self.word=self.word[:-1]

		if self.word.endswith("eed"):
			if self.m(-3)>0 :
				self.word=self.word[:-1]
		elif self.word.endswith("ed"):
			if self.containVowel(-2):
				self.word=self.word[:-2]
				self.step1abSuc()
		elif self.word.endswith("ing"):
			if self.containVowel(-3):
				self.word=self.word[:-3]
				self.step1abSuc()
	def step1abSuc(self):
		if self.word[-2:] in ["at","bl","iz"]:
			self.word=self.word+"e"
		if self.endsDoubleConstant() and (self.word[-1] in ["l","s","z"]):
			self.word=self.word[:-1]
		if self.endCvc() and self.m(0)==1:
			self.word=self.word+"e"
	def step1c(self):
		if self.word[-1]=="y" and self.containVowel(-1):
			self.word=self.word[:-1]+'i'
	def step2(self):
		"""step2() maps double suffices to single ones.
		so -ization ( = -ize plus -ation) maps to -ize etc. note that the
		string before the suffix must give m() > 0.
		"""
		if self.word.endswith("ational"):
			if self.m(-7)>0:self.word=self.word[:-5]+"e"
		elif self.word.endswith("tional"):
			if self.m(-6)>0:self.word=self.word[:-2]
		elif self.word.endswith("encl"):
			if self.m(-4)>0:self.word=self.word[:-1]+"e"
		elif self.word.endswith("ancl"):
			if self.m(-4)>0:self.word=self.word[:-1]+"e"
		elif self.word.endswith("izer"):
			if self.m(-4)>0:self.word=self.word[:-1]
		elif self.word.endswith("abli"):
			if self.m(-4)>0:self.word=self.word[:-1]+"e"
		elif self.word.endswith("alli"):
			if self.m(-4)>0:self.word=self.word[:-2]
		elif self.word.endswith("entli"):
			if self.m(-5)>0:self.word=self.word[:-2]
		elif self.word.endswith("eli"):
			if self.m(-3)>0:self.word=self.word[:-2]
		elif self.word.endswith("ousli"):
			if self.m(-5)>0:self.word=self.word[:-2]
		elif self.word.endswith("ization"):
			if self.m(-7)>0:self.word=self.word[:-5]+"e"
		elif self.word.endswith("ation"):
			if self.m(-5)>0:self.word=self.word[:-3]+"e"
		elif self.word.endswith("ator"):
			if self.m(-4)>0:self.word=self.word[:-2]+"e"
		elif self.word.endswith("alism"):
			if self.m(-5)>0:self.word=self.word[:-3]
		elif self.word.endswith("iveness"):
			if self.m(-7)>0:self.word=self.word[:-4]
		elif self.word.endswith("fulness"):
			if self.m(-7)>0:self.word=self.word[:-4]
		elif self.word.endswith("ousness"):
			if self.m(-7)>0:self.word=self.word[:-4]
		elif self.word.endswith("aliti"):
			if self.m(-5)>0:self.word=self.word[:-3]
		elif self.word.endswith("iviti"):
			if self.m(-5)>0:self.word=self.word[:-3]+"e"
		elif self.word.endswith("biliti"):
			if self.m(-6)>0:self.word=self.word[:-5]+"le"
	def step3(self):
		"""step3() dels with -ic-, -full, -ness etc. similar strategy to step2."""
		if self.word.endswith("icate"):
			if self.m(-5)>0:self.word=self.word[:-3]
		elif self.word.endswith("ative"):
			if self.m(-5)>0:self.word=self.word[:-5]
		elif self.word.endswith("alize"):
			if self.m(-5)>0:self.word=self.word[:-3]
		elif self.word.endswith("iciti"):
			if self.m(-5)>0:self.word=self.word[:-3]
		elif self.word.endswith("ical"):
			if self.m(-4)>0:self.word=self.word[:-2]
		elif self.word.endswith("ful"):
			if self.m(-3)>0:self.word=self.word[:-3]
		elif self.word.endswith("ness"):
			if self.m(-4)>0:self.word=self.word[:-4]
	def step4(self):
		"""step4() takes off -ant, -ence etc., in context <c>vcvc<v>."""
		suffixs=["al","ance","ence","er","ic","able","ible","ant","ement","ment","ent","ou","ism","ate","iti","ous","ive","ize"]
		for s in suffixs:
			if self.word.endswith(s) and self.m(-len(s))>1:
				self.word=self.word[:-len(s)]
				break
		if self.word.endswith("ion") and self.m(-3)>1 and (self.word[-4] in ["s","t"]):
			self.word=self.word[:-len(s)]
	
	def step5a(self):
		if self.word.endswith("e"):
			if self.m(-1)>1:self.word=self.word[:-1]
			elif self.m(-1)==1 and not self.endCvc(-1): self.word=self.word[:-1]
	def step5b(self):
		if self.word.endswith("ll") and self.m(-2)>1:
			self.word=self.word[:-1]
	def stem(self):
		self.step1ab()
		self.step1c()
		self.step2()
		self.step3()
		self.step4()
		self.step5a()
		self.step5b()
		return self.word


if __name__ == '__main__':
	s=suffixstrip(sys.argv[1])
	print s.stem()
