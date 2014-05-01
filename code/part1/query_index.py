import sys
import math
import json
import operator
import porter_stemmer
import re,string

# Read in inverted index file, business data file, and stopword file
print 'Processing Inverted Index...'
inverted_index_file = open(sys.argv[1])
inverted_index = json.loads(inverted_index_file.readline())

print 'Processing Business Data...'
business_file = open(sys.argv[2])
business_index = {}
for line in business_file.readlines():
	data = json.loads(line.replace("\n",""))
	business_index[data['business_id']] = data

print 'Processing Stopwords...'
stopfile = open(sys.argv[3])
stopwords = [line.strip() for line in stopfile]


def main():
	# ask for user input and process queries
	print 'Enter search terms:'
	line = sys.stdin.readline()
	while line:
		phrase = False
		if line[0] == "\"" and line[len(line)-2] == "\"":
			phrase = True
			line = line.replace("\"", "")
		
		regex = re.compile('[%s]' % re.escape(string.punctuation))
		oldwords = regex.sub(' ', line.strip().lower()).split()
		words = []
		ignored = 0
		for w in oldwords:
			if w in stopwords:
				if phrase: #add placeholder
					words.append("")
					ignored += 1
			else:
				stemmed = porter_stemmer.PorterStemmer().stem(w, 0,len(w)-1)
				words.append(stemmed)
		
		if phrase:
			businesses = processPhraseQuery(words, ignored)
		else:
			businesses = processQuery(words)
		# rank businesses and print results
		if len(businesses) == 0:
			print 'Sorry, no results found'
		else:
			# print businesses
			rank(businesses, words)
		print 'Enter search terms:'
		line = sys.stdin.readline()		

def processQuery(words):
	businesses_temp = {}
	businesses = []
	for w in words:
		if w in inverted_index:
			for b in inverted_index[w]:
				if b not in businesses_temp:
					businesses_temp[b] = 0
				businesses_temp[b] += 1
	
	# find the businesses whose reviews contained all the words
	for k, v in businesses_temp.iteritems():	
		if v == (len(words)):
			businesses.append(k)
	return businesses

def processPhraseQuery(words, ignored):
	businesses = []
	i = 0
	first = words[0]
	while first == "":
		i += 1
		if i == len(words):
			return []
		first = words[i]

	if first in inverted_index:
		for b in inverted_index[first]:
			for r in inverted_index[first][b]:
				for p in inverted_index[first][b][r]:
					count = 1
					position = p
					for x in range(i+1, len(words)):
						if words[x] == "":
							position += 1
						elif words[x] in inverted_index:
							if b in inverted_index[words[x]] and r in inverted_index[words[x]][b]:
								if (position + 1) in inverted_index[words[x]][b][r]:
									count += 1
									position += 1
					if count == (len(words) - ignored) and b not in businesses:
						businesses.append(b)
	return businesses


def rank(businesses, words):
	score = {x: 0 for x in businesses}
	# TODO - deal with words in stopwords
	for w in words:
		if w != "":
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
				score[b] += tf * idf
	# apply heuristic of score=tfidf*log(review_count)*stars
	for b in businesses:
		score[b] = score[b] * math.log(business_index[b]["review_count"])*business_index[b]["stars"]
	
	# sort tfidf dict by values and then figure out what we actually want to return
	sorted_businesses = sorted(score.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
	print 'Results:'

	for i,(b,score) in enumerate(sorted_businesses):
		row = str(i+1)+': '+business_index[b]['name']+'\n'
		row += '\tBusiness ID: ' + b + '\n'
		row += '\tFull Address: ' + business_index[b]['full_address'].replace('\n','\n\t\t') + '\n'
		row += '\tStars: ' + str(business_index[b]['stars']) + '\n'
		row += '\tReview Count: ' + str(business_index[b]['review_count']) + '\n'

		print row.encode('utf-8')


if __name__ == '__main__':
	main()

