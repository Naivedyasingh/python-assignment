# 11.you are building a program to process a large corpus of text data. write a python function to find all unique n-gram in given text string.

def find_unique_ngram(text,n):
    words=text.lower().split()
    ngrams=set()
    for itr in range(len(words)-n+1):
        ngram=tuple(words[itr:itr+n])
        ngrams.add(ngram)
    return ngrams    

text="The quick brown fox jump over the lazy dog"
n=2
unique_ngram=find_unique_ngram(text,2)
print(unique_ngram)