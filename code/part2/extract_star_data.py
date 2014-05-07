from __future__ import division
import sys
import argparse
import random
import json

def main():
	##### DO NOT MODIFY THESE OPTIONS ##########################
	parser = argparse.ArgumentParser()
	parser.add_argument('-data', required=True, help='Path to original data')	
	opts = parser.parse_args()
	############################################################
	
	# process the orginal data file
	f = open(opts.data, 'r')

	data = {}

	line = f.readline()
	while line:
		review = json.loads(line)
		
		stars = review['stars']
		votes = ""
		if review['votes']['funny']>0:
			votes += 'funny'
		if review['votes']['cool']>0:
			votes += 'cool'
		if review['votes']['useful']>0:
			votes += 'useful'
		
		if votes not in data:
			data[votes] = {}
		if stars not in data[votes]:
			data[votes][stars] = 0
		
		data[votes][stars] += 1
		line = f.readline()	

	f.close()

	for k in data:
		print k,data[k]

	############################################################
 		
if __name__ == '__main__':
	main()
