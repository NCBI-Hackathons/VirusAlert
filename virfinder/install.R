#!/usr/bin/Rscript

# see https://www.r-bloggers.com/permanently-setting-the-cran-repository/
local({
  r <- getOption("repos")
  r["CRAN"] <- "http://cran.cnr.berkeley.edu/"
  options(repos = r)
})

toolsdir=Sys.getenv('TOOLS_DIR')
libdir=file.path(toolsdir, 'R')
srcdir=file.path(toolsdir, 'VirFinder')

install.packages("glmnet", dependencies=TRUE, lib=libdir)
install.packages("Rcpp", dependencies=TRUE, lib=libdir)

source("https://bioconductor.org/biocLite.R")
biocLite("qvalue")
install.packages(srcdir, repos=NULL, type='source', lib=libdir)
