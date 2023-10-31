1. Download the Epic array type [ hg38, hg19 or hg450]
2. Extract beta values using processing hg38.R located in this path /data/DERI-MMH/DNA_meth/
3. We need to run step 2 several times for each folder located under this path: data/DERI-MMH/DNA_meth/IDAT/ -- [filtr_p1_850, filtr_p2,...etc ] Filter folders created using step 1 and 2 python scripts
4. Use the merg_df.py located in DNA_Methy/src/ to merge all beta values
5. Use process_850K_beta.ipynb to attach labels to beta values
6. Run MLP 
