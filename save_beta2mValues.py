library(lumi)

path <- "C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/Part1_850k_Betas.csv"
beta_values <- read.csv(path, header = TRUE, row.names = 1)

colnames(beta_values) <- str_replace_all(colnames(beta_values), "X", "") # here the X is added from the CSV format which is the index for each rows

beta_values_mat <- as.matrix(beta_values) # change the dataframe beta values to a mtrix

mda <- beta2m(beta_values_mat)


