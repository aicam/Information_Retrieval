from os import listdir
from os.path import isfile, join
from matchings import *
from create_inverted_index import *
import numpy as np

mypath = "sampleDoc"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def extract_dictionaries(file_names):
    files = {}
    for file in file_names:
        f = open(mypath + '/' + file)


        ## First matching
        files.update({file: np.array(f.read().
                     replace('\n', ' ').
                     replace('\u200c', ' ').
                     replace('.', '').split(' '))})
        f.close()
    return files


dicts = extract_dictionaries(onlyfiles)
dicts = matching_4(matching_3(matching_2(dicts)))
dicts = {key: [v for v in val if v != ''] for key, val in dicts.items()}
create_inverted_index(dicts)
