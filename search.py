import numpy as np

def search(ii, q):
    terms = q.split(' ')
    terms = [item for item in terms if item in ii.keys()]

    terms_dict = {term: [item['docID'] for item in ii[term]] for term in terms}
    doc_scores = {key: 0 for key in np.unique(np.hstack(list(terms_dict.values())))}
    for term in terms:
        for doc in list(set(terms_dict[term]).intersection(doc_scores.keys())):
            doc_scores[doc] += 1
    print(doc_scores)
