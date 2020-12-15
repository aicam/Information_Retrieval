import numpy as np
import string


## Remove 3 most frequent term
def matching_1(dics):
    words = np.concatenate(list(dics.values()))
    for i in range(3):
        unique, pos = np.unique(words, return_inverse=True)
        counts = np.bincount(pos)
        maxpos = counts.argmax()
        words = np.delete(words, np.argwhere(words == unique[maxpos]))
        dics = {key: np.delete(val, np.argwhere(np.array(val) == unique[maxpos])) for key, val in dics.items()}
    return dics


## Remove punctuation
def matching_2(dics):
    exclude = set(string.punctuation)
    dics = {key: [''.join(ch for ch in s if ch not in exclude) for s in val] for key, val in dics.items()}
    return dics


## Remove ها and تر and ترین
def matching_3(dics):
    special_chars = np.array(['ترین', 'تر', 'ها'])
    dics = {key: np.char.replace(val, special_chars, '') for key, val in dics.items()}
    return dics
