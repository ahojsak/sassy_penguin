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
	opts = parser.parse_args()
	############################################################

	funny_threshold = 1
	
	##### BUILD TRAINING SET ###################################
	# Initialize CountVectorizer
	# You will need to implement functions in tokenizer.py
	tokenizer = Tokenizer()
	vectorizer = CountVectorizer(binary=True, lowercase=True, decode_error='replace', tokenizer=tokenizer)
	
	# process the review file
	f = open(opts.training, 'rb')
	
	text = []
	score = []
	
	line = f.readline()
	while line:
		data = json.loads(line)
		if data['votes']['funny'] >= funny_threshold:
			score.append(1)
		else:
			score.append(0)
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

	classifier = MultinomialNB(fit_prior=True)
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
			data = json.loads(line)
			
			if data['votes']['funny'] >= funny_threshold:
				score.append(1)
			else:
				score.append(0)
			
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
