Final Project
=============
agale & ahojsak

Part 1:
-------------
The code for the first part of the project is in the code/part1 directory. 
We also have a copy of the large inverted index file in the course temp
directory: /course/cs1951a/pub/final/temp/agale\_inverted\_index.json.
To create the index, run "python create\_index.py <business review file> 
<stopword file> > outfile" and to run the search engine, run 
"python query\_index.py <inverted index file> <business data file> 
<stopword file>". 

The script will let you know when it is processing each of the files and 
when you may enter a search command. With the large index, it takes a 
while to build the dataset, but with a smaller dataset it runs quickly. 
And once it finishes reading in the data, the searches are very fast.

We support all three types of searches: one word queries, free text queries,
and phrase queries. The heuristic is described in the writeup. 

Part 2:
-------------
For part 2 of the project, we ended up using the Yelp dataset to predict
the funny, cool, and useful ratings for reviews based on the text of the
review.

The first script we wrote can be run "python extract\_star\_data.py
-data <review data file>". It prints out two csv datasets to the console
with consolidated information about the frequencies of vote counts and
the frequency of review stars given the combination of vote types. 

To get data for the next script, we wrote the script "create\_dataset.py"
which takes in the yelp review data and the name of the output training 
and test files. It randomly breaks the review into the training and 
test set based on a ratio constant provided in the file.

The next script we wrote can be run "python yelp\_review\_classifier.py
-training <training data set> -test <test data set>". Additionally, you
can include "-top n" to have it print out the n top features for the
classifier. This script prints out the test and training accuracy as
well as some relevant information. 

The data was then consolidated and used to make d3 visualizations that
can be seen in the part2.html file. Due to a bug in Firefox, the
visualizations are best viewed in Google Chrome. We have also provided
screenshots that we linked to below each visualization.
