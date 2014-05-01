import sys
import json
import porter_stemmer
import re,string

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
	sf = open(stopword_file)
	stopwords = {}
	for line in sf.readlines():
		stopwords[line.replace("\n","")] = 1
	sf.close()

	regex = re.compile('[%s]' % re.escape(string.punctuation))

	# process the review file
	f = open(review_file)
	n=0
	line = f.readline()
	while line:
			
		data = json.loads(line)
		business = data['business_id']
	
		# lower case the word and split on white space
		i=0
		for word in regex.sub(' ', data["text"].lower()).split():	
			# check to ensure word isn't a stop word
			if word not in stopwords:
				# apply porter stemming
				if word not in stemmed_dict:
					old_word = word
					word = porter_stemmer.PorterStemmer().stem(word, 0,len(word)-1)
					stemmed_dict[old_word] = word
				else:
					word = stemmed_dict[word]	
				if word not in index:
					index[word] = {business:{int(n): [i]}}
				elif business not in index[word]:
					index[word][business] = {int(n):[i]}
				elif n not in index[word][business]:
					index[word][business][int(n)] = [i]
				else:
					index[word][business][(n)].append(i)
			
			i+=1
		n+=1
		line = f.readline()
	f.close()
	for key in index:
		print json.dumps({key:index[key]}, separators=(',',':'))
	#print json.dumps(index, separators=(',',':'))

if __name__ == '__main__':
	main()
