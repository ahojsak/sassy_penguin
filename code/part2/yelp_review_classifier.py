from __future__ import division
import sys
import csv
import argparse
from collections import defaultdict
import Queue
import util
import json

import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import cross_validation
from sklearn.naive_bayes import MultinomialNB
from tokenizer import Tokenizer
import matplotlib.pyplot as plt

def main():
	##### DO NOT MODIFY THESE OPTIONS ##########################
	parser = argparse.ArgumentParser()
	parser.add_argument('-training', required=True, help='Path to training data')
	parser.add_argument('-test', help='Path to test data')	
	parser.add_argument('-stop', required=True, help='path to stop word file')
	opts = parser.parse_args()
	############################################################

	threshold = 1
	
	##### BUILD TRAINING SET ###################################
	# Initialize CountVectorizer
	# You will need to implement functions in tokenizer.py
	
	stopfile = open(opts.stop, 'rb')
	stopwords = [line.strip() for line in stopfile]

	tokenizer = Tokenizer(stopwords)
	vectorizer = CountVectorizer(binary=True, lowercase=True, decode_error='replace', tokenizer=tokenizer)
	
	# process the review file
	f = open(opts.training, 'rb')
	
	text = []
	score = []
	
	line = f.readline()
	while line:
		total = 0
		data = json.loads(line)
		if data['votes']['funny'] >= 1:
			total += 4
		if data['votes']['useful'] >= 1:
			total += 2
		if data['votes']['cool'] >= 1:
			total += 1
		if total in [1, 4, 5, 6]:
			total = 0
		score.append(total)

		text.append(data['text'])
		line = f.readline()
	f.close()

    # Get training features using vectorizer
	training_features = vectorizer.fit_transform(text)
	# Transform training labels to numpy array (numpy.array)
	training_labels = numpy.array(score)
	############################################################
	
	##### TRAIN THE MODEL ######################################
	# Initialize the corresponding type of the classifier and train it (using 'fit')

	classifier = MultinomialNB()
	classifier.fit(training_features, training_labels)
	print classifier.class_count_
	############################################################


	###### VALIDATE THE MODEL ##################################
	# Print training mean accuracy using 'score'
	train_accuracy = classifier.score(training_features, training_labels)
	print "The training accuracy is ", train_accuracy
	############################################################


	##### TEST THE MODEL #######################################
	if not opts.test is None:
		# Test the classifier on the given test set
		# Extract features from the test set and transform it using vectorizer
		f = open(opts.test, 'rb')
		text = []
		score = []
			
		line = f.readline()
		while line:
			total = 0
			data = json.loads(line)
			
			if data['votes']['funny'] >= 1:
				total += 4
			if data['votes']['useful'] >= 1:
				total += 2
			if data['votes']['cool'] >= 1:
				total += 1
			if total in [1, 4, 5, 6]:
				total = 0
			score.append(total)
			
			text.append(data['text'])
			line = f.readline()
		f.close()

		test_features = vectorizer.transform(text)
		test_labels = numpy.array(score)
		# Print test mean accuracy
		test_score = classifier.score(test_features, test_labels)
		print "The mean accuracy on test data is", test_score
		# Predict labels for the test set
		predicted_labels = classifier.predict(test_features)
		# Print the classification report
		print "Here is the classification report"
		print classification_report(test_labels, predicted_labels)
		# Print the confusion matrix
		print "Here is the confusion matrix"
		print confusion_matrix(test_labels, predicted_labels)
		

	############################################################
 		
if __name__ == '__main__':
	main()
