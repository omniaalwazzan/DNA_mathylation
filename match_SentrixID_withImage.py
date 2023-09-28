

import os
import pandas as pd

root_directory  = r'E:\Methylation_data_all_tumours_May23\Part_1_001_050'
# Initialize empty lists to store extracted data
folder_names = []
folder_paths = []


extracted_names = []
file_paths = []

# Recursively traverse the directory structure
for root, dirs, files in os.walk(root_directory):
    for file in files:
        # Check if the file name matches the desired pattern
        if file.endswith('_Grn.idat'):
            # Extract the part of the file name we want
            extracted_name = file.split('_Grn.idat')[0]

            # Build the full path to the file
            full_path = os.path.join(root, file)

            # Append the extracted data to the lists
            extracted_names.append(extracted_name)
            file_paths.append(full_path)

# Create a DataFrame from the extracted data
data = {'ExtractedName': extracted_names, 'FilePath': file_paths}
df = pd.DataFrame(data)

# Read the filterd data
filtered_data = pd.read_csv(r"E:/2ndYear/Slivia's project/mythalExp/filterd_data.csv")  

# Filter out cases that are above or equal a confedience score= 0.75 
filtered_data = filtered_data[filtered_data['MC 12.6 Score '] >=  0.55]

# Merg the two dataframes only if the extractedname column matches the Sentric.ID column, then drop duplicate columns
merged_data = pd.merge(df, filtered_data, left_on='ExtractedName', right_on='Sentrix.ID', how='inner')
merged_data = merged_data.drop_duplicates(subset='ExtractedName')


# To process the IDat files according the batch folder, I need to sort out the data 
merged_data = merged_data.sort_values(by='Batch number ', ascending=True)
merged_data.to_csv(r"E:\2ndYear\Slivia's project\mythalExp\cases_Part_1_001_050.csv")
