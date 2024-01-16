
# implementation of clustring method conducted in the paper: https://link.springer.com/content/pdf/10.1007/s00401-014-1315-x.pdf



import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
#mport matplotlib.pyplot as plt
#%%

df = pd.read_csv(r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/mVal_cv_feat.csv",index_col=0)

#df.drop(columns=['label'],inplace=True)
#%%

# Calculate Pairwise similarity between cases using Euclidean distance
euclidean_distances = pdist(df, metric='euclidean')

# Perform hierarchical clustering using Ward's linkage method
ward_linkage_matrix = linkage(euclidean_distances, method='ward')

# Plot a portion of the dendrogram
subset_size = 100  # Choose the number of cases to show
dendrogram(ward_linkage_matrix, truncate_mode='lastp', p=subset_size, labels=df.index)
plt.title("Hierarchical Clustering Dendrogram (Subset)")
plt.xlabel("Cases")
plt.ylabel("Distance")
plt.show()
#%%
# Plot a portion of the dendrogram
subset_size = 20  # Choose the number of cases to show
plt.figure(figsize=(15, 10))  # Set the size of the figure

dendrogram(
    ward_linkage_matrix,
    truncate_mode='lastp',
    p=subset_size,
    labels=df.index,
    orientation='right',
    leaf_font_size=8,  # Adjust the font size
    leaf_rotation=0,   # Rotate the labels if needed
    above_threshold_color='gray',  # Color for links above the threshold
    color_threshold=0.7 * np.max(ward_linkage_matrix[:, 2])  # Adjust the color threshold
)

plt.title("Hierarchical Clustering Dendrogram (Subset)")
plt.xlabel("Distance")
plt.ylabel("Cases")

plt.show()

#%%

# Calculate one-centered Pearson correlation matrix for CpG probes
correlation_matrix = df.T.corr()
#%%


# Convert correlation to distances
distances = 1 - correlation_matrix

# Perform hierarchical clustering using average linkage for CpG probes
average_linkage_matrix = linkage(squareform(distances), method='average')

# Plot dendrogram for CpG probes
plt.figure(figsize=(10, 6))
dendrogram(average_linkage_matrix, labels=df.columns)
plt.title("Hierarchical Clustering Dendrogram for CpG Probes (One-Centered Pearson Correlation)")
plt.xlabel("CpG Probes")
plt.ylabel("Distance")
plt.show()


#%%


# Determine the number of clusters based on distance threshold (adjust as needed)
distance_threshold = 0.7 * np.max(average_linkage_matrix[:, 2])

# Assign clusters using fcluster
clusters = fcluster(average_linkage_matrix, t=distance_threshold, criterion='distance')

# Create a DataFrame with cluster assignments and the original data
result_df = pd.DataFrame({'Cluster': clusters}, index=df.index)

# Optionally, you can add the original features/CpG probes to the result DataFrame
result_df = pd.concat([result_df, df], axis=1)

# Save the result DataFrame to a CSV file
result_df.to_csv(r'\clustering_result.csv')
