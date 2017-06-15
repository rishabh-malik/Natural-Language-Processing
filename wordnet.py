#WordNet is a lexical database for the English language
from nltk.corpus import wordnet
#Synsets having same meaning
syns = wordnet.synsets("program")
#example of synset
print(syns[0].name())
#just the word
print(syns[0].lemmas()[0].name())
#Definition of that first synset:
print(syns[0].definition())
#Examples of the word in use:
print(syns[0].examples())

#synonyms and antonyms to a word
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    # lemmas will be synonyms
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))



