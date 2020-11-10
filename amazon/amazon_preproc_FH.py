"""
This document imports the data into a pandas dataframe and goes through the following 
preprocessing steps:

-Case collapsing
-Remove punctuation
-Tokenization
-N-Grams: bigrams and trigrams
-Token, bigram and trigram frequencies
-Stemming -> check whether this makes a difference
-Lemmatization -> check whether this makes a difference
-Part-of-speech (POS) tagging
-Named entity recognition (NER)

"""

# -------------------------------------------------------------------------

## Import Data
"""
Imports data as pandas dataframe
Create list of title and genre columns from original data
Create list including all 32 genres
"""
import pandas as pd
df = pd.read_csv(r'/Users/feliciaheilgendorff/Documents/AU/NLP/NLP-Project/amazon/book32listing.csv', encoding='latin1', header=None)
df1 = df[[3,6]] # only columns with titles and genres
df1.columns = ['title', 'genre']
print(df1)

titles = df1['title'] # list of all titles
titles1 = titles.values.tolist() # change to list of strings
print(titles1)

genres = ['Arts & Photography', 'Biographies & Memoirs', 
'Business & Money', 'Calendars', 'Children''s Books', 'Comics & Graphic Novels', 
'Computers & Technology', 'Cookbooks, Food & Wine', 'Crafts, Hobbies & Home', 
'Christian Books & Bibles', 'Engineering & Transportation', 'Health, Fitness & Dieting', 
'History', 'Humor & Entertainment', 'Law', 'Literature & Fiction', 'Medical Books', 
'Mystery, Thriller & Suspense', 'Parenting & Relationships', 'Politics & Social Sciences', 
'Reference', 'Religion & Spirituality', 'Romance', 'Science & Math', 'Science Fiction & Fantasy', 
'Self-Help', 'Sports & Outdoors', 'Teen & Young Adult', 'Test Preparation', 'Travel', 
'Gay & Lesbian', 'Education & Teaching']
print(genres) # list of all possible genres

# -------------------------------------------------------------------------

## Case Collapsing
"""
Change all uppercase to lowercase letters
"""
case_collap = map(lambda x:x.lower(), titles1)
case_collap_list = list(case_collap)
print(case_collap_list)

## Remove Punctuation
"""
Remove punctuation by creating translation table
Punctuation to be removed is given in string: string.punctuation
"""
import string
trans = str.maketrans('', '', string.punctuation)
rem_punct = [s.translate(trans) for s in case_collap_list]

## Tokenization
"""
Split all titles into words
Output: list of lists of strings
"""
import nltk
from nltk.tokenize import word_tokenize
tokenized_titles = [word_tokenize(i) for i in rem_punct]
for i in tokenized_titles:
    print(i)

"""
## Filter out Stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in tokenized_titles if not w in stop_words]
print(words[:100])
"""

## N-Grams: Bigrams and Trigrams
"""
Currenlty only works with sublist (token_flat) -> not working with list of lists
Create bigrams + trigrams
"""
token_flat = [item for sublist in tokenized_titles for item in sublist]
token_bigram = [(token_flat[w], token_flat[w + 1], ) for w in range(len(token_flat) - 1)]
print(token_bigram)
token_trigram = [(token_flat[w], token_flat[w + 1], token_flat[w + 2]) for w in range(len(token_flat) - 2)]
print(token_trigram)

for t in tokenized_titles:
    token_bigram = [(t[w], t[w + 1], ) for w in range(len(t) - 1)]
    print(token_bigram)

for t in tokenized_titles:
    token_trigram = [(t[w], t[w + 1], t[w + 2]) for w in range(len(t) - 2)]
    print(token_trigram)





## Token, Bigram & Trigram Frequencies
"""
Still uses token_flat -> need to change this to list of lists
Initialize empty lists for wordcounts
Count frequencies of tokens, bigrams and trigrams
"""
from collections import Counter
unigram_count = Counter()
bigram_count = Counter()
trigram_count = Counter()

for i in token_flat:
    unigram_count[i] += 1
for i in token_bigram:
    bigram_count[i] += 1
for i in token_trigram:
    trigram_count[i] += 1

## Stemming
"""
Not working for list of lists yet
Test this out to see whether it makes a difference in final classifier
PorterStemmer (one algorithm for stemming; less aggressive than LancasterStemming)
Create empty list
Add each stemmed word to list
"""
from nltk.stem import PorterStemmer
porter = PorterStemmer()
stems = []
for word in token_flat:
    stems.append(porter.stem(word))
print(stems)

for title in tokenized_titles:
    for word in title:
        stems_title = porter.stem(word)
    stems.append(stem_title)
print(stems)

## Lemmatization
"""
Not working for list of lists yet
Same principle as with stemming
Test this out to see whether it makes a difference in final classifier
"""
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmas = []
for word in token_flat:
    lemmas.append(lemmatizer.lemmatize(word))
print(lemmas)


lemmas = []
for title in tokenized_titles:
    for word in title:
        lemmas_title = lemmatizer.lemmatize(word)
    lemmas.append(lemmas_title)
print(lemmas)



## Part-of-Speech (POS) Tagging
"""
This works for list of lists!
Create list of title lists with tokens and their corresponding part-of-speech tag
"""
nltk.download('averaged_perceptron_tagger')
from nltk.tag import pos_tag
postag = []
for title in tokenized_titles:
    postag.append(nltk.pos_tag(title))
print(postag)

## Named Entity Recognition (NER)
"""
Create list with words, correspondent POS and named entity tags
"""
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import ne_chunk
from nltk.chunk import tree2conlltags
print(tree2conlltags(ne_chunk(postag)))

ner = []
for title in titles1:
    ner.append(tree2conlltags(ne_chunk(pos_tag(word_tokenize(title)))))
print(ner)

# this works
print(tree2conlltags(ne_chunk(pos_tag(word_tokenize(titles1[157])))))

# -------------------------------------------------------------------------

## Naive Bayes classifier
"""
split into training and test data -> 80% / 20%
use n-grams ?

build vocabulary
vocabulary for each genre

for testing -> need list with just titles -> then check that against other list that includes respective genres
"""

# -------------------------------------------------------------------------

## BERT classifier

# -------------------------------------------------------------------------

## Research question: Does stemming / lemmatization improve/worsen classifier?