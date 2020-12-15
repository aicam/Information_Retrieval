from os import listdir
from os.path import isfile, join
mypath = "sampleDoc"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def extract_dictionaries(file_names):
    files = []
    for file in file_names:
        f = open(mypath + '/' + file)
        files.append({'dicID': file, 'content': f.read().replace('\n', ' ').replace('\u200c', ' ').split(' ')})
        f.close()
    return files


files_dic = extract_dictionaries(onlyfiles)
print(files_dic[0])