To select the most variable CpG sites based on beta or M values, the following steps were taken:

1. Beta/mValues were extracted using R scripts.
2. All beta/mValues were merged into a single dataframe.
3. The merged dataframe, df1, was read and transposed, making 'Sentrix.ID' the row index and CpG sites the columns.
4. df1 was merged with df2, an ImgID_850k_GT.csv file containing the ground truth information for each 'Sentrix.ID.'
5. The resulting dataframe, df, had a shape of (1574, 846280).
6. The 'class' column was dropped from df as it was unnecessary for identifying the most variable features.
7. The dataframe was transposed again, arranging CpG sites as rows because variance calculation requires features to be in rows.
8. Next, it is necessary to employ the 'connect_varitons_with_GT.ipyth' script to specifically choose features obtained from the previous steps
9. Last, run MLP script to evaluate our classifer.
