# importing various modules to be used 
from sklearn import cluster
from sklearn import metrics
import sys
import string
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import collections

# Function to load Glove model to use to vectorise sentences for KMeans
def loadGloveModel(gloveFile):
	print ("Loading Glove Model")
	f = open(gloveFile, 'r')
	model = {}
	for line in f:
		splitLine = line.split()
		word = splitLine[0]
		embedding = np.array([float(val) for val in splitLine[1:]])
		model[word] = embedding
	print("Done dude.", len(model)," words loaded!")
	return model
model = loadGloveModel("glove.6B.300d.txt")

# Function to get the mean vector of a sentence 
def avg_feature_vector(sentence, num_features):
	words = sentence.split()
	feature_vec = np.zeros((num_features, ), dtype='float32')
	n_words = 0
	for word in words:
		if word in model:
			n_words = n_words + 1
			feature_vec = np.add(feature_vec, model[word])
	if (n_words>0):
		feature_vec = np.divide(feature_vec, n_words)
	return feature_vec

# Taking Data from the file
fp = open("finalDataSet_2.txt","r")

# Defining set of stop words and the lemmatizer to be used for pre-processing
sw = set(stopwords.words('english'))
lem = WordNetLemmatizer()

# List to hold the Sentences and the Vector representation respectively  of the data 
sentences = []
x = []
lines = []

# Preprocessing The data obtained
for line in fp:
	try:
		line = line.decode('utf8')
		line = line.rstrip("\n")
		if len(line) == 0:
			continue
		lines.append(line)
	except:
		continue

customStopList = ['nil']
for data in lines:
	data = data.lower()
	tokenizedWords = word_tokenize(data)
	filteredSentence = [w for w in tokenizedWords if not w in sw and not w in set(string.punctuation) and w not in customStopList]
	tagged = nltk.pos_tag(filteredSentence)
	tree = nltk.ne_chunk(tagged).leaves()
	lematizedSentence = []
	for y in tree:
		if 'NN' in y[1] or 'NP' in y[1]:
			z = lem.lemmatize(y[0])
			lematizedSentence.append(z)
		elif 'VB' in y[1]:
			z = lem.lemmatize(y[0])
			lematizedSentence.append(z)
		else:
			lematizedSentence.append(y[0])
	backToSentence = " ".join(lematizedSentence)
	sentences.append(backToSentence)

# Getting the vector representation of the data
for line in sentences:
	line = line.rstrip("\n")
	averageVector = avg_feature_vector(line, num_features=300)
	x.append(averageVector)

# Actual KMeans algorithm
x = np.asarray(x)
NUM_CLUSTERS = 8
kmeans = cluster.KMeans(n_clusters=NUM_CLUSTERS)
kmeans.fit_transform(x)
assigned_clusters = kmeans.labels_

# obtaining the list of sentences in a cluster
length = len (assigned_clusters)
resultant = []
resultant2 = []
for i in range(0, NUM_CLUSTERS):
	resultant.append([])
	resultant2.append([])
	for j in range(0, length):
		if (assigned_clusters[j] == i):
			resultant[i].append(lines[j])
			resultant2[i].append(sentences[j])

# Eliminating the unnecessary lines 
for i, lists in enumerate( resultant2 ) :
	c = collections.Counter()
	for j, sentence in enumerate ( lists ) :
		splitLine = sentence.split()
		c.update( splitLine )
	sum = 0
	for word  in c :
		sum = sum + c[word]
	threshHold = sum * 0.3
	for k, sent in enumerate (lists ):
		splitLines = sent.split()
		thrown = 0
		for word in splitLines :
			if ( c[word] > threshHold) :
				thrown = 1
		if ( thrown == 0) :
			lists.pop( k )

# obtaining the top 3 words in each cluster 
customList = ['nil', 'Nil', 'NIL', 'm', 'M', '...']
noun_tags = ['NN', 'NNS', 'NP', 'NPS']
top_words = []
for i, lists in enumerate ( resultant2 ) :
	top_words.append( [] )
	c = collections.Counter()
	for j, sentence in enumerate ( lists ):
		splitLine = sentence.split()
		c.update( splitLine )
	for word, count  in c.most_common (5):
		word = str(word)
		pos = nltk.pos_tag([word])
		if word not in customList and  pos[0][1] in noun_tags:
			top_words[i].append(word)

for i, lists in enumerate(top_words) :
	print(lists)
sys.exit()
# end of file 