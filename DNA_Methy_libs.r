

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("wateRmelon")


if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("bigmelon")

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("lumi")


install_github("achilleasNP/IlluminaHumanMethylationEPICanno.ilm10b5.hg38") # Comment this part because we already installed it


# library(bigmelon)
library(rtracklayer)
library(readr)
library(stringr)
library(lumi)

# Need to use the hg38 annotation for EPICv1 array
library(devtools)
library(wateRmelon)
library(IlluminaHumanMethylationEPICanno.ilm10b5.hg38)
