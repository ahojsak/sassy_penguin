import re
import string
import porter_stemmer

class Tokenizer(object):

	def __init__(self, sw):
		self.stopwords = sw

	def process_tweet(self, review):
        #TODO: pre-process tweet
        # this is a helper function for __call__
		
		toreturn = []
		regex = re.compile('[%s]' % re.escape(string.punctuation))
		
		for word in regex.sub(' ', review.lower().encode('utf-8')).split():
			#	if word not in self.stopwords:
			word = porter_stemmer.PorterStemmer().stem(word, 0,len(word)-1)
			toreturn.append(word)
		return toreturn

	def __call__(self, doc):
    	# this function will tokenize the given document and return a list of extracted features (tokens)
		processed_doc = self.process_tweet(doc)
        #TODO: return a list of features extracted from processed_doc 
		return processed_doc
