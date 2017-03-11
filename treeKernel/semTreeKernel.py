import bllipparser
from bllipparser import RerankingParser
from nltk import Tree
from practnlptools.tools import Annotator

score = 0


annotator = Annotator()

rrp = RerankingParser.fetch_and_load('WSJ-PTB3', verbose=True)

query = "Describe steps taken and worldwide reaction prior to introduction of the Euro on January 1, 1999."
candidate = "Europe's new currency, the euro, will rival the U.S. dollar as an international currency over the long term, Der Speigel magazine reported Sunday."

qListOfDict = annotator.getAnnotations(query)['srl']
cListOfDict = annotator.getAnnotations(candidate)['srl']


qParsed = ['(S1 ']
cParsed = ['(S1 ']

for list in qListOfDict:
	









