import numpy as np

def search(ii, q):
    terms = q.split(' ')
    terms = [item for item in terms if item in ii.keys()]
    print(np.where(ii.keys() == 'به'))
    terms_dict = {term: [item['docID'] for item in ii[term]] for term in terms}
