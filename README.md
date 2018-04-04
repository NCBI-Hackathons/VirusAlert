<img src="./images/virus-button.png" width="300">

# VirusAlert

Discovery and validation of viruses using long read technology

Goal: To find viruses, both novel and known, in PacBio generated long read metagenomic data in order to find and diagnose viral infections in cultured cells using machine learning. 

Discovery and validation of viruses using VirFinder and RPS BLAST technology trainded with PacBio long read metagenomic data for PacBio long read metagenomic data. 

https://docs.google.com/presentation/d/125WTRdU_TjUtEwrDlG9p-orZDJxauGQl7ojDjvmwlMI/edit?usp=sharing



Bioreactor Use
-------------
VirusAlert is intended to be used to analyze cell cultures used pharma bioractors to periodically check for viral infection.
By running clean cell cultures through LRV, users can set a baseline p-value for their specific cell line. Extreme deviations along with BLAST analysis of 'contaminent' contigs can indicate viral infection and need for further investigation.

 
 Workflow
 -------
 <img src="./images/LongReadVirusesWorkflowII.v.2.png" width="900">

VirFinder
---------
 a novel k-mer based tool for identifying viral sequences from assembled metagenomic data
 GitHub: https://github.com/jessieren/VirFinder
 NCBI: https://www.ncbi.nlm.nih.gov/pubmed/28683828
 
 BLASTn
 -----
 Searches through NCBI database for matches to viral contigs. 
 

Install
-------

1) First, clone the repository:

    git clone https://github.com/NCBI-Hackathons/LongReadViruses.git

Next, run the top-level [install.sh][1] script.

This will install dependencies in the tools directory, and test data files in the data directory.

Usage
-----

Run [longreadviruses.py][2]. 

[1]: install.sh
[2]: longreadviruses.py
[3]: usage.txt


Command Line Options for virusalert.py:

-h|--help  Print this help text.
-v         Print debugging information. [default: true]
-i INPUTS  One or more SRR numbers or fastq/a file paths as input,
           e.g. SRR5150787 or testfile.fq [default: SRR5150787]
-t INTYPE  Type of input provided - can be either srr, fasta or fastq
           [default: srr]
-c CONTDB  Contamination database to use. Default is to download and
           install the RefSeq viral database.
-o OUTDIR  Working directory and where to save results [default: analysis]

Inputs
------
Sequence SRR: All data passed into used in VirusAlert should be long read PacBio shotgun metadata and passed in the form of a SRA Run Accession (SRR).

Threshold [Optional] : minimum P-value for a non contaminated output

Sample Output
------------
 <img src="./images/SampleGraph.png" width="900">
 
 [Tree of viruses image]?


Rough Plan
----------

1. Install (if not present) any BLAST dependencies, R, then VirFinder, and any pip dependencies (docopt):

        sh install.sh

2. Run program with sample options:

        python3 virusalert.py -i <input-SRR-code> <optional p-value> -o <output-results-directory-path>
        
3. Output




This should:

    1. Fetch the fasta data from the SRR code.
    2. Run the fasta data with VirFinder.
    3. Programmatically BLAST to see what the top hits are.
    4. Return a graphic, a file of p-values, and a file of top hits in the output directory (date-stamped).
Citations
---------
VirFinder:
Blast:
Viral RefSeq?:
