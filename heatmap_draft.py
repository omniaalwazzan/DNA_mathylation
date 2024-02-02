
import os 
import numpy as np
import pandas as pd  
from matplotlib import pyplot as plt

#%%
path_to_patches = r"C:\Users\omnia\OneDrive - University of Jeddah\PhD progress\DNA_methyalation\src\MUSTANG_GNN\to plot attention\my_edit\test\results\patches\NH20-583"
# We need to make sure the file loacation is the first col as index,# This has coordinates and updated attention scores 
df_path = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/src/MUSTANG_GNN/to plot attention/my_edit/att_NH20-583.csv" 
image_filenames = os.listdir(path_to_patches)
df_img = pd.read_csv(df_path)

patch_size =224

#%%

df_img['norm_score'] = (df_img['score'] - df_img['score'].min()) / (df_img['score'].max() - df_img['score'].min())

#%%

spatial_info_dict = {}

for i, row in df_img.iterrows():
    coordinates = list(map(int, row['Patch_coordinates'].strip('[]').split()))
    
    patch_name = f"{row['ID']}"

    spatial_info_dict[patch_name] = ({
       'x1': coordinates[2],
        'x2': coordinates[3],
        'y1': coordinates[0],
        'y2': coordinates[1]}, 
        row['norm_score'])
    
max_x = int(max(info[0]['x2'] for info in spatial_info_dict.values()))
max_y = int(max(info[0]['y2'] for info in spatial_info_dict.values()))


#%%


att_img = np.zeros((max_y + patch_size, max_x + patch_size), dtype=np.float64)


for patient_id, (coordinates, score) in spatial_info_dict.items():
    x1, x2, y1, y2 = coordinates['x1'], coordinates['x2'], coordinates['y1'], coordinates['y2']

    patch_score = np.ones((patch_size,patch_size))
    

    # Weight the patch by its score
    weighted_patch = patch_score * score

    # Blend the weighted patch onto the canvas
    att_img[y1:y2, x1:x2] = weighted_patch 

plt.imshow(att_img, cmap=plt.cm.RdBu_r)
