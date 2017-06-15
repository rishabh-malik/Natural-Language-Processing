#Named Entity Recognition- The idea is to have the machine immediately be able to pull out "entities" like people, places, things, locations, monetary figures, and more.

#NE Type and Examples
#ORGANIZATION - Georgia-Pacific Corp., WHO
#PERSON - Eddy Bonte, President Obama
#LOCATION - Murray River, Mount Everest
#DATE - June, 2008-06-29
#TIME - two fifty a m, 1:30 p.m.
#MONEY - 175 million Canadian Dollars, GBP 10.40
#PERCENT - twenty pct, 18.75 %
#FACILITY - Washington Monument, Stonehenge
#GPE - South East Asia, Midlothian

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)






