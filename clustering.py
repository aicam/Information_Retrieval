import datetime
from os import listdir
from os.path import isfile, join
from matchings import *
from create_inverted_index import *
from search import *
import numpy as np
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
categories = ['Health', 'History', 'Mathematics', 'Physics', 'Technology']
c_data = {key: {} for key in categories}
c_documents =  {key: [] for key in categories}
c_centers = {key: [] for key in categories}
for category in categories:
    mypath = "Dataset" + '/' + category
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    c_documents[category] = onlyfiles
    dicts, raw_docs = extract_dictionaries(onlyfiles)
    dicts = matching_7(matching_6(matching_4(matching_3(matching_2(dicts)))))
    dicts = {key: [v for v in val if v != ''] for key, val in dicts.items()}
    inverted_index = create_inverted_index(dicts)
    tfidf, champions_list = create_tfidf_championsList(inverted_index, onlyfiles)
    c_data[category].update({'tfidf': tfidf, 'ii': inverted_index})
    c_centers[category] = np.mean(tfidf, axis=1)
b = datetime.datetime.now()
print('Clusters got ready in ', (b - a).seconds, " seconds and ", (b - a).microseconds, " microseconds")
x = input("Input query:")
#'بردار مکان  یا موقعیت یا بردار شعاعی'
category_scores = []
for category in categories:
    category_scores.append(search_for_category(c_centers[category], c_documents[category], x, c_data[category]['ii']))
best_category = categories[np.argmax(category_scores)]
print(best_category)
search_by_tfidf(c_data[best_category]['tfidf'], c_documents[best_category], x, c_data[best_category]['ii'])