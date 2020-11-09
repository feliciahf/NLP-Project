"""
This document imports the data into a pandas dataframe and goes through the following 
preprocessing steps:

-Case collapsing
-Take out punctuation
-Tokenization
-n-grams
-Token frequencies
-Lemmatization -> check whether this makes a difference
-Part-of-speech (POS) tagging
-Named entity recognition (NER)

"""

import pandas as pd
#os.getcwd()
#os.chdir('./amazon')
df = pd.read_csv(r'/Users/feliciaheilgendorff/Documents/AU/NLP/NLP-Project/amazon/book32listing.csv', encoding='latin1', header=None)
df1 = df[[3,6]]
df1.columns = ['title', 'genre']
print(df1)

titles = df1['title'] # list of all titles
titles1 = titles.values.tolist()
print(titles1)

# list of all possible genres
genres = ['Arts & Photography', 'Biographies & Memoirs', 
'Business & Money', 'Calendars', 'Children''s Books', 'Comics & Graphic Novels', 
'Computers & Technology', 'Cookbooks, Food & Wine', 'Crafts, Hobbies & Home', 
'Christian Books & Bibles', 'Engineering & Transportation', 'Health, Fitness & Dieting', 
'History', 'Humor & Entertainment', 'Law', 'Literature & Fiction', 'Medical Books', 
'Mystery, Thriller & Suspense', 'Parenting & Relationships', 'Politics & Social Sciences', 
'Reference', 'Religion & Spirituality', 'Romance', 'Science & Math', 'Science Fiction & Fantasy', 
'Self-Help', 'Sports & Outdoors', 'Teen & Young Adult', 'Test Preparation', 'Travel', 
'Gay & Lesbian', 'Education & Teaching']
print(genres)

## (do titles include series titles/numbers/volumes? -> otherwise we should exclude those)

## case collapsing
case_collap = map(lambda x:x.lower(), titles1)
case_collap_list = list(case_collap)
print(case_collap_list)

## take out punctuation
rem_punct = case_collap_list.translate(None, string.punctuation)

import string
rem_punct = map(lambda x:x.punctuation(), case_collap_list)
rem_punct_list = list(rem_punct)
print(rem_punct_list)

import re
s = case_collap_list
s = re.sub(r'[^\w\s]','',s)

dataframe['column_name']=dataframe['column_name'].apply(str)

## tokenization: tokenize each title into separate words
"""
This doesn't work right now! 
All words in all titles are split up by each character
"""
def tokenize(sentences):
    """
    titles (list): Titles which you want to be tokenized

    Example:
    >>> title = ["NLP is very cool"]
    >>> tokenize(title)
    [["NLP", "is", "very", "cool"], ["It", "is", "also", "useful"]]
    """
    ## importing re:
    import re

    ## unlist (fixing issues):
    titles_flat = [word for w in titles for word in w]

    ## Split these: (keep words like J. D. Gould together)?
    ## More work required here..?
    output = [re.split("\W", b) for b in titles_flat]

    ## This
    return output


# testing:
titles_tok = tokenize(titles)
print(titles_tok)

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

for testing -> need list with just titles -> then check that against other list that includes respective genres
"""


## BERT classifier

## Research question: Does lemmatization improve/worsen classifier?

## Random research question: Does "girl" in title + published post-2010 predict Thriller genre?