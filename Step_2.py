# This script should be the Step 2

import os
import shutil
import cv2
import pandas as pd

# Specify the source directory (nested folders)
source_directory = r"E:\Methylation_data_all_tumours_May23\Part_1_001_050"

# Specify the destination directory (where you want to move the files)
destination_directory = r"E:\IDAT\Part 1"

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



# This code helps when creating image dataset, labelled by filename
# Thd code will take file names from one directory that match those in CSV and move them to another directory
def step_2(csv_file_path,src,dest_dir):
    
    CSV_DF = pd.read_csv(csv_file_path) # csv file contains image names and labels 
    IDAT_PATH = src # image folder 
    
    IDAT_DIR=os.listdir(src) 
    
    Dist_PATH=dest_dir # lable of the images
    
    
    #Training Split
    for file in CSV_DF['ExtractedName']:
        for name in IDAT_DIR:
            if name.startswith(file):
                sourc = os.path.join(IDAT_PATH,name )
                distination = os.path.join(Dist_PATH, name)
                shutil.move(sourc, distination)
    
    print("All .idat files moved successfully.")

                
## Calling the function
src_part1 = r"E:\IDAT\Part 1"
det_part1 = r"E:\IDAT\filterd_part1"
csv_p1_pth = r"E:\2ndYear\Slivia's project\mythalExp\cases_Part_1_001_050.csv"

step_2(csv_p1_pth,src_part1,det_part1)

# Move 850 Cases to a separate folder, Step2.1

csv_p1_pth_850k = "E:/IDAT/filterd_part1/850k/cases_part1_850k.csv"
dest_850k= "E:/IDAT/filterd_part1/850k"
step_2(csv_p1_pth_850k,det_part1,dest_850k)


def read_tsv(tsv_path):
    tsv = pd.read_table("E:/2ndYear/Slivia's project/Silvia Dataset/epialleles_gbm/EPIC.hg19.manifest.tsv")
    return tsv

def xls2csv(xls_path,csv_path):
    df = pd.read_excel(xls_path)
    csv_df = df.to_csv(csv_path, index=False)
    print(f"Excel file '{xls_path}' has been converted to CSV file '{csv_path}'.")
    return csv_df


    

    

