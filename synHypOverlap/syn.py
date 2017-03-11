from __future__ import division
from nltk.corpus import wordnet as wn
from nltk.corpus import treebank
from itertools import chain
import nltk

query = "Describe steps taken and worldwide reaction prior to introduction of the Euro on January 1, 1999. Include predictions and expectations reported in press."
data = nltk.word_tokenize(query)
print "Query Sentence"
print query
print "\n"

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

candidate = "The Frankfurt-based body said in its annual report released today that it has decided on two themes for the new currency: history of Euopean civilization and abstract or concrete paintings."
print "Cancdidate Sentence"
print candidate
print "\n"
data = nltk.word_tokenize(candidate)
candidateSyn = []
candidateHyp = []
for word in data:
	for i, j in enumerate(wn.synsets(word)):
		for l in j.lemmas():
			candidateSyn.append(l.name())
		for l in j.hypernyms():
			for k in l.lemma_names():
				candidateHyp.append(k)
		for l in j.hyponyms():
			for k in l.lemma_names():
				candidateHyp.append(k)

countSyn = 0
matchSyn = 0
for j in candidateSyn:
	countSyn = countSyn + 1
	if j in queryRel:
		matchSyn = matchSyn + 1

synOverlap = matchSyn/countSyn

countHyp = 0
matchHyp = 0
for j in candidateHyp:
	countHyp = countHyp + 1
	if j in queryRel:
		matchHyp = matchHyp + 1

hypOverlap = matchHyp/countHyp
print "Synonym and hyper/hypo overlap\n"
print synOverlap, hypOverlap

tagList = ['NN','NNS','NNP','NNPS']

def tagcheck(a):
	if a in tagList:
		return 1
	else:
		return 0
data = nltk.word_tokenize(candidate)
data = nltk.pos_tag(data)
glossWords = []
for word in data:

	if tagcheck(word[1]) == 1:
		gDef = ""
		for i in wn.synsets(word[0]): 
			gDef = i.definition()
			#print gDef
			gDef = nltk.word_tokenize(gDef)
			#print gDef
			for w in gDef:
				glossWords.append(w)

#print glossWords

countGloss = 0
matchGloss = 0
for i in glossWords:
	countGloss = countGloss + 1
	if i in queryRel:
		matchGloss = matchGloss + 1
	
glossOverlap = matchGloss/countGloss
print "Gloss overlap\n"
print glossOverlap
