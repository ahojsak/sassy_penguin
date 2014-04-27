import sys
import json

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

if __name__ == '__main__':
	main()

