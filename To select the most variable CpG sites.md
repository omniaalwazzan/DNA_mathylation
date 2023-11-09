To select the most variable CpG sites based on beta or M values, the following steps were taken:

Beta/mValues were extracted using R scripts.
All beta/mValues were merged into a single dataframe.
The merged dataframe, df1, was read and transposed, making 'Sentrix.ID' the row index and CpG sites the columns.
df1 was merged with df2, an ImgID_850k_GT.csv file containing the ground truth information for each 'Sentrix.ID.'
The resulting dataframe, df, had a shape of (1574, 846280).
The 'class' column was dropped from df as it was unnecessary for identifying the most variable features.
The dataframe was transposed again, arranging CpG sites as rows because variance calculation requires features to be in rows.
Next, it is necessary to employ the 'connect_varitons_with_GT.ipyth' script to specifically choose features obtained from the previous steps
Last, run MLP script to evaluate our classifer.
