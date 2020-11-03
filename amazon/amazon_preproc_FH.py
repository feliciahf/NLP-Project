"""
This document imports the data into a pandas dataframe and goes through the following 
preprocessing steps:

-Sentence segmentation
-Tokenization
-n-grams
-Token frequencies
-Lemmatization
-Part-of-speech (POS) tagging
-Named entity recognition (NER)

"""

import pandas as pd
#os.chdir('./amazon')
df = pd.read_csv(r'/Users/feliciaheilgendorff/Documents/AU/NLP/NLP-Project/amazon/book32listing.csv', encoding='latin1', header=None)
print(df)

titles = df[3] # list of all titles
genres = df[6] # list of all genres (appear multiple times)

books = list(zip(titles, genres))
# this gives a list with 2 columns: titles, genres

# list of all possible genres
genre_list = ['Arts & Photography', 'Biographies & Memoirs', 
'Business & Money', 'Calendars', 'Children''s Books', 'Comics & Graphic Novels', 
'Computers & Technology', 'Cookbooks, Food & Wine', 'Crafts, Hobbies & Home', 
'Christian Books & Bibles', 'Engineering & Transportation', 'Health, Fitness & Dieting', 
'History', 'Humor & Entertainment', 'Law', 'Literature & Fiction', 'Medical Books', 
'Mystery, Thriller & Suspense', 'Parenting & Relationships', 'Politics & Social Sciences', 
'Reference', 'Religion & Spirituality', 'Romance', 'Science & Math', 'Science Fiction & Fantasy', 
'Self-Help', 'Sports & Outdoors', 'Teen & Young Adult', 'Test Preparation', 'Travel', 
'Gay & Lesbian', 'Education & Teaching']

## do titles include series titles/numbers/volumes? -> otherwise we should exclude those

## tokenization: tokenize each title into separate words

## n-grams: bigrams, trigrams

## token frequencies: list of frequencies of each word (in each title?)

## lemmatization: strip words to their roots (should we do this?)

## part-of-speech tagging: types of words

## named entity recognition




## Naive Bayes classifier
"""
split into training and test data -> 80% / 20%
use n-grams ?

build vocabulary
vocabulary for each genre
"""