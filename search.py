import numpy as np
import collections
from sklearn.metrics.pairwise import cosine_similarity

def search(ii, q):
    terms = q.split(' ')
    terms = [item for item in terms if item in ii.keys()]
    terms_dict = {term: [item['docID'] for item in ii[term]] for term in terms}
    doc_scores = {key: 0 for key in np.unique(np.hstack(list(terms_dict.values())))}
    for term in terms:
        for doc in list(set(terms_dict[term]).intersection(doc_scores.keys())):
            doc_scores[doc] += 1
    return({k: v for k, v in sorted(doc_scores.items(), key=lambda item: item[1], reverse=True)})

def search_by_tfidf(tfidf, docs, query, dicts):
    query_terms = query.split(' ')
    query_terms_unique = np.unique(query_terms)
    all_terms = list(dicts.keys())
    weights = {}
    for term in query_terms_unique:
        if (term not in all_terms):
            continue
        tf = 1 + np.log10(query_terms.count(term))
        idf = np.log10(len(docs) / len(dicts[term]))
        weights.update({term: tf*idf})
    eliminated_tfidf = tfidf[np.where(np.isin(all_terms, list(weights.keys())))]
    q = np.array(list(collections.OrderedDict(sorted(weights.items(), reverse=True)).values()))
    return_docs = []
    for i in range(len(docs)):
        d = eliminated_tfidf[:,i]
        print(d)
        # print(np.dot(q, d)/(np.linalg.norm(q)*np.linalg.norm(d)))
        return_docs.append({docs[i]: cosine_similarity(q.reshape([-1, 1]), eliminated_tfidf[:,i].reshape([-1, 1]))})
    # print(return_docs)


