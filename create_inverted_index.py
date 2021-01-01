import numpy as np
import collections

def create_inverted_index(dics):
    words =  {word: [] for word in np.unique(np.concatenate(list(dics.values())))}
    dicts_keys = dics.keys()
    for key in dicts_keys:
        u_vocab, counts = np.unique(dics[key], return_counts = True)
        for i in range(len(u_vocab)):
            words[u_vocab[i]].append({'docID': key, 'frequency': counts[i]})
    od = collections.OrderedDict(sorted(words.items(), reverse=True))
    return od

def create_tfidf(dicts, docs):
    N = len(docs)
    tfidf = np.zeros([len(dicts.keys()), N])
    terms = list(dicts.keys())
    for i in range(tfidf.shape[0]):
        term = terms[i]
        f_t = dicts[term]
        idf = np.log10(N / len(f_t))
        for doc in f_t:
            docID = docs.index(doc['docID'])
            tf = 1 + np.log10(doc['frequency'])
            tfidf[i][docID] = tf * idf
    return tfidf

