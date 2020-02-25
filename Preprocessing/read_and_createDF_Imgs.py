import pandas as pd
import numpy as np
import os

filtered_data = pd.read_csv("../data/FILTERED_FINAL_IMBD_DATA.csv", sep=',', engine='python', header=0, index_col=0)

print(filtered_data['index'])
