#!/usr/bin/Rscript

install.packages("glmnet", dependencies=TRUE)
install.packages("Rcpp", dependencies=TRUE)
source("https://bioconductor.org/biocLite.R")
biocLite("qvalue")
install.packages(Sys.getenv('TOOLS_DIR'), repos=NULL, type='source')
