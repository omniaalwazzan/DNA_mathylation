import pandas as pd 
 
csv_path = "C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/subset_beta.csv"
csv_gt = "C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/ImgID_850k_GT.csv"
df1 = pd.read_csv(csv_path, index_col=(0))
df1 = df1.T
df1 = df1.rename_axis('Sentrix.ID')


df2 = pd.read_csv(csv_gt,index_col=(0))


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

# Select cases where the counts are >= 10
filtered_result = result[result['MC 12.6'].isin(values.index[values >= 10])]
filtered_result = filtered_result.reset_index(drop=True)

filtered_result.to_csv('C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/GT_subset_beta.csv', index=False)

