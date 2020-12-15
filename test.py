import numpy as np
import pandas as pd

df = pd.read_csv('persian_dict.csv')


unique, counts = np.unique(np.array(['سل', 'الو', 'چک', 'سل']), return_counts=True)
print(counts, " ", unique)