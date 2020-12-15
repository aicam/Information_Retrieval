import numpy as np

def create_inverted_index(dics):
    words =  {word: [] for word in np.unique(np.concatenate(list(dics.values())))}
    dicts_keys = dics.keys()
    for key in dicts_keys:
        u_vocab, counts = np.unique(dics[key], return_counts = True)
        for i in range(len(u_vocab)):
            words[u_vocab[i]].append({'dictID': key, 'frequency': counts[i]})
    print(words)
    return words
