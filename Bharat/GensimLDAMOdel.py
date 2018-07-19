import gensim
from gensim import corpora, models
from preprocessing import get_sentenses

processed_result = get_sentenses('finalDataSet_1.txt')
texts = []
discriptions = []

for sentense in processed_result:
	temp = sentense.split()
	texts.append(temp)
	discriptions.append(processed_result[sentense])

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
LDAModel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 8, id2word = dictionary, passes = 30)

topic_probabilities = {}
for i in range(len(corpus)):
	temp = LDAModel.get_document_topics(corpus[i], minimum_probability = 0.75)
	if len(temp) == 0:
		continue
	topic_probabilities[discriptions[i]] = temp[0][0]

cluster = []

for topic_no in range(8):
	temp = ''
	for comment in topic_probabilities:
		if topic_probabilities[comment] == topic_no:
			temp += comment + '\n\n'
	cluster.append(temp)

for i in cluster:
	print(i)

fhand = open('cluster_LDA.txt', 'w')

for i in cluster:
	fhand.write(i + '\n\n\n')
	
fhand.close()