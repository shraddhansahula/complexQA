from __future__ import division
from nltk.corpus import wordnet as wn
import nltk



query = "Describe steps taken and worldwide reaction prior to introduction of the Euro on January 1, 1999."
candidate = "The Frankfurt-based body said in its annual study released today that it has decided on two themes for the new currency: history of Euopean civilization and abstract or concrete paintings."
candidate = "Despite skepticism about the actual realization of a single European currency as scheduled on January 1, 1999, preparation for the design of the Euqo note have already begun."
tagList = ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ','RB','RBR','RBS','JJ','JJR','JJS']
print "Query Sentence"
print query
print "\n"
print "Cancdidate Sentence"
print candidate
print "\n"
#q = nltk.word_tokenize(query)
#c = nltk.word_tokenize(candidate)
# print q
# print c
def tagcheck(a):
    if a in tagList:
        return 1
    else:
        return 0


def pool(l):
    ans = []
    for i,j in enumerate(l):
        #print i,j
        if tagcheck(j[1]) == 1:
            for w in wn.synsets(j[0]):
                
                for lemma in w.lemmas():
                    sent = []
                    sentence = ""
                    #print w.name()
                    for k in range(0,len(l)):
                        if k==i:
                            sent.append(lemma.name())
                        else:
                            sent.append(l[k][0])

                    sentence = " ".join(sent)
                    ans.append(sentence)

    return ans

def skip(k):
	ans = []
	count = 0
	for i, w in enumerate(k):
		for j in range(1,5):
			if i+j < len(k):
				ans.append((k[i], k[i+j]))
				count = count + 1
	return ans, count


qList = nltk.word_tokenize(query)
qList = nltk.pos_tag(qList)
qPool = pool(qList)
qPool.append(query)

cList = nltk.word_tokenize(candidate)
cList = nltk.pos_tag(cList)
cPool = pool(cList)
cPool.append(candidate)

for j in qPool:
	cQ = 0
	j = nltk.word_tokenize(j)
	j, cQ = skip(j)
	maxQ = 0 
	for i in cPool:
		cC = 0
		i = nltk.word_tokenize(i)
		i, cC = skip(i)
		score = 0
		maxC = 0 
		for q in j:
			for c in i:
				if q==c:
					score = score + 1
		R = score/cC
		P = score/cQ
		F = 0.5*R + 0.5*P
		if maxC < F:
			maxC = F
	if maxQ < maxC:
		maxQ = maxC
print "Skip Bi-gram score\n"
print maxQ/3