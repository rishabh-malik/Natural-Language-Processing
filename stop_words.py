#sttop words are the words which are not needed by us for analysis
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

#all the stop words
stop_words = set(stopwords.words('english'))

#tokenizing by words
word_tokens = word_tokenize(example_sent)

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
    
print(word_tokens)
print(filtered_sentence)    