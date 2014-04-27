import sys
import math




def main():
	# first read in the inverted index file


	for line in sys.stdin:
		# answer each query
		print line


def rank(businesses, words):
	tfidf = {x: 0 for x in businesses}
	for w in words:
		for b in businesses:
			reviews = index[w][b]
			tf = 0
			#find correct entry in business dataset
			for n, line in enumerate(f.readlines()):
				data = json.loads(line.replace("\n",""))
				if data["business_id"] == b:
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

