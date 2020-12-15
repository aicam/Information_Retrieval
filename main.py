from os import listdir
from os.path import isfile, join
import numpy as np

mypath = "sampleDoc"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def extract_dictionaries(file_names):
    files = {}
    for file in file_names:
        f = open(mypath + '/' + file)



        files.update({file: f.read().
                     replace('\n', ' ').
                     replace('\u200c', ' ').
                     replace('.', '').split(' ')})
        f.close()
    return files



## Remove 3 most frequent term
def matching_1(dics):
    words = np.concatenate(list(dics.values()))
    for i in range(3):
        unique, pos = np.unique(words, return_inverse=True)
        counts = np.bincount(pos)
        maxpos = counts.argmax()
        words = np.delete(words, np.argwhere(words == unique[maxpos]))
        print(unique[maxpos])

files_dic = extract_dictionaries(onlyfiles)
matching_1(files_dic)
