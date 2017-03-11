from nltk.corpus import wordnet as wn
import nltk

query = "Describe steps taken and worldwide reaction prior to introduction of the Euro on January 1, 1999."
candidate = "The Frankfurt-based body said in its annual study released today that it has decided on two themes for the new currency: history of Euopean civilization and abstract or concrete paintings."

print "Query Sentence"
print query
print "\n"
print "Cancdidate Sentence"
print candidate
print "\n"

tagList = ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ','RB','RBR','RBS','JJ','JJR','JJS']

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


qList = nltk.word_tokenize(query)
qList = nltk.pos_tag(qList)
qPool = pool(qList)
#qPool.append(query)

cList = nltk.word_tokenize(candidate)
cList = nltk.pos_tag(cList)
cPool = pool(cList)

data = query
data = data.split(" ")
queryRel = [] 
for word in data: 
	for i,j in enumerate(wn.synsets(word)):
		for l in j.lemmas():
			queryRel.append(l.name())
		#queryRel.append(l.lemma_names() for l in j.hypernyms())
		for l in j.hypernyms():
			for k in l.lemma_names():
				queryRel.append(k)
		for l in j.hyponyms():
			for k in l.lemma_names():
				queryRel.append(k)

#print queryRel
cSet = nltk.word_tokenize(candidate)
cSet = nltk.pos_tag(cSet)
oneGramScore = 0
for word in cSet:
	#print word[0],word[1]
	score = 0
	wordCount = cSet.count(word)
	if tagcheck(word[1]) == 1:
		if word[0] in queryRel:
			score = score + 1
		score = score/wordCount
		oneGramScore = oneGramScore + score
print "1-Gram score\n"
print oneGramScore
