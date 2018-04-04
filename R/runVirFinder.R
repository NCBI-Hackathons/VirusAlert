#!/usr/bin/env Rscript
#usage: Rscript --vanilla runVirFinder.R SRR5383888.fa 0.95
args = commandArgs(trailingOnly=TRUE)

#args[1] should contain path points to the fasta file
#args[2] is the significance cutoff

library("tidyverse")
library(VirFinder)

fasta.inputfile <- args[1]
threshold <- args[2]

pred.result <- VF.pred(fasta.inputfile) %>%
  arrange(score) %>%
  mutate(fname = row_number())

write.table(pred.result, "virfinder_hits.csv", quote = F, sep=",", col.names=F) 

ggplot(pred.result, aes(x=fname, y=score))+
  geom_point()+
  geom_hline(yintercept = threshold, color="red")+
  theme_bw()+
  xlab("read index")+
  ylab("")

ggsave("virfinder_hits.png")

