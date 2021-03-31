# Information_Retrieval

A simple university project search tool for persian documents (txt).
# Methods
The documents will be tokenized and stemmed with other cleaning operations (available at matchings.py). Next, the inverted index of all words will be generated and used 
to create tf-idf and champions list matrices.
The final search is based on either inverted index or tfidf.
There is another script named clustering which search based on the clusters centers.
# How to run

Put all documents in a directory and put the name instead of sampleDoc:
```
mypath = "sampleDoc"
```

Based on your preference you can use search methods in search.py:

```
search_by_tfidf(tfidf, onlyfiles, x, inverted_index)
or
search(inverted_index, x)
```

For clustering, put your documents in separate directories:
```
root/Dataset/label1
.
.
.
```
Add your labels in the category array:
```
categories = ['Health', 'History', 'Mathematics', 'Physics', 'Technology']
```

