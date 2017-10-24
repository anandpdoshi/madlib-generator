# code developed by Jackie Cohen; revised by Paul Resnick
# cleanup by Anand Doshi

import nltk
# nltk requires some downloading/installing dependencies to use all its features;
# numpy is especially tricky to install

import random

debug = False #True

def read_file(fname=None):
    # Here is a comment for SI206
    # get file from user to make mad lib out of
    if debug:
    	print "Getting information from file madlib_test.txt...\n"

    if not fname:
        fname = "madlib_test.txt" # need a file with this name in directory

    with open(fname, 'r') as f:
        para = f.read()

    return para

def tokenize(para):
    tokens = nltk.word_tokenize(para)
    tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
    if debug:
    	print "First few tagged tokens are:"
    	for tup in tagged_tokens[:5]:
    		print tup

    return tagged_tokens

def ask_and_substitute(tagged_tokens):
    tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
    substitution_probabilities = {"NN":.1,"NNS":.2,"VB":.25,"JJ":.25}


    final_words = []

    for (word, tag) in tagged_tokens:
    	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
    		final_words.append(spaced(word))
    	else:
    		new_word = raw_input("Please enter %s:\n" % (tagmap[tag]))
    		final_words.append(spaced(new_word))

    return final_words


def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

def run():
    para = read_file()
    tagged_tokens = tokenize(para)
    final_words = ask_and_substitute(tagged_tokens)
    print "".join(final_words)

if __name__ == '__main__':
    run()
