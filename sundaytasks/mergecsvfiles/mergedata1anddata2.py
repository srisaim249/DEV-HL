import pandas as pd

a = pd.read_csv("data1withoutduplicates.csv")
b = pd.read_csv("data2withoutduplicates.csv")
#b = b.dropna(axis=1)
merged = a.merge(b, on='id')
merged.to_csv("outputwithoutduplicates.csv", index=False)