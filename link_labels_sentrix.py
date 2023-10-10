import pandas as pd

xls_path = r'C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/Copy of Illumina Array ProjectVersion - anonymised 1.xlsx'
df_large = pd.read_csv('C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/subset_beta.csv')  # Subset of beta 
csv_path = r'C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/combined_beta_labeled.csv'

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


