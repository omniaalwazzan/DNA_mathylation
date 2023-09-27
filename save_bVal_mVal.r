# NOTE: in Champ we need to place the csv sample_sheet inside the folder containing idat files 

library("ChAMP")
## we should always include \\ in any path or we get an error

dataDirectory <- "D:\\2ndYear\\temp\\Methylation_data_all_tumours_May23\\Part_1_001_050\\#002_450k Array Data 2015-02\\9989536145\\"

myLoad <- champ.load(dataDirectory,arraytype="450K")
myImport <- champ.import(dataDirectory)

# save beta
csv_path_beta <- "D:\\2ndYear\\Slivia's project\\mythalExp\\batch1\\betaV.csv"
write.csv(myImport$beta, csv_path, row.names=T)

# Save m-Values
csv_path_mVal <- "D:\\2ndYear\\Slivia's project\\mythalExp\\batch1\\mVal.csv"
write.csv(myImport$M, csv_path, row.names=T)


  #### METHOD 2 ####
# save filtered beata and m-values
# NOTE: in Champ we need to place the csv sample_sheet inside the folder containing idat files 


# Filter out failed probs from both matrices
myfilter_m <- champ.filter(beta=myImport$beta,M=myImport$M,pd=myImport$pd,detP=myImport$detP,beadcount=myImport$beadcount)

# save beta
csv_path_beta <- "E:\\2ndYear\\Slivia's project\\mythalExp\\batch1\\9989540035_betaV.csv"
write.csv(myfilter_m$beta, csv_path_beta, row.names=T)

# Save m-Values
csv_path_mVal <- "E:\\2ndYear\\Slivia's project\\mythalExp\\batch1\\9989540035_mVal.csv"
write.csv(myfilter_m$M, csv_path_mVal, row.names=T)
#E:\2ndYear\Slivia's project\mythalExp\batch1\mValues


####### This block we need to do it after extracting all beta & M vlaues from all samples ######
# myfilter <- champ.filter(beta=myImport$beta,M=myImport$M,pd=myImport$pd,detP=myImport$detP,beadcount=myImport$beadcount)
# CpG.GUI(CpG=rownames(myfilter$M),arraytype="450K")
# par("mar")
# par(mar=c(1,1,1,1))
# champ.QC()
# QC.GUI(beta=myfilter$beta,arraytype="450K")
# myNormBeta <- champ.norm(beta=myfilter$beta,arraytype="450K",cores=5)
#champ.SVD(beta=myNormBeta %>% as.data.frame(), pd=myLoad$pd)

#############
# Normalize m vlaues is not working an the followin is the error
#Error in champ.BMIQ(beta[, x], design.v, sampleID = colnames(beta)[x],  : 
#                      task 2 failed - "need at least 2 points to select a bandwidth automatically"
#myNorm <- champ.norm(beta=myfilter$M,arraytype="450K",cores=5)



## runcombat is not working on one sample group
#myCombat <- champ.runCombat(beta=myfilter$M,pd=myLoad$pd,batchname=c("Sample_Name"))

