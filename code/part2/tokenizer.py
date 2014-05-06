from porter_stemmer import PorterStemmer
import re
import string

class Tokenizer(object):
	def __init__(self):
		self.stemmer = PorterStemmer()

	def process_tweet(self, tweet):
        #TODO: pre-process tweet
        # this is a helper function for __call__
		
		toreturn = []
		
		for word in tweet.lower().encode('utf-8').split():
			word = re.sub(r'([a-z])\1\1+',r'\1\1',word)
			toreturn.append(word)

		return toreturn

	def __call__(self, doc):
    	# this function will tokenize the given document and return a list of extracted features (tokens)
		processed_doc = self.process_tweet(doc)
        #TODO: return a list of features extracted from processed_doc 
		return processed_doc
