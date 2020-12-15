from os import listdir
from os.path import isfile, join
from matchings import *
import numpy as np

mypath = "sampleDoc"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def extract_dictionaries(file_names):
    files = {}
    for file in file_names:
        f = open(mypath + '/' + file)



        files.update({file: np.array(f.read().
                     replace('\n', ' ').
                     replace('\u200c', ' ').
                     replace('.', '').split(' '))})
        f.close()
    return files


files_dic = extract_dictionaries(onlyfiles)




matching_3(files_dic)
