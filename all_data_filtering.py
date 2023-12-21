

import pandas as pd 

HE_folderName = r'C:\Users\omnia\OneDrive - University of Jeddah\PhD progress\DNA_methyalation\HE_folderNames.csv'

df = pd.read_csv(HE_folderName)
#%%
uni_cases = df['Folder'].nunique() # Patient ID
uni_cases_1 = df['ID'].nunique() # Patient ID

print('Number of Folders in HE: ',uni_cases)
print('Number of unique Cases HE: ',uni_cases_1)
#%%
column_to_extract = df[['Folder','ID']].copy()
unique_ids_HE_df = column_to_extract.drop_duplicates()

#%%
file_path = r'C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/Copy of IlluminaArray_Tom.xlsx'

# Read the Excel file
df_xlsx = pd.read_excel(file_path)
classes_num = df_xlsx['MC 12.6'].value_counts()

#%%
# Merge XLS with HE folder 
merged_1 = pd.merge(unique_ids_HE_df, df_xlsx,left_on='ID',right_on='Sample.ID',how='inner')

#%%
SentrixId_beta_path = r'C:\Users\omnia\OneDrive - University of Jeddah\PhD progress\DNA_methyalation\SentrixID_of_mVal.csv'
sentrix_df = pd.read_csv(SentrixId_beta_path)
#%
merged= pd.merge(merged_1, sentrix_df, left_on='Sentrix.ID',right_on='Sentrix.ID',how='inner')


#%%
# Replace Labels 

merged['MC 12.6'] = merged['MC 12.6'].replace({'ganglioglioma':'LGG1'
                                               ,'dysembryoplastic neuroepithelial tumour':'LGG1'
                                               ,'rosette-forming glioneuronal tumour':'LGG1'
                                               , 'papillary glioneuronal tumour':'LGG1'
                                               ,'supratentorial pilocytic astrocytoma':'LGG2'
                                               ,'supratentorial midline pilocytic astrocytoma': 'LGG2'})



#%%
uni_cases_mer = merged['Folder'].nunique() # Patient ID
uni_cases_mer_1= merged['ID'].nunique() # Patient ID
classes = merged['MC 12.6'].nunique()
print('Number of Folders: ',uni_cases_mer)
print('Number of unique Cases: ',uni_cases_mer_1)
print('Number of unique Classes: ',classes)
classes_num = merged['MC 12.6'].value_counts()

#%%
# Group by 'MC 12.6' and 'ID' to count occurrences
grouped = merged.groupby(['MC 12.6', 'ID']).size().reset_index(name='count')

# Count the number of cases for each 'MC 12.6'
cases_per_gt = grouped.groupby('MC 12.6')['ID'].nunique()

# Filter IDs that have more than 10 cases in each 'MC 12.6'
filtered_ids_GT_10 = cases_per_gt[cases_per_gt > 10].index.tolist()

# Filter the original DataFrame based on filtered_ids_GT_10
filtered_df_10 = merged[merged['MC 12.6'].isin(filtered_ids_GT_10)]

# Count unique IDs after filtering
uni_cases_fil = filtered_df_10['ID'].nunique()  # Count unique IDs
print("Unique IDs with more than 10 cases in each 'MC 12.6':")
print(filtered_ids_GT_10)
print("Number of unique IDs after filtering:", uni_cases_fil)
classes_counts = filtered_df_10['MC 12.6'].value_counts()
print("Number of cases in each ground truth:\n", classes_counts)


#%%
uni_cases_mer = filtered_df_10['Folder'].nunique() # Patient ID
uni_cases_mer_1= filtered_df_10['Sentrix.ID'].nunique() # Patient ID
classes = filtered_df_10['MC 12.6'].nunique()
print('Number of Folders: ',uni_cases_mer)
print('Number of unique Cases: ',uni_cases_mer_1)
print('Number of unique Classes: ',classes)
classes_num = filtered_df_10['MC 12.6'].value_counts()
#%%
# Here I merged the Tom xls file with image folder names, then retrieved merged df I merged it with setnrix id extracted from IDAT csv file betahg38
filtered_df_10.to_csv(r'C:\Users\omnia\OneDrive - University of Jeddah\PhD progress\DNA_methyalation\Last filtring with betaMvalues and imgID\all_data_MvalSentrix_20GT.csv',index=False)

#%%
# Now we need to merg the filterd cases with the orignial XLSX df to have other important cols like sentrix and CPN
merged_2 = pd.merge(filtered_ids_df, df_xlsx,left_on='ID',right_on='Sample.ID',how='inner')
