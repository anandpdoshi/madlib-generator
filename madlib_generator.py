# code developed by Jackie Cohen; revised by Paul Resnick and Colleen Van Lent
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