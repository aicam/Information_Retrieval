import numpy as np

a = np.array(['سلام', 'بهترین'])
print(np.char.replace(a, ['ام','ترین'], ''))