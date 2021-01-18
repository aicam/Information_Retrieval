import numpy as np
import collections

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
    all_terms = np.array(list(dicts.keys()))
    weights = {}
    for term in query_terms_unique:
        if (term not in all_terms):
            continue
        tf = 1 + np.log10(query_terms.count(term))
        idf = np.log10(len(docs) / len(dicts[term]))
        weights.update({term: tf*idf})
    q = np.array(list(collections.OrderedDict(sorted(weights.items())).values()))
    weight_terms = np.array(list(collections.OrderedDict(sorted(weights.items())).keys()))
    eliminated_indices = []
    for i in range(len(weight_terms)):
        eliminated_indices.append(np.where(all_terms == weight_terms[i])[0][0])
    eliminated_tfidf = tfidf[eliminated_indices]#np.where(np.isin(all_terms, sorted(list(weights.keys()), reverse=True)))]
    return_docs = []
    norm_q = np.linalg.norm(q)
    for i in range(len(docs)):
        d = eliminated_tfidf[:,i]
        if not np.any(d):
            continue
        return_docs.append({docs[i]: np.dot(q, d)/(norm_q*np.linalg.norm(d))})
    print(sorted(return_docs, key=lambda x: list(x.values())[0], reverse=True))


def search_for_category(tfidf_center, docs, query, dicts):
    query_terms = query.split(' ')
    query_terms_unique = np.unique(query_terms)
    all_terms = np.array(list(dicts.keys()))
    weights = {}
    for term in query_terms_unique:
        if (term not in all_terms):
            continue
        tf = 1 + np.log10(query_terms.count(term))
        idf = np.log10(len(docs) / len(dicts[term]))
        weights.update({term: tf * idf})
    q = np.array(list(collections.OrderedDict(sorted(weights.items())).values()))
    weight_terms = np.array(list(collections.OrderedDict(sorted(weights.items())).keys()))
    shared_indices = []
    for i in range(len(weight_terms)):
        shared_indices.append(np.where(all_terms == weight_terms[i])[0][0])
    d = tfidf_center[shared_indices]
    return np.dot(q, d)/(np.linalg.norm(q)*np.linalg.norm(d)) * len(shared_indices)