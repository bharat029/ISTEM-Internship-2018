import nltk
from string import punctuation
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
custom_stop_words = ['nil', 'system', 'someone', 'build', 'engineering', 'need', 'user', 'area', 'study', 'passionate', 'medium', 'time', 'computer', 'field', 'interest', 'company', 'thing', 'learn', 'experience','help', 'love', 'skill', 'want', 'bring', 'tech', 'technology', 'people', 'person', 'life', 'family', 'use', 'would', 'work', 'matter', 'idea', 'way', 'skill', 'program', 'project']
#custom_stop_words = ['nil']
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

def processComment(comment):
    try:
        tokens = nltk.tokenize.word_tokenize(comment)
        filtered_tokens = []
        # Remove punctuation and stopwords
        for token in tokens:
            token = token.lower()
            if token in stop_words or token in punctuation or len(list(set(token).intersection(punctuation))) > 0:
                pass
            elif token in custom_stop_words:
                pass
            else:
                filtered_tokens.append(token)

        sentence = ' '.join(filtered_tokens)
        
        # Get POS tagging for the sentence and lemmatize nouns and verbs, other POS are added without any processing
        pos_tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))).leaves()
        sentence_words = []
        for leaf in pos_tree:
            if 'NN' in leaf[1] or 'NP' in leaf[1]:
                lemma = lemmatizer.lemmatize(leaf[0])
                if lemma not in custom_stop_words:
                    sentence_words.append(lemma)
            elif 'VB' in leaf[1]:
                lemma = lemmatizer.lemmatize(leaf[0], 'v')
                if lemma not in custom_stop_words:
                    sentence_words.append(lemma)
            else:
                sentence_words.append(leaf[0])

        return ' '.join(sentence_words)
    except Exception as e:
        return ""

def get_sentenses(fname):
    fhand = open(fname, errors = 'ignore')
     
    preprocessing_result = {}
    data = fhand.read()
    
    actual_sentenses = data.split('\n\n')
    preprocessed_sentenses = []
              
    for i in actual_sentenses:
        preprocessed_sentenses.append(processComment(i))
    
    for i in range(len(actual_sentenses)):
        preprocessing_result[preprocessed_sentenses[i]] = actual_sentenses[i]
    
    fhand.close()
    fhand = open('preprocessed.txt', 'w')
    
    for i in preprocessed_sentenses:
        fhand.write(i + '\n')
    fhand.close()

    return preprocessing_result

if __name__ == '__main__':
    get_sentenses('finalDataSet.txt')
    print('Done')