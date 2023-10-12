# This is to only classify cases matching image id from Silvia's dataset

import pandas as pd

csv_path = r'C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/filterd_tom.csv'
imag_id = pd.read_csv(r"C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/ImgID_output.csv")
IDs_850k = pd.read_csv(r"C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/SentrixID_850k_T.csv")
#subset_beta = pd.read_csv(r"C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/subset_beta.csv")
df =  pd.read_csv(csv_path)

# this is the alignment of Tom's file and Image names extracted from folder names
tom_imgID_df = pd.merge(df, imag_id, left_on='Sample.ID', right_on='Sample_ID', how='inner')
tom_imgID_df = tom_imgID_df.drop_duplicates(subset='Sample.ID')



# We need only sample id, sentrix.id and gt to make our classifir  
new_df = tom_imgID_df[['Sample.ID', 'Sentrix.ID','MC 12.6']] 

# Merg the sentrixid of processed idat files with img id to make sure we are using correct idat  then drop duplicate columns
sentrix_imgId = pd.merge(new_df,IDs_850k,  left_on='Sentrix.ID', right_on='Sentrix.ID', how='inner') 
sentrix_imgId = sentrix_imgId.drop_duplicates(subset='Sentrix.ID')
sentrix_imgId.to_csv(r"C:/Users/omnia/OneDrive - University of Jeddah/1st year of PhD/DNA_methyalation/ImgID_850k_GT.csv")

df["MC 12.6"].nunique()


value_counts = df['Column1'].value_counts()

value_c = sentrix_imgId["MC 12.6"].value_counts()




