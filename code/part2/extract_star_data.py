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
	vote_counts = {'funny':{}, 'cool':{}, 'useful':{}}
	line = f.readline()
	while line:
		review = json.loads(line)
		
		stars = review['stars']
		votes = ""
		if review['votes']['funny']>0:
			votes += 'funny'
			if review['votes']['funny'] not in vote_counts['funny']:
				vote_counts['funny'][review['votes']['funny']] = 0
			vote_counts['funny'][review['votes']['funny']] += 1

		if review['votes']['cool']>0:
			votes += 'cool'
			if review['votes']['cool'] not in vote_counts['cool']:
				vote_counts['cool'][review['votes']['cool']] = 0
			vote_counts['cool'][review['votes']['cool']] += 1

		if review['votes']['useful']>0:
			votes += 'useful'
			if review['votes']['useful'] not in vote_counts['useful']:
				vote_counts['useful'][review['votes']['useful']] = 0
			vote_counts['useful'][review['votes']['useful']] += 1
	
		if votes not in data:
			data[votes] = {}
		if stars not in data[votes]:
			data[votes][stars] = 0
		
		data[votes][stars] += 1
		line = f.readline()	

	f.close()

	print 'Star counts by combination of vote types'
	for k in data:
		print k,data[k]

	print ''
	print 'Vote counts by type'
	for k in vote_counts:
		print k, vote_counts[k]

	############################################################
 		
if __name__ == '__main__':
	main()
