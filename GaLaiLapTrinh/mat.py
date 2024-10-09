import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = 'grocery_dataset.txt'

# Đọc 5 dòng đầu tiên của file
df = pd.read_csv(path, nrows=5)

print(df)
