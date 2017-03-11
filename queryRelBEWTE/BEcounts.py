from __future__ import division
from nltk.corpus import wordnet as wn
from nltk.corpus import treebank
from itertools import chain
import os
import collections
from math import log
import pickle


prepositions = ['when','whenever','where','wherever','while','even','though','lest','since','that','though','till','unless','until','than','because','before','after','although','long','much','soon','though','if','so','aboard','about','above','across','after','against','along','amid','among','anti','around','as','at','before','behind','below','beneath','beside','besides','between','beyond','but','by','concerning','considering','despite','down','during','except','excepting','excluding','following','for','from','in','inside','into','like','minus','near','of','off','on','onto','opposite','outside','over','past','per','plus','regarding','round','save','since','than','through','to','toward','towards','under','underneath','unlike','until','up','upon','versus','via','with','within','without']
#filePoint = open("../input/start.1.1", "r")
data = "Discuss conditions on American Indian reservations or among Native American communities. Include the benefits and drawbacks of the reservation system. Include legal privileges and problems."
print "Query Sentence"
print data
print "\n"
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
	
listOfTags = []
for word, tag in treebank.tagged_words():
	if tag not in listOfTags:
		listOfTags.append(tag)
#print queryRel
#print listOfTags

#filePoint2= open("../output/BEXs/00000000/start.2.1")
#print "Candidate Sentence"
#candidate = "The Frankfurt-based body said in its annual report released today that it has decided on two themes for the new currency: history of Euopean civilization and abstract or concrete paintings."

# print candidate
# print "\n"

BEcounts = collections.Counter()

os.chdir("../output/BEXs/00000000")
listOfFiles = os.listdir(".")
for bex in listOfFiles:
	with open(bex, "r") as f:
		for line in f:
			line = line.split("|")
			line = line[1:-1]
			line = [w for w in line if w not in listOfTags]
			line = [w for w in line if w not in prepositions]
			BEcounts.update(zip(line,line[1:]))
os.chdir("../../../queryRel")
out = open("BEcounts", "wb")
pickle.dump(BEcounts, out)
out.close()			


			#print line
		# for line in f:
		# 	beCount = beCount + 1
		# 	line = line.split("|")
			
		# 	for word in line:

		# 		if word in queryRel:
		# 			matchBECount = matchBECount + 1
		# 			#print line
		# 			break





# print "Calculated values."
# print matchBECount, beCount
# print "\n"
# scoreBE = (float)(matchBECount/beCount)
# print "BE score\n"
# print scoreBE