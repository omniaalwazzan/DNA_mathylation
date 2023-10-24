import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import pyHSICLasso as hsic


path = "C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/Part6_850k_Betas.csv"
GT_path = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/ImgID_850k_GT.csv"

#path_4cases = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/Part6_850k_Betas_4samples.csv"
df =  pd.read_csv(path,index_col=(0))
df1 = df.T
df1 = df1.rename_axis('Sentrix.ID')

df2 = pd.read_csv(GT_path,index_col=(0))
result = pd.merge(left=df1, right=df2, left_index=True, right_on='Sentrix.ID')
values = result['MC 12.6'].value_counts()


columns_to_move = ['Sentrix.ID', 'Sample.ID']
new_positions = [0, 1]
# Create a new list of column names with the specified order
new_order = [col for col in result if col not in columns_to_move]
# Insert columns at their new positions
for col, pos in zip(columns_to_move, new_positions):
    new_order.insert(pos, col)

# Reorder the columns in the DataFrame
result = result[new_order]

filtered_result = result[result['MC 12.6'].isin(values.index[values >= 10])]
filtered_result = filtered_result.reset_index(drop=True)

df = filtered_result.drop(columns=['Sample.ID'])

df['class'], class_mapping = pd.factorize(df['MC 12.6'])
df.drop(columns=['MC 12.6'], inplace=True)
df.drop(columns=['Sentrix.ID'], inplace=True)

df.columns

last_column = df.pop(df.columns[-1])
# Insert the last column at the first position
df.insert(0, last_column.name, last_column)

new_path = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/lasso_Part6_850k_Betas.csv"
df.to_csv(new_path)
h = hsic.HSICLasso() # initate the class
h.input(new_path)
h.classification(num_feat=50, M=20, B=3)
h.dump() # this save to dataframe
