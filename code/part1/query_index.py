import sys
<<<<<<< HEAD
import math



def main():
	# first read in the inverted index file
	inverted_index_file = open(sys.argv[1])
	inverted_index = json.loads(inverted_index_file.readline())

	business_index = {}
	business_file = open(sys.argv[2])
	for line in business_file.readlines():
		data = json.loads(line.replace("\n",""))
		business_index[data['business_id']] = data

	for line in sys.stdin:
		# answer each query
		print line


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
	
	return scores


if __name__ == '__main__':
	f = open(review_file)
	main()

