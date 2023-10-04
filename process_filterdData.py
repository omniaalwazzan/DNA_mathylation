import pandas as pd 
import numpy as np 

beta_df = pd.read_csv(r"D:\Slivia's project\betaValues\Part1_450k_Betas.csv")

beta_df.set_index(beta_df.columns[0], inplace=True)

beta_df.head()

features = beta_df.iloc[0:, 0:1].values

df = pd.read_csv(r"D:\Slivia's project\mythalExp\filterd_data.csv")
unique_rows_count = df['MC 12.6'].nunique()

print("Number of unique rows in the column:", unique_rows_count)

print("Unique rows in the column:")
print(df['MC 12.6'].unique())


value_counts = df['MC 12.6'].value_counts()

print("Counts of samples in each unique row:")
print(value_counts)
