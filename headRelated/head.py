from __future__ import division
import StanfordDependencies
from practnlptools.tools import Annotator
from nltk.corpus import wordnet as wn
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

lmt = WordNetLemmatizer()

sd = StanfordDependencies.get_instance(backend='subprocess')
a = Annotator()

query = "Describe steps taken and worldwide reaction prior to introduction of the Euro on January 1, 1999. Include predictions and expectations reported in press."
candidate = "The Frankfurt-based body said in its annual report released today that it has decided on two themes for the new currency: history of Euopean civilization and abstract or concrete paintings."
print "Query Sentence"
print query
print "\n"
print "Cancdidate Sentence"
print candidate
print "\n"
synTree = a.getAnnotations(query)['syntax_tree']

tokens = sd.convert_tree(synTree)
queue = []
for i, token in enumerate(tokens):
	if token[6] == 0:
		queue.append((i+1,token))

qHeadWords = []
while queue != []:
	s = queue[0]
	queue.remove(s)
	flag = 0
	#print s[1][1], s[0]
	for i, word in enumerate(tokens):
		if word[6] == s[0]:
			flag = 1
			queue.append((i+1, word))
	if flag == 1:
		qHeadWords.append(lmt.lemmatize(s[1][1],'v'))


synTree = a.getAnnotations(candidate)['syntax_tree']

tokens = sd.convert_tree(synTree)
queue = []
for i, token in enumerate(tokens):
	if token[6] == 0:
		queue.append((i+1,token))

cHeadWords = []
while queue != []:
	s = queue[0]
	queue.remove(s)
	flag = 0
	#print s[1][1], s[0]
	for i, word in enumerate(tokens):
		if word[6] == s[0]:
			flag = 1
			queue.append((i+1, word))
	if flag == 1:
		cHeadWords.append(lmt.lemmatize(s[1][1], 'v'))

queryRel = []
for word in qHeadWords: 
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

candidateRel = []
for word in cHeadWords: 
	for i,j in enumerate(wn.synsets(word)):
		for l in j.lemmas():
			candidateRel.append(l.name())
		#queryRel.append(l.lemma_names() for l in j.hypernyms())
		for l in j.hypernyms():
			for k in l.lemma_names():
				candidateRel.append(k)
		for l in j.hyponyms():
			for k in l.lemma_names():
				candidateRel.append(k)

exactHeadScore = 0
count = 0
for j in cHeadWords:
	count = count + 1
	for i in qHeadWords:
		#print i,j
		if i==j:
			exactHeadScore = exactHeadScore + 1

exactHeadScore = exactHeadScore/count
print "Exact Head Score\n"
print exactHeadScore

relHeadScore = 0
count = 0
for j in candidateRel:
	count = count + 1
	if j in queryRel:
		relHeadScore = relHeadScore + 1

relHeadScore = relHeadScore/count
print "Relative Head Score\n"
print relHeadScore



