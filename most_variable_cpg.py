
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import pyHSICLasso as hsic

path = "C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/Part6_850k_Betas.csv"
#path_4cases = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/Part6_850k_Betas_4samples.csv"
df =  pd.read_csv(path,index_col=(0))

# Method 1: Coefficient of Variation (CV): Calculate the coefficient of variation for each probe, which is the ratio of the standard deviation to the mean.
#Probes with a higher CV indicate higher relative variability.
cv = (df.std(axis=1) / df.mean(axis=1)) * 100  # CV as a percentage
number_of_probes=8000
most_variable_probes_cv = cv.nlargest(n=number_of_probes)

#  Method 2: Interquartile Range (IQR): Calculate the interquartile range (IQR) for each probe. IQR is the range between the 25th and 75th percentiles.
iqr = df.quantile(0.75, axis=1) - df.quantile(0.25, axis=1)
most_variable_probes_iqr = iqr.nlargest(n=number_of_probes)

#  Method 3: Median Absolute Deviation (MAD):
#Calculate the median absolute deviation for each probe, which is the median of the absolute differences from the median.
mad = df.mad(axis=1)
most_variable_probes_mad = mad.nlargest(n=number_of_probes)

# Method 4: Standard Deviation or Variance
# Calculate the standard deviation or variance of methylation levels for each probe across samples.
#Probes with higher standard deviation or variance are considered more variable.
variability = df.var(axis=1)  # Calculate variance across rows (probes)
most_variable_probes_vr = variability.nlargest(n=number_of_probes)

# Plotting

# Assuming most_variable_probes contains the top 10,000 most variable probes
subset_probes = most_variable_probes_vr.sample(n=200)  # Sample 200 probes
plt.figure(figsize=(10, 6))
subset_probes.plot(kind='bar', color='skyblue')
plt.title('Subset of Most Variable Probes')
plt.xlabel('Probe Index')
plt.ylabel('Variability')
plt.xticks(rotation=45)
plt.show()


# Assuming df is your DataFrame with DNA methylation data
sns.heatmap(df.loc[most_variable_probes_vr.index[:200]], cmap='coolwarm')
plt.title('Top 200 Most Variable Probes')
plt.show()




# Method 5: Block HSIC Lasso. This would need our df to have the class as the first col, and the rest cols as features
GT = [0,1,2,3]
df["class"] = GT
# Get the last column
last_column = df.pop(df.columns[-1])
# Insert the last column at the first position
df.insert(0, last_column.name, last_column)
df = df.reset_index(drop=True)
new_path = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/Part6_850k_Betas_4samples_1.csv"
h = hsic.HSICLasso() # initate the class
h.input(new_path)
h.classification(num_feat=50, M=20, B=3)
h.dump() # this save to dataframe
