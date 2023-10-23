library(minfiData)
library("limma")
library("minfi")
library("RColorBrewer")
library("missMethyl") # Can take a short time...
library("minfiData")
library("Gviz")
library("DMRcate")
library("DMRcatedata")
library("stringr")
library("mCSEA")


## we should always include \\ in any path or we get an error   
dataDirectory <-"C:\\Users\\omnia\\OneDrive - University of Jeddah\\PhD progress\\DNA_methyalation\\Part1_450k_Betas.csv"
beta_values <- read.csv(dataDirectory, header = TRUE, row.names = 1)
colnames(beta_values) <- str_replace_all(colnames(beta_values), "X", "")


beta_values_mat <- as.matrix(beta_values)# change the dataframe beta values to a mtrix

annotation.epic <- read.delim("C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/EPIC_manifest_hg19.tsv") 


methylSet <- MethyLumiM(betas = beta_values_mat)


detP <- detectionP(beta_values_mat)




