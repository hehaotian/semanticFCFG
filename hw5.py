# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:44:16 2014

@author: haotianhe

LING 571 HW 5

Semantic FCFG Parser
"""

import sys
import nltk
from nltk.tokenize import RegexpTokenizer

if __name__ == "__main__":
    
    if (len(sys.argv) >= 2):
        grammar_path = sys.argv[1]
        sent_path = sys.argv[2]
    else:
        grammar_path = "grammar.fcfg"
        sent_path = "semantics_sentences.txt"
        
    grammar = nltk.data.load('file:' + grammar_path); # loads the grammar
    parser = nltk.parse.FeatureChartParser(grammar) # builds a parser for the grammar
    sents = open(sent_path, 'r') # reads the example sentences
    
    # initialize the counting
#totalParsCount = 0
#sentCount = 0
#parsCount = 0
    
    for line in sents: # reads each sentence
        # print line
        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
        tokens = tokenizer.tokenize(line) # makes each sentence lowercase and splitted
        #sentCount += 1 # counts the number of sentences in this example
    
        trees = parser.nbest_parse(tokens) # parses the given sentence to get parse trees that represent possible structures for the given sentence
        if (len(trees) == 0):
            print ""
        for tree in trees: # prints the parse trees
            print tree.node['SEM'].simplify()
#parsCount += 1 # counts the number of parses for the sentence
            
            #if parsCount == 1: # prints the number of parses under the tree
            #print str(parsCount) + " parse" + "\n"
            #else:
            #print str(parsCount) + " parses" + "\n"

#totalParsCount += parsCount
#parsCount = 0;

#print "The average number of parses per sentence obtained by the grammar is " + str(int(round(totalParsCount/sentCount))) # prints the statement of the performance
    