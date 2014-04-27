import sys
import json
import porter_stemmer

# Script Usage: python create_index.py <review file> <stopword file> > <output file>

def main():
	index = {}
	# Inverted Index Structure
	#	{
	#		"word": {
	#			"business_id": {
	#				"review_id": [positions]
	#			}
	#		}
	#	}
	
	review_file = sys.argv[1]
	stopword_file = sys.argv[2]
    
	stemmed_dict = {}

	# load stop word file and save
	sf = open(review_file)
	stopwords = {}
	for line in sf.readlines():
		stopwords[line.replace("\n","")] = 1
	
	# process the review file
	f = open(review_file)
	for n, line in enumerate(f.readlines()):
		data = json.loads(line.replace("\n",""))
		business = data["business_id"]
		# lower case the word and split on white space
		for i, word in enumerate(data["text"].lower().split()):
			# check to ensure word isn't a stop word
			if word not in stopwords:
				# apply porter stemming
				if word not in stemmed_dict:
					old_word = word
					word = porter_stemmer.PorterStemmer().stem(word, 0,len(word)-1)
					stemmed_dict[old_word] = word
				else:
					word = stemmed_dict[word]
				word = word.encode('utf-8')
				if word not in index:
					index[word] = {business:{n: [i]}}
				elif business not in index[word]:
					index[word][business] = {n:[i]}
				elif n not in index[word][business]:
					index[word][business][n] = [i]
				else:
					index[word][business][n].append([i])
	print json.dumps(index)

if __name__ == '__main__':
	main()
