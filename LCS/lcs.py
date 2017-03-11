from __future__ import division
from nltk.corpus import wordnet as wn
import nltk



query = "Describe steps taken and worldwide reaction prior to introduction of the Euro on January 1, 1999."
candidate = "The Frankfurt-based body said in its annual study released today that it has decided on two themes for the new currency: history of Euopean civilization and abstract or concrete paintings."
candidate = "Despite skepticism about the actual realization of a single European currency as scheduled on January 1, 1999, preparation for the design of the Euro note have already begun."
tagList = ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ','RB','RBR','RBS','JJ','JJR','JJS']
q = nltk.word_tokenize(query)
c = nltk.word_tokenize(candidate)
print "Query Sentence"
print query
print "\n"
print "Cancdidate Sentence"
print candidate
print "\n"

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


qList = nltk.word_tokenize(query)
qList = nltk.pos_tag(qList)
qPool = pool(qList)
qPool.append(query)

cList = nltk.word_tokenize(candidate)
cList = nltk.pos_tag(cList)
cPool = pool(cList)
cPool.append(candidate)

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result.append(a[x-1])
            x -= 1
            y -= 1
    return len(result)

def wlcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                #print x,y
                lengths[i+1][j+1] = lengths[i][j] + 1
            # else:
            #     lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = []
    maX = 0
    x, y = len(a), len(b)
    for i in range(0,x+1):
        for j in range(0,y+1):
            if lengths[i][j] > maX:
                maX = lengths[i][j]
    # print lengths
    # while x != 0 and y != 0:
    #     if lengths[x][y] == lengths[x-1][y]:
    #         x -= 1
    #     elif lengths[x][y] == lengths[x][y-1]:
    #         y -= 1
    #     else:
    #         assert a[x-1] == b[y-1]
    #         print a[x-1], b[y-1]
    #         result.append(a[x-1])
    #         x -= 1
    #         y -= 1
    return maX


#print wlcs(q,c)/len(q)
lcsMaxC = 0
lcsMaxQ = 0
wlcsMaxC = 0
wlcsMaxQ = 0
#print lcs(q,c)
for j in qPool:
    j = nltk.word_tokenize(j)
    #print lcs(j,c)
    lcsMaxC = 0
    wlcsMaxC = 0
    for i in cPool:
        i = nltk.word_tokenize(i)
        Rlcs = lcs(j, i)/len(i)
        Plcs = lcs(j, i)/len(j)
        #print R, P
        Flcs = 0.5*Rlcs + 0.5*Plcs
        Rwlcs = wlcs(j, i)/len(i)
        Pwlcs = wlcs(j, i)/len(j)
        Fwlcs = 0.5*Rwlcs + 0.5*Pwlcs
        if lcsMaxC < Flcs:
            lcsMaxC = Flcs
        if wlcsMaxC < Fwlcs:
            wlcsMaxC = Fwlcs

    if lcsMaxQ < lcsMaxC:
        lcsMaxQ = lcsMaxC
    if wlcsMaxQ < wlcsMaxC:
        wlcsMaxQ = wlcsMaxC
print "LCS Score\n"
print lcsMaxQ
print "\nWLCS Score\n"
print wlcsMaxQ