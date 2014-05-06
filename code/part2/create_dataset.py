from __future__ import division
import sys
import argparse
import random
import json

def main():
	##### DO NOT MODIFY THESE OPTIONS ##########################
	parser = argparse.ArgumentParser()
	parser.add_argument('-data', required=True, help='Path to original data')
	parser.add_argument('-training', required=True, help='Path to training data')
	parser.add_argument('-test', required=True, help='Path to test data')	
	opts = parser.parse_args()
	############################################################

	training_prob = 0.7
	test_prob = 0.3
	
	# process the orginal data file
	f = open(opts.data, 'r')
	f_train = open(opts.training, 'w')
	f_test = open(opts.test, 'w')

	line = f.readline()
	while line:
		rand = random.random()
		data = json.loads(line)
		new_data = {}
		new_data['stars'] = data['stars']
		new_data['votes'] = data['votes']
		new_data['text'] = data['text']

		if rand < training_prob:
			# Add to training set
			json.dump(new_data, f_train)
			f_train.write('\n')
		elif rand < training_prob + test_prob:
			# Add to test set
			json.dump(new_data, f_test)
			f_test.write('\n')
		line = f.readline()	

	f.close()
	f_train.close()
	f_test.close()
	############################################################
 		
if __name__ == '__main__':
	main()
