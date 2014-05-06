from __future__ import division
import sys
import csv
import argparse
from collections import defaultdict
import Queue
import util

import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import cross_validation
from sklearn.naive_bayes import BernoulliNB
from tokenizer import Tokenizer
import matplotlib.pyplot as plt

def main():
	##### DO NOT MODIFY THESE OPTIONS ##########################
	parser = argparse.ArgumentParser()
	parser.add_argument('-training', required=True, help='Path to training data')
	parser.add_argument('-test', help='Path to test data')	
	opts = parser.parse_args()
	############################################################

	##### BUILD TRAINING SET ###################################
	# Initialize CountVectorizer
	# You will need to implement functions in tokenizer.py
	tokenizer = Tokenizer()
	vectorizer = CountVectorizer(binary=True, lowercase=True, decode_error='replace', tokenizer=tokenizer)
	
	# process the review file
	f = open(opts.training, 'rb')
	
	tweets = []
	sent = []
	
	line = f.readline()
	while line:
		data = json.loads(line)
		sent.append(data['votes']['funny'])
		tweets.append(data['text']
		line = f.readline()
	f.close()

    # Get training features using vectorizer
	training_features = vectorizer.fit_transform(tweets)
	# Transform training labels to numpy array (numpy.array)
	training_labels = numpy.array(sent)
	############################################################
	
	##### TRAIN THE MODEL ######################################
	# Initialize the corresponding type of the classifier and train it (using 'fit')

	classifier = BernoulliNB(binarize=None, alpha=0.75)
	classifier.fit(training_features, training_labels)
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
		tweets = []
		sent = []
		
			
		line = f.readline()
		while line:
			data = json.loads(line)
			sent.append(data['votes']['funny'])
			tweets.append(data['text']
			line = f.readline()
		f.close()

		test_features = vectorizer.transform(tweets)
		test_labels = numpy.array(sent)
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
		
		# Use predict_proba
		test_predicted_proba = classifier.predict_proba(test_features)

		# Plot ROC curve
		util.plot_roc_curve(test_labels, test_predicted_proba)
	
	############################################################
 		
if __name__ == '__main__':
	main()
