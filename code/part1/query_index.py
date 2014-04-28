import sys
import math
import json


def main():
	print 'Processing Inverted Index...'
	# first read in the inverted index file
	inverted_index_file = open(sys.argv[1])
	inverted_index = json.loads(inverted_index_file.readline())

	print 'Processing Business Data...'
	business_index = {}
	business_file = open(sys.argv[2])
	for line in business_file.readlines():
		data = json.loads(line.replace("\n",""))
		business_index[data['business_id']] = data

	print 'Processing Stopwords...'
	stopfile = open(sys.argv[3])
	stopwords = [line.strip() for line in stopfile]

	print 'Enter search terms:'
	line = sys.stdin.readline()
	while line:
		businesses = []
		if line[0] == '"' and line[len(line)-1] == '"':
			#phrase query
			line.replace('"', '')
			words = line.strip().split()
			#TODO - finish
		
		# one word / free text queries
		else:
			words = line.strip().split()
			ignored = 0
			businesses_temp = {x:0 for x in inverted_index[words[0]]}
			for w in words:
				if w not in stopwords:
					for b in inverted_index[w]:
						businesses_temp[b] += 1
				else:
					ignored += 1
			
			# find the businesses whose reviews contained all the words
			for k, v in businesses_temp.iteritems():	
				if v == (len(words) - ignored):
					businesses.append(k)
		print 'matches',businesses
		line = sys.stdin.readline()	
		#return rank(businesses, words)	


def rank(businesses, words):
	tfidf = {x: 0 for x in businesses}
	for w in words:
		for b in businesses:
			reviews = inverted_index[w][b]
			tf = 0
			
			data = business_index[b]
			total_reviews = data["review_count"]

			#num of reviews in which word appears		
			relevant_reviews = len(reviews)
			for k, v in enumerate(reviews):
				tf += len(v)

			idf = math.log(total_reviews / relevant_reviews)
			tfidf[b] += tf * idf
			#TODO - add other heuristics 
	
	#TODO - sort tfidf dict by values and then figure out what we actually want to return
	return None #scores


if __name__ == '__main__':
	main()

