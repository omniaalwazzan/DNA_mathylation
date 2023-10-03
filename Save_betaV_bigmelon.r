# IDATs processing.R

# Clear the workspace and load the necessary packages
#rm(list = ls())
library(bigmelon)
library(rtracklayer)
library(readr)
#library(IlluminaHumanMethylationEPICanno.ilm10b4.hg19)

# Load the .idat files that need to be analyzed in the current batch
dataDirectory <- "E:\\Slivia's project\\IDAT\\Part2_850k"   # <--- edit 1 

gfile.all.batches.analysis <- iadd2(path = dataDirectory,
                                    gds = "E:\\Slivia's project\\GDC files\\P2_850_analysis.gds")  # <--- edit 2 
# gfile.30004.analysis <- openfn.gds("Batch_204894630004_analysis.gds")

# Get methylated and unmethylated and betas
mns.all.batches.analysis <- methylated(gfile.all.batches.analysis)[,]
uns.all.batches.analysis <- unmethylated(gfile.all.batches.analysis)[,]
betas.all.batches.analysis <- betas(gfile.all.batches.analysis)

# Remove sex chromosome probes

# Reference to the annotation of EPIC array 
annotation.epic <- read.delim("E:/Slivia's project/IDAT/EPIC_manifest_hg19.tsv") # <--- edit 3
ind.sex.mito.probes <- which(annotation.epic$CpG_chrm == "chrX" | annotation.epic$CpG_chrm == "chrY" | annotation.epic$CpG_chrm == "chrM")
sex.mito.probes.names <- annotation.epic$probeID[ind.sex.mito.probes]

# Probes in autosomes only
mns.all.batches.analysis.auto <- mns.all.batches.analysis[-which(rownames(mns.all.batches.analysis) %in% sex.mito.probes.names),]
uns.all.batches.analysis.auto <- uns.all.batches.analysis[-which(rownames(uns.all.batches.analysis) %in% sex.mito.probes.names),]
design.type.analysis.auto <- fData(gfile.all.batches.analysis)$DESIGN[-which(row.names(fData(gfile.all.batches.analysis)) %in% sex.mito.probes.names)]

# Verify if all the remaining probes are in autosomes
all.equal(rownames(mns.all.batches.analysis.auto), rownames(uns.all.batches.analysis.auto)) # TRUE
ind.cpg.names.in.hg19.anno <- match(rownames(mns.all.batches.analysis.auto), annotation.epic$probeID)
chr.names <- annotation.epic$CpG_chrm[ind.cpg.names.in.hg19.anno]
sort(unique(chr.names)) # 22 autosomes only!

# Perform dasen normalisation on autosomes only to avoid
# introducing technical bias from sex chromosomes
print("Dasen normalization on CpGs from autosomes...")
dasen.norm <- adjustedDasen(mns = mns.all.batches.analysis.auto, 
                            uns = uns.all.batches.analysis.auto,
                            onetwo = design.type.analysis.auto,
                            chr = annotation.epic$CpG_chrm[match(rownames(mns.all.batches.analysis.auto),
                                                                 annotation.epic$probeID)])


# Now cleaning the data
CpGs.autosomes <- dasen.norm[!rownames(dasen.norm) %in% sex.mito.probes.names, ]
SNP.associated.CpGs <- annotation.epic[annotation.epic$MASK_general == TRUE,]
SNP.associated.CpGs.auto <- SNP.associated.CpGs[SNP.associated.CpGs$probeID %in% rownames(CpGs.autosomes),]
CpGs.cleaned <- CpGs.autosomes[!rownames(CpGs.autosomes) %in% SNP.associated.CpGs.auto$probeID, ]

write.csv(as.data.frame(CpGs.cleaned), "E:\\Slivia's project\\betaValues\\Part2_850k_Betas.csv", # <--- edit 4
          row.names = TRUE)

# Close the opened gfile
closefn.gds(gfile.all.batches.analysis)
