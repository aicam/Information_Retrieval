import datetime
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

a = datetime.datetime.now()
dicts, raw_docs = extract_dictionaries(onlyfiles)
dicts = matching_7(matching_6(matching_4(matching_3(matching_2(dicts)))))
dicts = {key: [v for v in val if v != ''] for key, val in dicts.items()}
inverted_index = create_inverted_index(dicts)
tfidf = create_tfidf(inverted_index, onlyfiles)
b = datetime.datetime.now()
print('Inverted indexes are ready, enter your query in ', (b - a).seconds, " seconds and ", (b - a).microseconds, " microseconds")
# x = input("Enter query: ")
c = datetime.datetime.now()
search_by_tfidf(tfidf, onlyfiles, "فوتبال وجود یشسیشسیشسیشسی", inverted_index)
d = datetime.datetime.now()
print((d - c).seconds)
print((d - c).microseconds)
