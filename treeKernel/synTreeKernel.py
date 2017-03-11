import bllipparser
from bllipparser import RerankingParser
from nltk import Tree

score = 0




rrp = RerankingParser.fetch_and_load('WSJ-PTB3', verbose=True)

query = "Include predictions and expectations reported in press."
candidate = "Europe's new currency, the euro, will rival the U.S. dollar as an international currency over the long term, Der Speigel magazine reported Sunday."

print "Query Sentence"
print query
print "\n"
print "Cancdidate Sentence"
print candidate
print "\n"

query = rrp.simple_parse(query)
candidate = rrp.simple_parse(candidate)

qTree = bllipparser.Tree(query)
cTree = bllipparser.Tree(candidate)

def calScore(q, c):
	prod1 = []
	prod2 = []
	pre1 = q.is_preterminal()
	pre2 = c.is_preterminal()
	S = 1
	if pre1==False:
		for l in q[0]:
			prod1.append(l.label)
	if pre2==False:
		for l in c[0]:
			prod2.append(l.label)
	s = 0
	different = 0
	if len(prod1) != len(prod2):
		different = 1
	else:
		for i in range(0,len(prod1)):
			if(prod1[i] != prod2[i]):
				different = 1
				break
	if different == 1 :
		return 0

	if pre1 == True and pre2 == True:
		if c.token == q.token:
			#print c.token, q.token
			return 1
	else:
		for j in q:
			for i in c:
				s = (1 + calScore(j, i))
				#print s
		S = S*s
	return S



for sub1 in qTree.all_subtrees():
	for sub2 in cTree.all_subtrees():
		score = score + calScore(sub1, sub2)
print "Tree kernel score"
print score/7.6



