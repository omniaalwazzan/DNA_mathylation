import os 
import numpy as np
import pandas as pd 
import PIL.Image as Image
from PIL import Image
import torch.optim as optim

#%%
#screen shot image NH23-275   I
path_to_patches = r"C:\Users\omnia\OneDrive - University of Jeddah\PhD progress\DNA_methyalation\src\MUSTANG_GNN\to plot attention\my_edit\test\results\patches\NH20-583"
# We need to make sure the file loacation is the first col as index
df_path = r"C:\Users\omnia\OneDrive - University of Jeddah\PhD progress\DNA_methyalation\src\MUSTANG_GNN\to plot attention\my_edit\test\results\extracted_patches_edit.csv" 

image_filenames = os.listdir(path_to_patches)
df_img = pd.read_csv(df_path,index_col=(0))
#%%
# Initialize the spatial_info_dict
# spatial_info_dict = {}

# # Iterate over rows in the DataFrame and create the dictionary
# for index, row in df.iterrows():
#     # Extracting coordinates from the df
#     coordinates = list(map(int, row['Patch_coordinates'].strip('[]').split()))
    
#     # Assuming patch names are based on index (e.g., patch_0, patch_1, ...)
#     patch_name = f"{index}"

#     # Save the patch name and coordinates to the dictionary
#     spatial_info_dict[patch_name] = {
#         'x1': coordinates[0],
#         'x2': coordinates[1],
#         'y1': coordinates[2],
#         'y2': coordinates[3]
#     }


spatial_info_dict = {}

for index, row in df_img.iterrows():
    coordinates = list(map(int, row['Patch_coordinates'].strip('[]').split()))
    
    patch_name = f"{index}"

    spatial_info_dict[patch_name] = {
       'x1': coordinates[2],
        'x2': coordinates[3],
        'y1': coordinates[0],
        'y2': coordinates[1]
    }

#%%
from PIL import Image

# Find the maximum dimensions for creating the canvas
max_x = int(max(spatial_info_dict[filename]['x2'] for filename in spatial_info_dict))
max_y = int(max(spatial_info_dict[filename]['y2'] for filename in spatial_info_dict))

# Create the canvas with the maximum dimensions
canvas = np.zeros((max_y + 224, max_x + 224, 3), dtype=np.uint8)

# Place each patch at its specified location on the canvas
for filename in spatial_info_dict:
    x1, x2, y1, y2 = spatial_info_dict[filename]['x1'], spatial_info_dict[filename]['x2'], spatial_info_dict[filename]['y1'], spatial_info_dict[filename]['y2']

    # Load the patch image using PIL
    patch_image_path = os.path.join(path_to_patches, filename)
    patch_image = np.array(Image.open(patch_image_path))
    if patch_image.shape[2] == 4:
        patch_image = patch_image[:, :, :3]

    # Place the patch on the canvas
    canvas[y1:y2, x1:x2, :] = patch_image

# Convert NumPy array to PIL Image
reconstructed_image_pil = Image.fromarray(canvas)

# Display the reconstructed image
reconstructed_image_pil.show()
