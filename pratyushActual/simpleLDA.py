import gensim
from gensim import corpora, models
fp= open("preprocessed.txt","r")
line= fp.readline()
texts=[]
while(line):
	splitLine= list(line.split(" "))
	texts.append(splitLine)
	line=fp.readline()
fp.close()
dictionary= corpora.Dictionary(texts)
corpus= [dictionary.doc2bow(text) for text in texts]
LDAModel= gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word= dictionary, passes=30)
print(LDAModel.print_topics(num_topics=3, num_words=4))