import pandas as pd
import numpy as np

xls_path = r'C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/Copy of Illumina Array ProjectVersion - anonymised 1.xlsx'
df_large = pd.read_csv('C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/subset_beta.csv')  # Subset of beta 
csv_path = r'C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/combined_beta_labeled.csv'
csv_path_transpoesd = r'C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/T_combined_beta_labeled.csv'



xls_file = pd.ExcelFile(xls_path)
df_labels = pd.read_excel(xls_file, sheet_name='Sheet1')  # Replace 'Sheet1' with the actual sheet name


selected_rows = [0]
df_large.iloc[selected_rows, 0:3]
# Load your DataFrame containing patient IDs and labels (df_labels)

# Create a dictionary from df_labels with patient IDs as keys and labels as values
id_label_dict = dict(zip(df_labels['Sentrix.ID'], df_labels['MC 12.6']))



# Filter columns in df_large that have corresponding keys in id_label_dict
selected_columns = [col for col in df_large.columns if col in id_label_dict]



# Create a new DataFrame with labels as a row
labels_df = pd.DataFrame([df_large[selected_columns].columns.map(id_label_dict)], columns=selected_columns)

# Concatenate the labels DataFrame with df_large
df_large_labeled = pd.concat([df_large, labels_df], axis=0)

df_large_labeled.to_csv(csv_path)

df_large_labeled_reset = df_large_labeled.reset_index(drop=True)

# Transpose the DataFrame
df_transposed = df_large_labeled_reset.transpose()

# Set the first row as the index
df_transposed.columns = df_transposed.iloc[0]
df_transposed = df_transposed.reindex(df_transposed.index.drop(df_transposed.index[0]))


# rename the last col from nan to GT

# Assuming df is your DataFrame
# Check if the last column name is 'nan'
if np.isnan(df_transposed.columns[-1]):
    # Get the current column names
    columns = df_transposed.columns.tolist()
    
    # Rename the last column to 'new_column_name'
    new_column_name = 'GT'
    columns[-1] = new_column_name
    
    # Update the DataFrame with the new column names
    df_transposed.columns = columns


df_transposed.to_csv(csv_path_transpoesd)
