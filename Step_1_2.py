import pandas as pd
import shutil 
import os 

def read_tsv(tsv_path):
    tsv = pd.read_table(tsv_path)
    return tsv

def xls2csv(xls_path,csv_path):
    df = pd.read_excel(xls_path)
    csv_df = df.to_csv(csv_path, index=False)
    print(f"Excel file '{xls_path}' has been converted to CSV file '{csv_path}'.")
    return csv_df

### Step one ###

# Specify the source directory (nested folders)
source_directory = "/data/Blizard-MarinoCollab/Methylation_data_all_tumours_May23/Part_1_001_050"
# Specify the destination directory (where we want to move the files)
destination_directory = "/data/DERI-MMH/DNA_meth/IDAT/filtr_p1"  

# Loop through all files in the source directory and its subdirectories
for foldername, subfolders, filenames in os.walk(source_directory):
    for filename in filenames:
        # Check if the file ends with ".idat"
        if filename.endswith(".idat"):
            # Create the full path to the source file
            source_file_path = os.path.join(foldername, filename)
            # Create the full path to the destination file
            destination_file_path = os.path.join(destination_directory, filename)
            # Move the file from the source to the destination
            shutil.move(source_file_path, destination_file_path)
            #print(f"Moved {filename} to {destination_directory}")

print("All .idat files moved successfully.")


def step_2(csv_file_path, src, dest_dir):
    if isinstance(csv_file_path, str):
        # If input is a file path, read the CSV file into a DataFrame
        CSV_DF = pd.read_csv(csv_file_path)
    elif isinstance(csv_file_path, pd.DataFrame):
        # If input is already a DataFrame, use it directly
        CSV_DF = csv_file_path
    else:
        raise ValueError("Invalid input type. Expected file path (string) or DataFrame.")
    
    IDAT_PATH = src  # folder containing idat files 
    IDAT_DIR = os.listdir(src) 
    Dist_PATH = dest_dir  
    
    for file in CSV_DF['ExtractedName']:
        for name in IDAT_DIR:
            if name.startswith(file):
                sourc = os.path.join(IDAT_PATH, name)
                destination = os.path.join(Dist_PATH, name)
                shutil.move(sourc, destination)
    
    print("All .idat files moved successfully.")


# Step 2.1 
# This would create a csv file containing only 850k cases 
def array_850K(csv_path):
    df = pd.read_csv(csv_path)
    # Filter rows containing '850k array data' in the 'path' column
    csv_p1_pth_850k = df[df['FilePath'].str.contains('850k array data', case=False)]
    
    return csv_p1_pth_850k


csv_from_step1 = r"D:\2ndYear\Slivia's project\mythalExp\Part_2_051_100.csv"

# Move 850 Cases to a separate folder, Step2.1
src_part = r"D:\IDAT\filterd_part2"
csv_p1_pth_850k = array_850K(csv_from_step1)
dest_850k= r"D:\IDAT\Part2_850k"
step_2(csv_p1_pth_850k,src_part,dest_850k)




# Count the number of IDat files inside nested folder 

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:32:20 2023

@author: omnia
"""

import pandas as pd
import os

# Specify the path to the directory containing the folders
directory_path = r"E:\Slivia's project\IDAT"

# Loop through each folder in the specified directory
for foldername in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, foldername)
    
    # Check if the current item in the directory is a folder
    if os.path.isdir(folder_path):
        # Count the number of files in the folder
        num_files = len(os.listdir(folder_path))
        
        # Print a statement showing the folder name and the number of files inside
        print(f"Folder '{foldername}' contains {num_files} files.")
