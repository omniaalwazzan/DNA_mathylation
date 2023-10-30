import pandas as pd
import numpy as np 
import pyHSICLasso as hsic
import os



beta_850k = "/data/DERI-MMH/DNA_meth/beta-vals/Part2_850k_Betas.csv" 
#"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/subset_beta.csv"
file_name = os.path.basename(beta_850k)


df1 = pd.read_csv(beta_850k, index_col=(0))

df1= df1.T
df1 = df1.rename_axis('Sentrix.ID')

print('shape of bata values part',file_name,' is :', df1.shape)

# "/data/DERI-MMH/DNA_meth/beta-vals/ImgID_850k_GT_more10.csv"
csv_gt = "/data/DERI-MMH/DNA_meth/beta-vals/ImgID_850k_GT_more10.csv"
df2 = pd.read_csv(csv_gt,index_col=(0))


file_name1 = os.path.basename(csv_gt)
print('shape of GT df is',file_name1,' is :', df2.shape)


result = pd.merge(left=df1, right=df2, left_index=True, right_on='Sentrix.ID')
values = result['MC 12.6'].value_counts()

print('GT are:', values)

print(result.columns)
print(result.head())

result = result.drop(columns=['Sample.ID'])
result.set_index('Sentrix.ID', inplace=True)

result['class'], class_mapping = pd.factorize(result['MC 12.6'])
result.drop(columns=['MC 12.6'], inplace=True)
print(result.head(3))

last_column = result.pop(result.columns[-1])
# Insert the last column at the first position
result.insert(0, last_column.name, last_column)
print(result.head(3))

# Extract the second column to the last as NumPy array 'x'
x = result.iloc[:, 1:].values.astype(dtype=np.float16)

# Extract the first column as NumPy array 'y'
y = result.iloc[:, 0].values.astype(dtype=np.float16)

# Print the extracted arrays
print("x (columns 2 to last):\n", x.shape)
print("y (first column):\n", y.shape)

B=2
h = hsic.HSICLasso() # initate the class
h.input(x,y)

# Check if the number of rows in x is divisible by B
while x.shape[0] % B != 0:
    B += 1  # Increment B until a divisor is found

print("Optimal divisor for the number of rows in x:", B)

h.classification(num_feat=8000, M=20, B=B) #B must be an exact divisor of the number of samples(rows)
h.save_param() #Save selected features and its neighbors 
h.dump()
