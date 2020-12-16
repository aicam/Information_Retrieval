from os import listdir
from os.path import isfile, join
from matchings import *
from create_inverted_index import *
from search import *
import numpy as np

mypath = "sampleDoc"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def extract_dictionaries(file_names):
    files = {}
    raw_docs = {}
    for file in file_names:
        f = open(mypath + '/' + file)


        ## First matching
        raw_data = f.read()
        raw_docs.update({file: raw_data.
                         replace('\n', '')})
        files.update({file: np.array(raw_data.
                     replace('\n', ' ').
                     replace('\u200c', ' ').
                     replace('.', '').split(' '))})
        f.close()
    return files, raw_docs


dicts, raw_docs = extract_dictionaries(onlyfiles)
dicts = matching_7(matching_6(matching_4(matching_3(matching_2(dicts)))))
dicts = {key: [v for v in val if v != ''] for key, val in dicts.items()}
inverted_index = create_inverted_index(dicts)
print('Inverted indexes are ready, enter your query')
# x = input()
result = search(inverted_index, 'پرسپولیس چند مدت')
for key, value in result.items():
    print("Document " + key + " matched:")
    print(raw_docs[key])
    print("------------------------------Document score: ", value)